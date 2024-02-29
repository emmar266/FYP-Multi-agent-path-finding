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

    #can be used for


    #For static and buffer could for each agent try to be a static buffer and ensure each agent can find a


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


    def createPathMatrix(self,paths):
        collisionMatrix = [[0] * len(self.agents) for _ in range(len(self.agents))]
        for agent, path in paths.pathWithoutTime.items():
            for agent2,path2 in paths.pathWithoutTime.items():
                if agent == agent2:
                    continue
                if self.findPathSimilarities(path, path2):
                    print(type(self.agents))
                    print(self.agents.index(agent))
                    print(self.agents.index(agent2))
                    collisionMatrix[self.agents.index(agent)][self.agents.index(agent2)] =1
                    collisionMatrix[self.agents.index(agent2)][self.agents.index(agent)] =1
        return collisionMatrix


    #for every path check if whitespace aro und
    def attemptTwo(self,numReservedAreas):
        #Get initial free paths for all agents
        if self.initalPaths is None:
            self.getInitialPaths()
        #Create a collision matrix which shows agents who are colliding
        collisionM = self.createPathMatrix(self.initalPaths)
        #as of python 3.7 you can sort dict - sort dict based on length of path
        sortedpaths = dict(sorted(self.initalPaths.paths.items(), key=lambda path: len(path[1])*-1))
        potentialAgents = {}
        #iterate through all agents and check if the current agent was reserved, would paths that collide still
        #be able to get to dest
        for agent in sortedpaths:
            agentPossible = True
            #get row of agent and check if collide with current agent, denoted by 1 in matrix
            for index,collision in enumerate(collisionM[self.agents.index(agent)]):
                if collision == 1:
                    #Create a copy of the graph so you can add static obstacles - ie reserved area
                    tempGraph = copy.deepcopy(self.graph)
                    tempGraph.setStaticObstacle(self.initalPaths.pathWithoutTime[agent])
                    graphM = graphManger(tempGraph)
                    aStarObj = aStar(graphM)
                    #need to regenerate path with ra as static obstacle
                    possiblePath = aStarObj.findPath([],self.agents[index],self.graph.width * self.graph.length)
                    if possiblePath is False:
                        #Not a possible reserved agent
                        agentPossible = False
                        break
            if agentPossible:
                potentialAgents[agent] = sortedpaths[agent]
        self.collisionM = collisionM
        return potentialAgents

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

    def check(self,potentialAgents):
        for index,agent in enumerate(potentialAgents):
            for index2,agent2 in enumerate(potentialAgents):
                if self.collisionM[self.agents.index(agent)][self.agents.index(agent2)] == 1:
                    return False
        return True

    #agents in potentialAgents
    def findCompatibleRA(self,potentialAgents, collisionMatrix, desiredNumRA):
        if desiredNumRA ==1:
            return [potentialAgents[0]]
        self.collisionM = collisionMatrix
        for agent in potentialAgents:
            #find agents not colliding with agent that are reserved
            possibleCompa = self.unCollidingRA(collisionMatrix,agent,potentialAgents)
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

    #
    def findCompatibleRaRandom(self,potentialAgents,desiredNumRA):
        for i in range(desiredNumRA *2):
            random.shuffle(potentialAgents)
            if self.check(potentialAgents[:desiredNumRA]):
                return potentialAgents[:desiredNumRA]
        return False