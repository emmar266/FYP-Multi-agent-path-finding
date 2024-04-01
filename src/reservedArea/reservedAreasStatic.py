from src.setupGrid import graphManger
from src.cbs.cbs import highLevel
from src.reservedArea.reservedAgentsDecider import reservedAgentDecider,RAAttemptOne,RAAttemptTwo,RAattemptThree
from src.pp.prioritised import prioritisedPlanning
from src.pathObj import Paths
import time

class reservedAreasStatic:
    def __init__(self,graph, agents):
        self.graph = graphManger(graph)
        self.graphArea = self.graph.graph.width * self.graph.graph.length
        self.agents = agents
        #self.reservedAreaDecider = reservedAgentDecider(graph, agents)

    #tested works
    def reservedAreaDeciderVersionOne(self,numRA):
        reservedAgentDecider = RAAttemptTwo(self.graph.graph,self.agents)
        start = time.time()
        potentialAgents = reservedAgentDecider.attemptTwo(numRA)
        if len(potentialAgents)>0:
            raAgents =reservedAgentDecider.findCompatibleRaRandom(list(potentialAgents.keys()), numRA)
            end = time.time()
            print("DeciderTime = ", end - start)
            start = time.time()
            paths = self.staticCBS(raAgents, potentialAgents)
            end =time.time()
            print("CBS time - ", end - start)
            return paths
        else:
            print("noRa")
            end = time.time()
            print("DeciderTime = ", end - start)
            start = time.time()
            paths = self.staticCBS([], [])
            end =time.time()
            print("CBS time - ", end - start)
            return paths
    #tested works
    def reservedAreaDeciderVersionOne2(self,numRA):
        reservedAgentDecider = RAAttemptTwo(self.graph.graph,self.agents)
        start = time.time()
        potentialAgents = reservedAgentDecider.attemptTwo(numRA)
        end = time.time()
        print("DeciderTime = ", end -start)
        raAgents =reservedAgentDecider.findCompatibleRA(list(potentialAgents.keys()),numRA)
        start = time.time()
        paths = self.staticCBS(raAgents,potentialAgents)
        end = time.time()
        print("CBS run = ", end -start)
        return paths

    def reservedAreaDeciderVersionTwo(self,numRA):
        reservedAgentDecider = RAattemptThree(self.graph.graph,self.agents)
        start = time.time()
        raAgents, paths = reservedAgentDecider.attemptThree(numRA)
        end = time.time()
        print("DeciderTime = ", end -start)
        if len(raAgents) ==0:
            print("noRa")
        start = time.time()
        paths = self.staticCBS(raAgents,paths)
        end = time.time()
        print("CBS run = ", end -start)
        return paths

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
        return cbsAlgo.cbs()

