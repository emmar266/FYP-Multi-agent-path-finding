from src.setupGrid import graphManger
from src.aStar import aStar
from src.pathObj import Paths
import copy


class reservedAgentDecider:
    def __init__(self,graph,agents):
        self.graph = graph
        self.agents = agents

    def convertPathToConstraintsStatic(self,paths):
        dynamic = []
        for path in paths:
            for step in path:
                dynamic.append([step.x,step.y,step.time])
        return dynamic

    def tempGraphChange(self,constraints):
        tempGraph = copy.deepcopy(self.graph)


    #This will work for one agent
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
    def raDontBlockStartEnd(self,reservedPath):
        for agent in self.agents:
            if agent.startPos in reservedPath or agent.goal in reservedPath:
                return False
        return True

    #For static and buffer could for each agent try to be a static buffer and ensure each agent can find a


    #this is flawed as its not a common node - with time incorporated but common x y
    def findPathSimilarities(self,path1,path2):
        for node in path1:
            if node in path2:
                return True
        return False


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
        """
        for agentIndex,agent in enumerate(self.agents):
            for agentTwoIndex,agent2 in enumerate(self.agents):
                if agent.agentId == agent2.agentId:
                    continue
                if self.findPathSimilarities(paths[agent.agentId],paths[agent2.agentId]):
                    #have no way to guarantee that agentids are spanning from 0 - len(agents)-1 must index
                    collisionMatrix[agentIndex,agentTwoIndex]
                    collisionMatrix[agentTwoIndex,agentIndex]"""
        return collisionMatrix


    #for every path check if whitespace aro und
    def attemptTwo(self,numReservedAreas):
        graphM = graphManger(self.graph)
        aStarObj = aStar(graphM)
        paths = {}
        for agent in self.agents:
            paths[agent] = aStarObj.findPath([], agent, self.graph.width * self.graph.length)
        paths = Paths(paths)
        paths.makePathAsList()
        collisionM = self.createPathMatrix(paths)
        #as of python 3.7 you can sort dict
        sortedpaths = dict(sorted(paths.paths.items(), key=lambda path: len(path[1])*-1))
        potentialAgents = {}

        for agent in sortedpaths:
            agentPossible = True
            for index,collision in enumerate(collisionM[self.agents.index(agent)]):
                if collision == 1:
                    tempGraph = copy.deepcopy(self.graph)
                    tempGraph.setStaticObstacle(paths.pathWithoutTime[agent])
                    graphM = graphManger(tempGraph)
                    aStarObj = aStar(graphM)
                    #need to regen path with ra as
                    possiblePath = aStarObj.findPath([],self.agents[index],self.graph.width * self.graph.length)
                    if possiblePath is False:
                        #Not a possible reserved agent
                        agentPossible = False
                        break
            if agentPossible:
                potentialAgents[agent] = sortedpaths[agent]
        #need to know create some way of deciding what agents are compatible as reserved areas together
        if len(potentialAgents) < numReservedAreas:
            return False
        #need to get compatible reservedAgents
        compatibleRAAgents ={}
        for agent in potentialAgents:
            for agent2 in potentialAgents:
                if agent == agent2:
                    continue
                if collisionM[]


        return potentialAgents

