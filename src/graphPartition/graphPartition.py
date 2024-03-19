from src.setupGrid import graphManger
from src.cbs.cbs import highLevel
from src.graphPartition.graphPartitionDecider.deciderV1 import graphPartitionDeciderV1
from src.graphPartition.graphPartitionDecider.deciderV2 import graphPartitionDeciderV2

class graphPartition:


    #initially gonna just code the part where partitions are given and agents within said partition are given
    #Cbs
    def givenPartition(self,graphs, agentsPerGraph):
        pathsPerPartition = {}
        for index,graph in enumerate(graphs):
            algo = highLevel(graph,agentsPerGraph[index])
            pathsPerPartition[index] = algo.cbs()
        return pathsPerPartition

    def dictAssign(self, key, dict,toAdd):
        if key not in dict:
            dict[key] = [toAdd]
        else:
            dict[key].append(toAdd)
        return dict

    #Something to be aware of - depending how i deal with areas without a popular spot in my graph partition this may need to be adjusted
    def assignAgentsToPartition(self, partitions,agents):
        agentAssignment = {}
        for agent in agents:
            for partition in partitions:
                # check if start location is within partition
                if partition.minX <= agent.startPos[0] <= partition.maxX and partition.minY <= agent.startPos[1] <= partition.maxY:
                    if partition.minX <= agent.goal[0] <= partition.maxX and partition.minY <= agent.goal[
                        1] <= partition.maxY:
                        #can assign to partition
                        self.dictAssign(partition, agentAssignment, agent)
                    else:
                        self.dictAssign("None",agentAssignment, agent)
                        break
                elif partition.minX <= agent.goal[0] <= partition.maxX and partition.minY <= agent.goal[
                            1] <= partition.maxY:
                    #can't be assigned to any other complete partition if partially in another
                    self.dictAssign("None", agentAssignment, agent)
                    break
        return agentAssignment

                # check if end location is within partition
                #if in one and not the other than there is no perfect partition for the current agent as
                #no partitions intersect at this point


    def getPartitionsV1(self,agents,graph):
        partitionDecider = graphPartitionDeciderV1(graph, agents)
        partitions = partitionDecider.graphAnalysis(0.6, 0.2 )
        agentAssigned = self.assignAgentsToPartition(partitions, agents)
        self.givenPartition(partitions, agentAssigned)

    def getPartitionsV2(self,agents,graph):
        partitionDecider = graphPartitionDeciderV2(graph, agents)
        partitions = partitionDecider.partitonV2(0.6, 0.2)
        self.givenPartition(partitions)
