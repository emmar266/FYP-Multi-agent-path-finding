from src.setupGrid import graphManger
from src.cbs.cbs import highLevel

class graphPartition:


    #initially gonna just code the part where partitions are given and agents within said partition are given
    #Cbs
    def givenPartition(self,graphs, agentsPerGraph):
        pathsPerPartition = {}
        for index,graph in enumerate(graphs):
            algo = highLevel(graph,agentsPerGraph[index])
            pathsPerPartition[index] = algo.cbs()
        return pathsPerPartition




