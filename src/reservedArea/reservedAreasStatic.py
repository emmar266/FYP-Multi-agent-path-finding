from src.setupGrid import graphManger
from src.cbs.cbs import highLevel
from src.reservedArea.reservedAgentsDecider import reservedAgentDecider,RAAttemptOne,RAAttemptTwo,RAattemptThree
from src.pp.prioritised import prioritisedPlanning
from src.pathObj import Paths

class reservedAreasStatic:
    def __init__(self,graph, agents):
        self.graph = graphManger(graph)
        self.graphArea = self.graph.graph.width * self.graph.graph.length
        self.agents = agents
        #self.reservedAreaDecider = reservedAgentDecider(graph, agents)

    #tested works
    def reservedAreaDeciderVersionOne(self,numRA):
        reservedAgentDecider = RAAttemptTwo(self.graph.graph,self.agents)
        potentialAgents = reservedAgentDecider.attemptTwo(numRA)
        raAgents =reservedAgentDecider.findCompatibleRaRandom(list(potentialAgents.keys()), numRA)
        self.staticCBS(raAgents,potentialAgents)
    #tested works
    def reservedAreaDeciderVersionOne2(self,numRA):
        reservedAgentDecider = RAAttemptTwo(self.graph.graph,self.agents)
        potentialAgents = reservedAgentDecider.attemptTwo(numRA)
        raAgents =reservedAgentDecider.findCompatibleRA(list(potentialAgents.keys()),numRA)
        self.staticCBS(raAgents,potentialAgents)

    def reservedAreaDeciderVersionTwo(self,numRA):
        reservedAgentDecider = RAattemptThree(self.graph.graph,self.agents)
        potentialAgents = reservedAgentDecider.attemptThree(numRA)
        self.staticCBS(potentialAgents,potentialAgents)

    def convertPathToConstraintsStatic(self,paths):
        dynamic = []
        for path in paths:
            for step in path:
                dynamic.append([step.x,step.y])
        return dynamic

    def staticCBS(self,reservedAgents, agentPaths):
        agents = self.agents
        for agent in reservedAgents:
            agents.remove(agent)
            self.graph.graph.setStaticObstacle(agentPaths[agent])
        #run cbs as usual
        cbsAlgo =highLevel(self.graph.graph,agents)
        cbsAlgo.cbs()

