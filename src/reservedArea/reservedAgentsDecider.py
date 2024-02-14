from src.setupGrid import graphManger
from src.aStar import aStar
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


    #for every path check if whitespace around
    def attemptTwo(self):
        pass