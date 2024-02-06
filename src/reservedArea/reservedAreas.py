from src.aStar import aStar
from src.setupGrid import graphManger
from src.cbs.cbs import highLevel, ConstraintsStructure
from src.pp.prioritised import prioritisedPlanning

class reservedAreasStatic:
    def __init__(self,graph, agents):
        self.graph = graphManger(graph)
        self.graphArea = self.graph.graph.width * self.graph.graph.length
        self.agents = agents



    def checkReservedAgentsDontCollide(self):
        #should return true or false
        pass

    def convertPathToConstraintsStatic(self,paths):
        dynamic = []
        for path in paths:
            for step in paths:
                dynamic.append([step.x,step.y])
        return dynamic

    def staticCBS(self,reservedAgents):
        # Calculate paths for all reserved agents
        aStarObj = aStar(self.graph)
        reservedPaths = []
        for agent in reservedAgents:
            reservedPaths += aStarObj.findPath([],agent,self.graphArea)
        # add to graph with setStaticObject
        self.graph.graph.setStaticObstacle(self.convertPathToConstraintsStatic(reservedPaths))
        #run cbs as usual
        cbsAlgo =highLevel(self.graph.graph,self.agents)
        cbsAlgo.cbs()

    def staticPP(self,reservedAgents):
        # Calculate paths for all reserved agents
        aStarObj = aStar(self.graph)
        reservedPaths = []
        for agent in reservedAgents:
            reservedPaths += aStarObj.findPath([],agent,self.graphArea)
        # add to graph with setStaticObject
        self.graph.graph.setStaticObstacle(self.convertPathToConstraintsStatic(reservedPaths))
        #run pp as usual
        p = prioritisedPlanning(self.graph, self.agents)
        val = p.randomisedOrdering()

    def setupInitialConstraintsCBS(self,paths):
        constraints = {}
        for agent in self.agents:
            constraints[agent.agentId] = ConstraintsStructure(agent.agentId, paths)
        return constraints


    def dynamicCBS(self,reservedAgents):
        aStarObj = aStar(self.graph)
        reservedPaths = []
        for agent in reservedAgents:
            reservedPaths += aStarObj.findPath([], agent,self.graphArea)
        constraints = self.setupInitialConstraintsCBS(reservedPaths)
        #run cbs as usual
        cbsAlgo =highLevel(self.graph.graph,self.agents)
        cbsAlgo.cbs(constraints)

    def dynamicPP(self, reservedAgents):
        aStarObj = aStar(self.graph)
        reservedPaths = []
        for agent in reservedAgents:
            reservedPaths += aStarObj.findPath([], agent,self.graphArea)
        p = prioritisedPlanning(self.graph, self.agents)
        val = p.randomisedOrdering(reservedPaths)