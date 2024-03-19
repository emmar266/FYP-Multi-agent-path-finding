from src.graphPartition.graphPartitionDecider.decider import graphPartitionDecider
from src.aStar import aStar
from src.setupGrid import graphManger
from src.pathObj import Paths



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
