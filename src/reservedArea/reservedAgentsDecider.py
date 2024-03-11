from src.setupGrid import graphManger
from src.aStar import aStar
from src.pathObj import Paths
import copy
import random

class reservedAgentDecider:
    def __init__(self,graph,agents):
        self.graph = graph
        self.agents = agents
        self.collisionM = None
        self.initalPaths = None

    def unCollidingRA(self,collisionMatrix,agent,potentialAgents):
        indexOfCurrent = self.agents.index(agent)
        row = collisionMatrix[indexOfCurrent]
        possibleCompatible = []
        for index,value in enumerate(row):
            #possible other agent
            if indexOfCurrent == index:
                continue
            if self.agents[index] in potentialAgents:
                if value != 1:
                    possibleCompatible.append(self.agents[index])
        return possibleCompatible
    def createPathMatrix(self,paths):
        collisionMatrix = [[0] * len(self.agents) for _ in range(len(self.agents))]
        for agent, path in paths.pathWithoutTime.items():
            for agent2,path2 in paths.pathWithoutTime.items():
                if agent == agent2:
                    continue
                if self.findPathSimilarities(path, path2):
                    collisionMatrix[self.agents.index(agent)][self.agents.index(agent2)] =1
                    collisionMatrix[self.agents.index(agent2)][self.agents.index(agent)] =1
        return collisionMatrix

    #this is flawed as its not a common node - with time incorporated but common x y
    def findPathSimilarities(self,path1,path2):
        for node in path1:
            if node in path2:
                return True
        return False


    def getInitialPaths(self):
        graphM = graphManger(self.graph)
        aStarObj = aStar(graphM)
        paths = {}
        for agent in self.agents:
            paths[agent] = aStarObj.findPath([], agent, self.graph.width * self.graph.length)
        #Create Path object and create
        paths = Paths(paths)
        paths.makePathAsList()
        self.initalPaths = paths

    def check(self,potentialAgents):
        for index,agent in enumerate(potentialAgents):
            for index2,agent2 in enumerate(potentialAgents):
                if self.collisionM[self.agents.index(agent)][self.agents.index(agent2)] == 1:
                    return False
        return True

class RAAttemptOne(reservedAgentDecider):
    def convertPathToConstraintsStatic(self,paths):
        dynamic = []
        for path in paths:
            for step in path:
                dynamic.append([step.x,step.y,step.time])
        return dynamic

    #This attempt is not ideal as it will favour agents to be reserved which are completely separate from other agents
    #   - Which means likely no improvement in regards to time for CBS
    def attemptOne(self):
        graphM = graphManger(self.graph)
        aStarObj = aStar(graphM)
        paths = {}
        for agent in self.agents:
            paths[agent.agentId] = aStarObj.findPath([],agent,self.graph.width * self.graph.length)
        potentialAgent = {}
        for potentialRA in self.agents:

            allPaths = [ path for agent,path in paths.items() if agent != potentialRA.agentId]
            constraints = self.convertPathToConstraintsStatic(allPaths)
            #these constraints need to be static - which means modifying and then reverting the graph
            tempGraph = copy.deepcopy(self.graph)
            tempGraph.setStaticObstacle(constraints)
            graphM = graphManger(tempGraph)
            aStarObj = aStar(graphM)
            path = aStarObj.findPath([], potentialRA,self.graph.width * self.graph.length)
            if path is not False:
                potentialAgent[potentialRA] = path
        return potentialAgent



