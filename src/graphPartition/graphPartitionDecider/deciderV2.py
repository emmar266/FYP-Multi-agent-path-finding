from src.graphPartition.graphPartitionDecider.decider import graphPartitionDecider
from src.graphPartition.graphPartitionDecider.deciderV1 import graphPartitionDeciderV1
from src.aStar import aStar
from src.setupGrid import graphManger

from src.graphPartition.partitionExtension import partitionExtension

class graphPartitionDeciderV2(graphPartitionDecider):
    def __init__(self,graph, agents):
        super().__init__(graph, agents)
        self.initalAnalysis = graphPartitionDeciderV1(graph,agents)

    #for this i'm going to use this
    def dictAssign(self, key, dict,toAdd):
        if key not in dict:
            dict[key] = [toAdd]
        else:
            dict[key].append(toAdd)
        return dict
    def assignAgentsToPartition(self, partitions):
        agentAssignment = {}
        #partialCovering going to keep track of agents that are partially in one partition
        partialCovering = {}
        for agent in self.agents:
            for partition in partitions:
                # check if start location is within partition

                if partition.minX <= agent.startPos[0] <= partition.maxX and partition.minY <= agent.startPos[1] <= partition.maxY:
                    if partition.minX <= agent.goal[0] <= partition.maxX and partition.minY <= agent.goal[
                        1] <= partition.maxY:
                        #can assign to partition
                        self.dictAssign(partition, agentAssignment, agent)
                    else:
                        self.dictAssign("None",agentAssignment, agent)
                        self.dictAssign(partition, partialCovering, agent)
                        break
                elif partition.minX <= agent.goal[0] <= partition.maxX and partition.minY <= agent.goal[
                            1] <= partition.maxY:
                    #can't be assigned to any other complete partition if partially in another
                    self.dictAssign("None", agentAssignment, agent)
                    self.dictAssign(agent, partialCovering, partition)
                    break
                else:
                    self.dictAssign("None", agentAssignment, agent)
        return agentAssignment, partialCovering

    #One issue i have is that by potentially extending the graph I'll have to call buildPartition twice which may not be ideal?

    def checkInOtherPartition(self,currentStep,potentialExtension ,partitions):
        for partition in partitions:
            if potentialExtension == partitions:
                continue
            else:
                if partition.checkIfInPartition(currentStep):
                    return False
        return True

    # if only one partial covering can check if you can extend the partition
    # Should i enforce that it has to be a certain distance from the partition ?
    # could get path and add i block buffer around it and extend it like that
    # think i'm going to have to generate the path add buffer and then check if it intrudes on any other partition
    def analysePartialCovering(self,coverings,partitions):
        toExtend = {}
        extend = True
        for agent in coverings:
            if len(coverings[agent]) >1:
                #can't extend as it's in multiple partitions
                continue
            else:
                minX,maxX, minY, maxY   = None,None,None, None
                path = self.initialPaths.pathWithoutTime[agent]
                for step in path:
                    if minX is None or step[0] < minX:
                        minX = step[0]
                    if maxX is None or step[0]> maxX:
                        maxX = step[0]
                    if minY is None or step[1] < minY:
                        minY = step[1]
                    if maxY is None or step[1] > maxY:
                        maxY = step[1]
                    if self.checkInOtherPartition(step,coverings[agent][0], partitions) :
                        #not possible to extend
                        extend = False
                #extend partition
                if extend:
                    if coverings[agent][0] in toExtend:
                        toExtend[coverings[agent][0]].addPathToContension(path, minX,maxX, minY, maxY)
                    else:
                        toAdd = partitionExtension()
                        toAdd.addPathToContension(path, minX,maxX, minY, maxY)
                        toExtend[coverings[agent][0]] = [toAdd]
                extend = True
        return toExtend

    def extendPartition(self,toExtend):
        for partition in toExtend:
            partition.extendGraph(toExtend[partition][0])

    def partitonV2(self,popPercent, bufferPercent):
        partitions = self.initalAnalysis.graphAnalysis(popPercent,bufferPercent)
        self.initialPaths = self.initalAnalysis.initialPaths
        agents, partialCoverings = self.assignAgentsToPartition(partitions)
        #need to remove those agents involved in extension from None in agetns
        toExtend = self.analysePartialCovering(partialCoverings, partitions)
        self.extendPartition(toExtend)
        return partitions

