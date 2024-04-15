import copy

from src.setupGrid import graphManger
from src.cbs.cbs import highLevel, ConstraintsStructure
from src.graphPartition.graphPartitionDecider.deciderV1 import graphPartitionDeciderV1
from src.graphPartition.graphPartitionDecider.deciderV2 import graphPartitionDeciderV2
import time
from src.pathObj import Paths

class graphPartition:

    def buildConstraints(self, constraints, agents):
        constraintStruct = {}
        for agent in agents:
            constraints = copy.deepcopy(constraints)
            constraintStruct[agent.agentId] = ConstraintsStructure(agent.agentId, constraints)
        return constraintStruct

    def convertPathsToOringinalGraphCoordinates(self, paths, partition):
        for path in paths.values():
            for step in path:
                step.x = partition.minX + step.x
                step.y = partition.minY + step.y



    #initially gonna just code the part where partitions are given and agents within said partition are given
    #Cbs
    def givenPartition(self,originalGraph,graphs, agentsPerGraph):
        pathsPerPartition = {}

        longestTime = 0
        for index,graph in enumerate(graphs):
            if graph in agentsPerGraph:
                print("Agents for partition ", len(agentsPerGraph[graph]))
                algo = highLevel(graph.partitionGraph,agentsPerGraph[graph])
                start = time.time()
                paths = algo.cbs()
                self.convertPathsToOringinalGraphCoordinates(paths,graph)

                pathsPerPartition.update(paths)
                end = time.time()
                if longestTime == 0:
                    longestTime = end -start
                if end -start > longestTime:
                    longestTime = end - start

        if "None" in agentsPerGraph:
            pathOBj = Paths(pathsPerPartition)
            pathOBj.makePathAsList()
            print("Og graph agents ", len(agentsPerGraph["None"]))
            algo = highLevel(originalGraph, agentsPerGraph["None"])
            start = time.time()
            constraints = {}
            if len(pathOBj.pathAsList) >0:
                a = list(pathOBj.pathAsList.values())
                toadd = []
                for sublist in pathOBj.pathAsList.values():
                    toadd.extend(sublist)
                constraints = self.buildConstraints(toadd, agentsPerGraph["None"])
            pathsPerPartition.update( algo.cbs(constraints))
            end = time.time()
            print("time taken -", longestTime+(end-start))
        else:
            print("time-taken - ", longestTime)
        count = 0
        for val in pathsPerPartition:
            count += len(pathsPerPartition[val])
            if pathsPerPartition[val] == False:
                print("False Val found")
            print("agent ", val.agentId)
            for step in pathsPerPartition[val]:
                print("("+ str(step.x)+ ","+ str(step.y)+ "),",end="")
            print("")
        print("Steps ", count)
        return pathsPerPartition

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
        for agent in agents:
            assigned = False
            for partition in partitions:
                if assigned:
                    break
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
                        break
            if assigned is False:
                self.dictAssign("None", agentAssignment, agent)
        return agentAssignment

                # check if end location is within partition
                #if in one and not the other than there is no perfect partition for the current agent as
                #no partitions intersect at this point


    def getPartitionsV1(self,agents,graph,popPercent,bufferRatio):
        start = time.time()
        partitionDecider = graphPartitionDeciderV1(graph, agents)
        partitions = partitionDecider.graphAnalysis(popPercent, bufferRatio )
        agentAssigned = self.assignAgentsToPartition(partitions, agents)
        end = time.time()
        print("Decider Time - ", end -start)
        print("Num partitions built - ",len(partitions))
        print("Partitions assigned with agents = ",len(agentAssigned)-1)
        self.givenPartition(graph,partitions, agentAssigned)

    def getPartitionsV2(self,agents,graph,popPercent,bufferRatio):
        start = time.time()
        partitionDecider = graphPartitionDeciderV2(graph, agents)
        partitions = partitionDecider.partitonV2(popPercent, bufferRatio)
        agentAssigned = self.assignAgentsToPartition(partitions, agents)
        end = time.time()
        print("Num partitions built - ",len(partitions))
        print("Partitions assigned with agents = ",len(agentAssigned)-1)
        print("decider time - ", end-start)
        self.givenPartition(graph,partitions, agentAssigned)
