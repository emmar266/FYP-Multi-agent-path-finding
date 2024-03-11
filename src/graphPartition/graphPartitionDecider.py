from src.aStar import aStar
from src.setupGrid import graphManger
from collections import defaultdict
from src.graphPartition.subGraph import subGraph
from src.graphPartition.partition import Partition
from src.pathObj import Paths
from src.graphPartition.partitionExtension import partitionExtension

#TODO What is not considered in my graph decider is areas of the graph not covered by heatmap,
# need to further

class graphPartitionDecider:
    def __init__(self,graph, agents ):
        self.initialGraph = graph
        self.agents = agents


class graphPartitionDeciderV1(graphPartitionDecider):


    #Linearly split up graphs - maybe just split in half etc
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

    #when merging it should the merging of partitions not the merging of subgraphs
    def merge(self, toMerge,current,existing):
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
        graphM = graphManger(self.initialGraph)
        aStarObj = aStar(graphM)
        nodes = defaultdict(int)
        count = 0
        for agent in self.agents:
            path = aStarObj.findPath([], agent,self.initialGraph.width * self.initialGraph.length)
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
            else:
                newPart = Partition()
                newPart.addSubGraph(currentSub)
                existingPartitions.append(newPart)
        for partition in existingPartitions:
            partition.buildPartiion(self.initialGraph)
        return existingPartitions


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
                    self.dictAssign(partition, partialCovering, agent)
                    break
                else:
                    self.dictAssign("None", agentAssignment, agent)
        return agentAssignment, partialCovering

    #One issue i have is that by potentially extending the graph I'll have to call buildPartition twice which may not be ideal?

    def checkInOtherPartition(self,currentStep, partitions,potentialExtension):
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
    def analysePartialCovering(self,coverings):
        aStarObj = aStar(self.initialGraph)
        toExtend = {}
        for agent in coverings:
            if len(coverings[agent]) >1:
                #can't extend as it's in multiple partitions
                continue
            else:
                minX,maxX, minY, maxY   = None,None,None, None
                path = aStarObj.findPath([],agent,self.initialGraph.width * self.initialGraph.length)
                for step in path:
                    if step[0] < minX:
                        minX = step[0]
                    if step[0]> maxX:
                        maxX = step[0]
                    if step[1] < minY:
                        minY = step[1]
                    if step[1] > maxY:
                        maxY = step[1]
                    if self.checkInOtherPartition(step,coverings[agent][0]):
                        #not possible to extend
                        break
                #extend partition
                if coverings[agent][0] in toExtend:
                    toExtend[coverings[agent][0]].addPathToContension(path, minX,maxX, minY, maxY)
                else:
                    toAdd = partitionExtension()
                    toAdd.addPathToContension(path, minX,maxX, minY, maxY)
                    toExtend[coverings[agent]][0] = [toAdd]
        return toExtend

    def extendPartition(self,toExtend):
        for partition in toExtend:
            partition.extendGraph(toExtend[partition])
        return list(toExtend.keys())

    def partitonV2(self,popPercent, bufferPercent):
        partitions = self.initalAnalysis.graphAnalysis(popPercent,bufferPercent)
        agents, partialCoverings = self.assignAgentsToPartition(partitions)
        toExtend = self.analysePartialCovering(partialCoverings)
        self.extendPartition(toExtend)
        return partitions






class clusterPartition(graphPartitionDecider):

    def getInitialPaths(self):
        graphM = graphManger(self.initialGraph)
        aStarObj = aStar(graphM)
        paths = {}
        for agent in self.agents:
            paths[agent] = aStarObj.findPath([], agent, self.initialGraph.width * self.initialGraph.length)
        #Create Path object and create
        paths = Paths(paths)
        paths.makePathAsList()
        return paths

    #this can't use
    def checkCollision(self,pathOne, pathTwo):
        for step in pathOne:
            if step in pathTwo:
                return True
        return False

    def getCluster(self, agents):
        groupings =[] # list of sets - ordering is maintained
        indexOfGroup = {}
        for agent, path in agents.items():
            for agentTwo, path2 in agents.items():
                if agent == agentTwo:
                    continue
                if self.checkCollision(path, path2):
                    if agent in indexOfGroup and agentTwo in indexOfGroup:
                        #must merge sets
                        setOne = groupings[indexOfGroup[agent]]
                        setTwo = groupings[indexOfGroup[agentTwo]]
                        #merging this is gonna be horrible


                    elif agent in indexOfGroup:
                        # add agent2 to the set agent is in
                        indexOfGroup[agentTwo] = indexOfGroup[agent]
                        groupings[indexOfGroup[agent]].add(agentTwo)
                    elif agentTwo in indexOfGroup:
                        #add agent to the set agent is in
                        indexOfGroup[agent] = indexOfGroup[agentTwo]
                        groupings[indexOfGroup[agentTwo]].add(agent)
                    else:
                        #create new set
                        toAdd = set()
                        toAdd.add(agent)
                        toAdd.add(agentTwo)
                        indexOfGroup[agent] = len(groupings)
                        indexOfGroup[agentTwo] = len(groupings)
                        groupings.append(toAdd)

        return groupings

    def findCollisions(self,agents):
        collisions = {}
        for agent, path in agents.pathWithoutTime.items():
            for agentTwo, path2 in agents.pathWithoutTime.items():
                if agent == agentTwo:
                    continue
                if self.checkCollision(path, path2):
                    if agent in collisions:
                        if agentTwo not in collisions[agent]:
                            collisions[agent].append(agentTwo)
                    else:
                        collisions[agent] = [agentTwo]
                    if agentTwo in collisions:
                        if agent not in collisions[agentTwo]:
                            collisions[agentTwo].append(agent)
                    else:
                        collisions[agentTwo] = [agent]

        return collisions

    def createCluster(self,collision,agents ):
        clusters = set()
        for agent in agents:
            currentSet = set()
            currentSet.add(agent)
            for colliding in collision[agent]:
                currentSet.update(collision[colliding])
            clusters.add(currentSet)
        return clusters

    def createClusterv2(self,collisions):
        pass

    def getClusters(self):
        #run initial paths
        #for any agents that have colliding paths must be clustered together
        #Ken mentioned that i then would not be able to paraleleise f
        paths = self.getInitialPaths()
        #check for colliding paths and group them together
        #self.getCluster(paths.pathAsList)
        collisions = self.findCollisions(paths)
        self.createCluster(collisions, self.agents)




