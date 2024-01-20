import src.aStar as aStar
import random


class prioritisedPlanning:
    def __init__(self,graph,agents) :
        self.graph = graph
        self.agents = agents
        self.aStar = aStar.aStar(self.graph)

    def randomisedOrdering(self):
        for i in range(0,len(self.agents)//2):
            paths,pathUnFound = self.getPathsOnPriority()
            if pathUnFound:
                self.randomisedOrdering() 
                continue
            else:
                return paths
        return False

    def getPathsOnPriority(self):
        paths = {}
        atLeastOnePathNotFound = False
        currentConstraints = []
        for currentAgent in self.agents:
            agentPath = self.aStar.findPath(currentConstraints, currentAgent )
            currentConstraints += self.pathToConstraints(agentPath)
            if agentPath is False:
                #no path found 
                paths[currentAgent] = "Not Found"
                atLeastOnePathNotFound = True

            else:
                paths[currentAgent] = agentPath
        return paths,atLeastOnePathNotFound

    def pathToConstraints(self,path):
        constraints = []
        for node in path:
            constraints.append([node.x,node.y,node.time])
        return constraints

