from src.aStar import aStar
from src.setupGrid import graphManger
from src.cbs.cbs import highLevel
from src.pp.prioritised import prioritisedPlanning



class reservedAreasStatic:
    def __init__(self,graph, agents):
        self.graph = graph
        self.graphArea = graph.width * graph.length
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
        reservedPaths = {}
        for agent in reservedAgents:
            reservedPaths[agent] = aStar.findPath([], agent,self.graphArea)
        # add to graph with setStaticObject
        self.graph.graph.setStaticObstacle(self.convertPathToConstraintsStatic(reservedPaths))
        #run cbs as usual
        cbsAlgo =highLevel(self.graph,self.agents)
        cbsAlgo.cbs()
        pass

    def staticPP(self,reservedAgents):
        # Calculate paths for all reserved agents
        reservedPaths = {}
        for agent in reservedAgents:
            reservedPaths[agent] = aStar.findPath([], agent,self.graphArea)
        # add to graph with setStaticObject
        self.graph.graph.setStaticObstacle(self.convertPathToConstraintsStatic(reservedPaths))
        #run pp as usual
        p = prioritisedPlanning(self.graph, self.agents)
        val = p.randomisedOrdering()

        pass

    def dynamicCBS(self):
        #calculate paths for all reserved agents
        #create constraints based on these agents
            # will have to modify cbs to allow the function to take in initial constraints
            # or I could allow the graph to have constraints - easier to modify cbs and makes more sense i thnk

        pass

    def dynamicPP(self):

        pass