class RAAttemptTwo(reservedAgentDecider):
    def attemptTwo(self, numReservedAreas):
        # Get initial free paths for all agents
        if self.initalPaths is None:
            self.getInitialPaths()
        # Create a collision matrix which shows agents who are colliding
        collisionM = self.createPathMatrix(self.initalPaths)
        # as of python 3.7 you can sort dict - sort dict based on length of path
        sortedpaths = dict(sorted(self.initalPaths.paths.items(), key=lambda path: len(path[1]) * -1))
        potentialAgents = {}
        # iterate through all agents and check if the current agent was reserved, would paths that collide still
        # be able to get to dest
        for agent in sortedpaths:
            agentPossible = True
            # get row of agent and check if collide with current agent, denoted by 1 in matrix
            for index, collision in enumerate(collisionM[self.agents.index(agent)]):
                if collision == 1:
                    # Create a copy of the graph so you can add static obstacles - ie reserved area
                    tempGraph = copy.deepcopy(self.graph)
                    tempGraph.setStaticObstacle(self.initalPaths.pathWithoutTime[agent])
                    graphM = graphManger(tempGraph)
                    aStarObj = aStar(graphM)
                    # need to regenerate path with ra as static obstacle
                    possiblePath = aStarObj.findPath([], self.agents[index], self.graph.width * self.graph.length)
                    if possiblePath is False:
                        # Not a possible reserved agent
                        agentPossible = False
                        break
            if agentPossible:
                potentialAgents[agent] = self.initalPaths.pathWithoutTime[agent]
        self.collisionM = collisionM
        return potentialAgents


    #agents in potentialAgents
    def findCompatibleRA(self,potentialAgents, desiredNumRA):
        if desiredNumRA ==1:
            return [potentialAgents[0]]
        for agent in potentialAgents:
            #find agents not colliding with agent that are reserved
            possibleCompa = self.unCollidingRA(self.collisionM,agent,potentialAgents)
            if len(possibleCompa) < desiredNumRA-1:
                continue
            #need to check
            for i in range(desiredNumRA):
                random.shuffle(possibleCompa)
                if self.check(possibleCompa[:desiredNumRA-1]):
                    toReturn = possibleCompa[:desiredNumRA-1]
                    toReturn.append(agent)
                    return toReturn
        return False


    #this is dealing with a list but potentialAgents is of type dict
    def findCompatibleRaRandom(self,potentialAgents,desiredNumRA):
        if desiredNumRA ==1:
            return [potentialAgents[0]]
        for i in range(desiredNumRA *2):
            random.shuffle(potentialAgents)
            if self.check(potentialAgents[:desiredNumRA]):
                return potentialAgents[:desiredNumRA]
        return False


class RAattemptThree(reservedAgentDecider):

    def getColliding(self,agents):
        toCheck = set()
        for agent in agents:
            indexOfCurrent = self.agents.index(agent)
            row = self.collisionM[indexOfCurrent]
            for index, value in enumerate(row):
                # possible other agent
                if indexOfCurrent == index:
                    continue
                if value == 1:
                    toCheck.add(self.agents[index])
        return toCheck
            #get nodes that are colliding based on matrix

    def getTimeFreePathofRA(self, agents):
        toReserve = []
        for agent in agents:
            toReserve += self.initalPaths.pathWithoutTime[agent]
        return toReserve

    #checks if collididng agents have a path
        # could extend this to check all agents outside those reserved
        # this would be slower but ensure that the reserved agents together doesn't prevent any agent from
    def checkIfAgentsHaveValidPath(self,reserved,agentsToCheck):
        tempGraph = copy.deepcopy(self.graph)
        paths = self.getTimeFreePathofRA(reserved)
        tempGraph.setStaticObstacle(paths)
        graphM = graphManger(tempGraph)
        aStarObj = aStar(graphM)
        for unreserved in agentsToCheck:
            path = aStarObj.findPath([],unreserved,self.graph.width * self.graph.length)
            if path is False:
                return False
        return True



    #get intial paths for all agents
    #sort based on length - want to prioritise longer paths
    #with first longest path - randomise combination of other potential reserved agents
        # first check if all in combination are combatible - check matrix
        #Next check that all the other agents that collide with those in the combination can still get to dest
            # keep set of objects that do collide
    def attemptThree(self,numReservedAreas):
        #Get initial free paths for all agents
        if self.initalPaths is None:
            self.getInitialPaths()

        collisionM = self.createPathMatrix(self.initalPaths)
        sortedpaths = dict(sorted(self.initalPaths.paths.items(), key=lambda path: len(path[1])*-1))
        potentialAgents = {}
        #iterate for numReservedAreas *2 checking
        #if numReservedAreas == 1:
        #    return sortedpaths
        self.collisionM = collisionM
        for agent in sortedpaths:
            # find agents not colliding with agent that are reserved - think i need to add agent into possibleCOmpa list
            # rather than get it from potential agents
            # need to check if the possibleCompa + curent agent when combined can generate
            for i in range(numReservedAreas):
                possibleCompa = list(sortedpaths.keys())#.remove(agent)
                possibleCompa.remove(agent)
                #if possibleCompa is the same length as numReserved then there's no point in shuffling it x times
                #if len(possibleCompa)
                random.shuffle(possibleCompa)
                #need to first check if those in possible compa collide
                current = possibleCompa[:numReservedAreas-1]
                current.append(agent)
                if self.check(current) is False:
                    continue
                #get agents colliding with those in possibleCompa
                toCheck = self.getColliding(current)
                # check if those can plan there path around those in possibleCompa
                if self.checkIfAgentsHaveValidPath(current, toCheck):
                    return current, self.initalPaths.pathWithoutTime
        return False

