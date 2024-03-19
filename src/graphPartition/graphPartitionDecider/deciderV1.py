from src.graphPartition.graphPartitionDecider.decider import graphPartitionDecider
from src.aStar import aStar
from src.setupGrid import graphManger
from collections import defaultdict
from src.graphPartition.subGraph import subGraph
from src.graphPartition.partition import Partition
from src.pathObj import Paths


class graphPartitionDeciderV1(graphPartitionDecider):

    def getInitialPaths(self):
       graphM = graphManger(self.initialGraph)
       aStarObj = aStar(graphM)
       paths = {}
       for agent in self.agents:
           path = aStarObj.findPath([], agent, self.initialGraph.width * self.initialGraph.length)
           paths[agent] = path
       self.initialPaths = Paths(paths)
       self.initialPaths.makePathAsList()



    #items in existingSubGraph will
    def checkIfSubGraphIntersect(self,current,existingSubGraph):
        tomerge = []
        for existingGraph in existingSubGraph:
            if existingGraph.minX <= current.leftX <= existingGraph.maxX or existingGraph.minX <= current.rightX <= existingGraph.maxX:
                if existingGraph.minY <= current.topY <= existingGraph.maxY or existingGraph.minY <= current.bottomY <= existingGraph.maxY:
                    tomerge.append(existingGraph)
            #need to if current is in range of others
        return tomerge

    #when merging it should the merging of partitions not the merging of subgraphs
    def merge(self, toMerge,current,existing):
        #just take the first
        mergeTo = toMerge[0]
        for i in range(1, len(toMerge)):
            existing.remove(toMerge[i])
            for subGraph in toMerge[i].subGraphs:
                mergeTo.addSubGraph(subGraph)
        mergeTo.addSubGraph(current)

    def buildHeatMapV1(self, popularityPercentage):
        nodes = defaultdict(int)
        count = 0
        for agent,path in self.initialPaths.pathWithoutTime.items():
            if path is False:
                return False
            for step in path:
                nodes[tuple(step)] += 1
            count += len(path)
        popularityThres = count * popularityPercentage
        freqVisited = [key for key, count in nodes.items() if count > popularityThres]
        return freqVisited


    def addTimeRange(self,step,additionalTimeNode,timeRange):
        for i in range(step[2], timeRange + step[2]):
            additionalTimeNode[step[0],step[1],i] += 1



    def buildHeatMapV2(self, popularityPercentage, timeRange):
        nodes = defaultdict(int)
        additionalTimeNode = defaultdict(int)
        count = 0
        for agent,path in  self.initialPaths.pathAsList.items():
            if path is False:
                return False
            for step in path:
                if additionalTimeNode[tuple(step)] > 0 and nodes[tuple(step)] ==0:
                    nodes[tuple(step)] = additionalTimeNode[tuple(step)] +1
                else:
                    nodes[tuple(step)] += 1
                self.addTimeRange(step, additionalTimeNode,timeRange)
            count += len(path)
        popularityThres = count * popularityPercentage
        freqVisited = [key for key, count in nodes.items() if count > popularityThres]
        return freqVisited

    def checkWithinGraph(self,left,right,top,bottom):
        if right >= self.initialGraph.width:
            right = self.initialGraph.width -1
        if bottom >= self.initialGraph.length:
            bottom = self.initialGraph.length -1
        if left <0:
            left = 0
        if top < 0:
            top = 0
        return left,right,top,bottom


    # Popularity Percentage - what percentage is considered popular
    # BufferRatio - what percentage of the original graph should be considered for a buffer area
    #should also put a restriction on how small a partition can exist within the graph
    def graphAnalysis(self, popularityPercentage, bufferRatio):
        self.getInitialPaths()
        freqVisited = self.buildHeatMapV2(popularityPercentage, 4)
        existingPartitions = []
        xBuffer, yBuffer = bufferRatio, bufferRatio
        for popVal in freqVisited:
            left, right, top, bottom = popVal[0] - xBuffer, popVal[0] + xBuffer, popVal[1] - yBuffer, popVal[1] + yBuffer
            left, right, top, bottom = self.checkWithinGraph(left,right,top,bottom)
            currentSub = subGraph(left,right,top,bottom)
            # need to check if this one intersects with any others if so merge
            toMerge = self.checkIfSubGraphIntersect(currentSub, existingPartitions)
            if len(toMerge) >0 :
                self.merge(toMerge, currentSub,existingPartitions)
            else:
                newPart = Partition()
                newPart.addSubGraph(currentSub)
                existingPartitions.append(newPart)
        for partition in existingPartitions:
            partition.buildPartiion(self.initialGraph)
        return existingPartitions
