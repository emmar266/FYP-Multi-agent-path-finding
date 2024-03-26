from src.graphPartition.graphPartition import graphPartition
import time
from src.cbs.cbs import highLevel

class GraphPartitionExperiments:

    def givenPartition(self,graphs, agentsPerGraph):
        pathsPerPartition = {}
        longestTime = None
        for index,graph in enumerate(graphs):
            algo = highLevel(graph,agentsPerGraph[index])
            pathsPerPartition[index] = algo.cbs()
        return pathsPerPartition, longestTime


    def graphPartitionV1(self, agents, graph, popPercent,buffer):
        obj = graphPartition()
        start = time.time()
        obj.getPartitionsV1(agents,graph, popPercent,buffer)
        end = time.time()
        return end - start

    def graphPartitionV2(self, agents, graph, popPercent, buffer):
        obj = graphPartition()
        start = time.time()
        obj.getPartitionsV1(agents, graph,popPercent, buffer)
        end = time.time()
        return end - start
