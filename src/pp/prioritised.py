import src.aStar as aStar
import random


class prioritisedPlanning:
    def __init__(self,graph,agents) :
        self.graph = graph
        self.agents = agents
        self.aStar = aStar.aStar(self.graph)

    def randomisedOrdering(self,initialConstraints=[]):
        for i in range(0,len(self.agents)//2):
            paths,pathUnFound = self.getPathsOnPriority(initialConstraints)
            if pathUnFound:
                self.randomisedOrdering() 
                continue
            else:
                return paths
        return False

    def getPathsOnPriority(self, initialConstraints=[]):
        paths = {}
        atLeastOnePathNotFound = False
        currentConstraints = initialConstraints
        previousLongestPath = 0
        for currentAgent in self.agents:
            if previousLongestPath == 0:
                agentPath = self.aStar.findPath(currentConstraints, currentAgent, self.graph.graph.length * self.graph.graph.width )
            else:
                agentPath = self.aStar.findPath(currentConstraints, currentAgent, previousLongestPath)
            currentConstraints += self.pathToConstraints(agentPath)
            if agentPath is False:
                #no path found 
                paths[currentAgent] = "Not Found"
                atLeastOnePathNotFound = True

            else:
                paths[currentAgent] = agentPath
                if len(paths[currentAgent]) > previousLongestPath:
                    previousLongestPath = len(paths[currentAgent])
        return paths,atLeastOnePathNotFound

    def pathToConstraints(self,path):
        constraints = []
        for node in path:
            constraints.append([node.x,node.y,node.time])
        return constraints

