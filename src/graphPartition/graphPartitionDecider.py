from src.aStar import aStar
from src.setupGrid import graphManger
from collections import defaultdict
class graphPartitionDecider:
    def __init__(self,graph, agents ):
        self.initialGraph = graph
        self.agents = agents

    #Linearly split up graphs
    def randomisePartition(self):
        pass



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
        for popVal in freqVisited:
            pass
            #build buffer area around each popVal
            #if it intersects, merge partitions



        #should disregard nodes with count 1 - visited by one node only



