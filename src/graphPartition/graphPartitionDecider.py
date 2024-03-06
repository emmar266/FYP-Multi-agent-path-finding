from src.aStar import aStar
from src.setupGrid import graphManger
from collections import defaultdict
from subGraph import subGraph

#TODO What is not considered in my graph decider is areas of the graph not covered by heatmap,
# need to further

class graphPartitionDecider:
    def __init__(self,graph, agents ):
        self.initialGraph = graph
        self.agents = agents

    #Linearly split up graphs
    def randomisePartition(self):
        pass


    def getBufferSize(self,bufferRatio):
        #based on the buffer size ratio determine how many nodes are in the original graph
        xBufferSize = round(self.initialGraph.width * bufferRatio)
        yBufferSize = round(self.initialGraph.length * bufferRatio)
        return xBufferSize, yBufferSize

    def getBufferDetails(self,point, xbuff, ybuff):
        #get bounds for buffer area to fill into subgraph class
        left,right,top,bottom = point[0] - xbuff,point[0] + xbuff,point[1] - ybuff, point[1]+ ybuff
        return left,right,top, bottom


    #items in existingSubGraph will
    def checkIfSubGraphIntersect(self,current,existingSubGraph):
        tomerge = []
        for existingGraph in existingSubGraph:
            if existingGraph.minX <= current.leftX <= existingGraph.maxX or existingGraph.minX <= current.rightX <= existingGraph.maxX:
                if existingGraph.minY <= current.topY <= existingGraph.maxY or existingGraph.minY <= current.bottomY <= existingGraph.maxY:
                    tomerge.append(existingGraph)
            #need to if current is in range of others

        return tomerge
    def merge(self,current, toMerge,existing):
        #just take the first
        mergeTo = toMerge[0]
        for i in range(1, len(toMerge)):
            existing.remove(toMerge[i])
            for subGraph in toMerge[i].subGraphs:
                mergeTo.addSubGraph(subGraph)
        mergeTo.addSubGraph(current)





    # Popularity Percentage - what percentage is considered popular
    # BufferRatio - what percentage of the original graph should be considered for a buffer area
    #should also put a restriction on how small a partition can exist within the graph
    def graphAnalysis(self, popularityPercentage, bufferRatio):
        graphM = graphManger(self.graph)
        aStarObj = aStar(graphM)
        nodes = defaultdict(int)
        count = 0
        for agent in self.agents:
            path = aStarObj.findPath([], agent,self.graph.width * self.graph.length)
            if path is False:
                return False
            for step in path:
                nodes[step.x, step.y] += 1
            count += len(path)
        popularityThres = count * popularityPercentage
        freqVisited = [key for key, count in nodes.items() if count > popularityThres]
        existingPartitions = []
        for popVal in freqVisited:
            xBuffer, yBuffer = self.getBufferSize(bufferRatio)
            left, right, top, bottom = popVal[0] - xBuffer, popVal[0] + xBuffer, popVal[1] - yBuffer, popVal[1] + yBuffer
            currentSub = subGraph(left,right,top,bottom)
            # need to check if this one intersects with any others if so merge
            toMerge = self.checkIfSubGraphIntersect(currentSub, existingPartitions)
            if len(toMerge) >0 :
                self.merge(toMerge, currentSub,existingPartitions)
        for partition in existingPartitions:
            partition.buildPartiion(self.graph)
        return existingPartitions






