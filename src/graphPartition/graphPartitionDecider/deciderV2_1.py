from src.graphPartition.graphPartitionDecider.decider import graphPartitionDecider
from src.graphPartition.graphPartitionDecider.deciderV1 import graphPartitionDeciderV1
from src.aStar import aStar
from src.setupGrid import graphManger
import copy
from src.graphPartition.partitionExtension import partitionExtension

class graphPartitionDeciderV2_1(graphPartitionDecider):
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
    def checkIfInPartition(self,partition,coordinates):
        x = coordinates[0] - partition.minX
        y = coordinates[1] - partition.minY
        if partition.partitionGraph.floorPlan[y][x] == "Blocked":
            return False
        return True

    def changeAgentCoordinates(self,agent, partition):
        newStart = [agent.startPos[0] - partition.minX, agent.startPos[1] - partition.minY]
        newGoal = [agent.goal[0] - partition.minX, agent.goal[1] - partition.minY]
        newAgent = copy.deepcopy(agent)
        newAgent.startPos = newStart
        newAgent.goal = newGoal
        return newAgent

    #Something to be aware of - depending how i deal with areas without a popular spot in my graph partition this may need to be adjusted
    def assignAgentsToPartition(self, partitions,agents):
        agentAssignment = {}
        partialCovering = {}
        for agent in agents:
            assigned = False
            for partition in partitions:
                #v = partition.partitionGraph.floorPlan[agent.goal[0]][agent.goal[1]]
                # check if start location is within partition
                if partition.minX <= agent.startPos[0] <= partition.maxX and partition.minY <= agent.startPos[1] <= partition.maxY:
                   if self.checkIfInPartition(partition,agent.startPos):

                        if partition.minX <= agent.goal[0] <= partition.maxX and partition.minY <= agent.goal[1] <= partition.maxY:
                            if self.checkIfInPartition(partition, agent.goal):
                            #can assign to partition
                                assigned = True

                                self.dictAssign(partition, agentAssignment,self.changeAgentCoordinates(agent, partition) )
                            else:
                                assigned = True
                                self.dictAssign("None", agentAssignment, agent)
                                self.dictAssign( agent, partialCovering,partition)
                                break
                        else:
                            assigned = True
                            self.dictAssign("None",agentAssignment, agent)
                            break
                elif partition.minX <= agent.goal[0] <= partition.maxX and partition.minY <= agent.goal[1] <= partition.maxY:
                    if self.checkIfInPartition(partition, agent.goal):

                        #can't be assigned to any other complete partition if partially in another
                        assigned = True
                        self.dictAssign("None", agentAssignment, agent)
                        self.dictAssign( agent, partialCovering,partition)
                        break
            if assigned is False:
                self.dictAssign("None", agentAssignment, agent)
        return agentAssignment, partialCovering

    #One issue i have is that by potentially extending the graph I'll have to call buildPartition twice which may not be ideal?
    def checkInOtherPartitionExtension(self, currentStep, previousExpansions, timePoint):
        collidings = []
        for partitions in previousExpansions.values():
            for partitionExtension in partitions:
                for index,path in enumerate(partitionExtension.pathsToIncorporate):
                    if currentStep in path:
                        collidings.append(partitionExtension.agentsToIncorporate[index])
                            #return True
        return collidings


    def checkInOtherPartition(self,currentStep,potentialExtension ,partitions,previousExpansions, time):
        allcollidings = []
        for partition in partitions:
            if potentialExtension == partition:
                continue
            else:
                if partition.checkIfInPartition(currentStep):
                    return True, allcollidings
                collidings = self.checkInOtherPartitionExtension(currentStep, previousExpansions,time+1)
                if len(collidings) > 0:
                     allcollidings+= collidings
                    #return True
        return False, allcollidings

    # if only one partial covering can check if you can extend the partition
    # Should i enforce that it has to be a certain distance from the partition ?
    # could get path and add i block buffer around it and extend it like that
    # think i'm going to have to generate the path add buffer and then check if it intrudes on any other partition
    def analysePartialCovering(self,coverings,partitions):
        toExtend = {}
        extend = True
        extensionCollidings = {}
        for agent in coverings:
            if len(coverings[agent]) >1:
                #can't extend as it's in multiple partitions
                continue
            else:
                minX,maxX, minY, maxY   = None,None,None, None
                path = self.initialPaths.pathWithoutTime[agent]
                currentColldings = []
                for index,step in enumerate(path):
                    if minX is None or step[0] < minX:
                        minX = step[0]
                    if maxX is None or step[0]> maxX:
                        maxX = step[0]
                    if minY is None or step[1] < minY:
                        minY = step[1]
                    if maxY is None or step[1] > maxY:
                        maxY = step[1]
                    inOtherPartitions, collidings = self.checkInOtherPartition(step,coverings[agent][0], partitions,toExtend, index)
                    if len(collidings) >0:
                        currentColldings += collidings
                    if inOtherPartitions:
                        #not possible to extend
                        extend = False
                        break
                #extend partition
                if extend:
                    if coverings[agent][0] in toExtend:
                        val = toExtend[coverings[agent][0]][0]
                        toExtend[coverings[agent][0]][0].addPathToContension(path, minX,maxX, minY, maxY)
                        toExtend[coverings[agent][0]][0].agentsToIncorporate.append(agent)
                    else:
                        toAdd = partitionExtension()
                        toAdd.agentsToIncorporate.append(agent)
                        toAdd.addPathToContension(path, minX,maxX, minY, maxY)
                        toExtend[coverings[agent][0]] = [toAdd]
                    extensionCollidings[agent] = list(set(currentColldings))
                extend = True
        return toExtend, extensionCollidings

    def extendPartition(self,toExtend):
        for partition in toExtend:
            partition.extendGraph(toExtend[partition][0])

    def partitonV2(self,popPercent, bufferPercent):
        partitions = self.initalAnalysis.graphAnalysis(popPercent,bufferPercent)
        self.initialPaths = self.initalAnalysis.initialPaths
        agents, partialCoverings = self.assignAgentsToPartition(partitions,self.agents)
        #need to remove those agents involved in extension from None in agetns
        toExtend, collidings = self.analysePartialCovering(partialCoverings, partitions)
        self.extendPartition(toExtend)
        return partitions, collidings

