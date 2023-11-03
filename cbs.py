from tree import Tree, node
import aStar
import setupGrid

class Constraint:
    def __init__(self,x,y,time,agentsInvolved) -> None:
        self.x = x
        self.y = y
        self.time = time
        self.agentsInvolved = agentsInvolved

    def __eq__(self, objectToCompare) -> bool:
        if self.x == objectToCompare.x and self.y==objectToCompare.y and self.time == objectToCompare.time and self.agentsInvolved == objectToCompare.agentsInvolved:
            return True
        return False

class highLevel:
    def __init__(self,graph) -> None:
        self.agents = {} # gonna be structured with id:path
        self.constraints = {} #"agent": (x,y) : [time1,time2 ...]
        
        self.graphManager =setupGrid.graphManger(graph)
        self.aStar = aStar(self.graphManager)


    def cbs(self,graph,agents):
        #tree = x
        #first iteration of path finding for all agents
        #   return paths 
        #   check for collisions 
        highLevelTree = Tree()
        #run path finding algo for all paths no constraints - should return list of all paths for each robot/task
        paths = self.findPathsForAll([]) 
        currentCollisions = self.collsionsFound(paths)

        highLevelTree.setInitialNode = node(currentCollisions,self.calculateNodeCost(paths))
        #need check which will break out of function if there's no collisons 
        if len(currentCollisions) ==0:
            #no collisions first time around
            return paths
        
        
        #from the collisons we want to create x new nodes on a tree based on the number of robots in the collison 
        #   can't be more than 4 if robots can only move L R U D - could be 8 if diagonal movements allowed - nawr 
        

        #find constraints
        # run first 
        currentCollisions = None
        while currentCollisions != None:
            #run path finding for everynode with new collisons
            #lowlevel 
            currentCollisions = self.checkForcollsions(paths)

    def calculateNodeCost(self,paths):
        totalCost = 0
        for agent in paths:
            totalCost += agent.time
        return totalCost

    def checkForcollsions(self,paths): #returns the collsions found as a list or dict etc 
        collisions = {}
        for agent in paths:
            for agent2 in paths:
                if agent == agent2:
                    continue
                i = 0
                while i < len(paths[agent]) or i < len(paths[agent2]):
                    stepAgentOne = paths[agent][i]
                    stepAgentTwo = paths[agent2][i]
                    if stepAgentOne == stepAgentTwo:
                        newConstraint = Constraint(stepAgentOne.x,stepAgentOne.y,stepAgentOne.time,[agent,agent2])
                        if newConstraint in collisions[agent]:
                            collisions[agent].append(newConstraint)
                            collisions[agent2].append(newConstraint)
                        #collison detected
        return collisions

    def findPathsForAll(self,constraints):
        paths = {}
        for agent in self.agents:
            paths[agent] = self.aStar.findPath(constraints,agent)
            #paths.append() # this will return the paths
        return paths