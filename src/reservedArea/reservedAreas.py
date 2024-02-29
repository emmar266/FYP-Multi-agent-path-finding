from src.aStar import aStar
from src.setupGrid import graphManger
from src.cbs.cbs import highLevel, ConstraintsStructure
from src.reservedArea.reservedAgentsDecider import reservedAgentDecider
from src.pp.prioritised import prioritisedPlanning
from src.pathObj import Paths

class reservedAreasStatic:
    def __init__(self,graph, agents):
        self.graph = graphManger(graph)
        self.graphArea = self.graph.graph.width * self.graph.graph.length
        self.agents = agents
        self.reservedAreaDecider = reservedAgentDecider(graph, agents)

    def reservedAreaDeciderVersionOne(self,numRA):
        potenialAgents = self.reservedAreaDecider.attemptTwo(numRA)
        raAgents = self.reservedAreaDecider.findCompatibleRA(potenialAgents,numRA)
        self.staticCBS(raAgents)

    def reservedAreaDeciderVersionOne(self,numRA):
        potenialAgents = self.reservedAreaDecider.attemptTwo(numRA)
        raAgents = self.reservedAreaDecider.findCompatibleRaRandom(potenialAgents, numRA)
        self.staticCBS(raAgents)

    def convertPathToConstraintsStatic(self,paths):
        dynamic = []
        for path in paths:
            for step in path:
                dynamic.append([step.x,step.y])
        return dynamic

    def staticCBS(self,reservedAgents):
        for agent,path in reservedAgents.items():
            self.graph.graph.setStaticObstacle(path)
        #run cbs as usual
        cbsAlgo =highLevel(self.graph.graph,self.agents)
        cbsAlgo.cbs()

class reservedAreaBufferArea:
    def setupInitialConstraintsCBS(self,paths):
        constraints = {}
        for agent in self.agents:
            constraints[agent.agentId] = ConstraintsStructure(agent.agentId, paths)
        return constraints


    def addBufferConstraints(self,constraints):
        initialLengthOfConstraints = len(constraints)
        i = 0
        while i < initialLengthOfConstraints:
            current = constraints[i]
            constraints += self.graph.findValidNeighbours(current, constraints)
            i+=1
        return constraints


    def dynamicCBSWithBuffer(self,reservedAgents):
        aStarObj = aStar(self.graph)
        reservedPaths = []
        for agent in reservedAgents:
            reservedPaths += aStarObj.findPath([], agent,self.graphArea)
        constraints = self.setupInitialConstraintsCBS(reservedPaths)
        bufferedConstraints = self.addBufferConstraints(constraints)
        cbsAlgo =highLevel(self.graph.graph,self.agents)
        cbsAlgo.cbs(bufferedConstraints)

    #should have a dynamic obj with buffer for PP
    #def