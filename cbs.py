from tree import Tree, node
import aStar
import setupGrid

class Collision:
    def __init__(self,x,y,time,agentsInvolved) -> None:
        self.x = x
        self.y = y
        self.time = time
        self.agentsInvolved = agentsInvolved

    def __eq__(self, objectToCompare) -> bool:
        if self.x == objectToCompare.x and self.y==objectToCompare.y and self.time == objectToCompare.time and set(self.agentsInvolved) == set(objectToCompare.agentsInvolved):
            return True
        return False

class highLevel:
    def __init__(self,graph) -> None:
        self.agents = {} # gonna be structured with id:path
        self.constraints = {} #"agent": (x,y) : [time1,time2 ...]
        
        self.graphManager =setupGrid.graphManger(graph)
        self.aStar = aStar.aStar(self.graphManager)

    #In its current state this is more psuedo code than anything else 
    def cbs(self,agents):
        #tree = x
        #first iteration of path finding for all agents
        #   return paths 
        #   check for collisions 
        root = node()
        #run path finding algo for all paths no constraints - should return list of all paths for each robot/task
        currentPaths = self.findPathsForAll([]) 
        currentCollisions = self.collsionsFound(currentPaths)
        root.paths = currentPaths
        root.cost = self.calculateNodeCost(currentPaths)
        #highLevelTree.setInitialNode = node(currentCollisions,self.calculateNodeCost(paths))
        #need check which will break out of function if there's no collisons 
        if len(currentCollisions) ==0:
            #no collisions first time around
            return currentPaths
        openSet = set()
        openSet.add(root)
        while len(openSet) != 0:
            currentNode = self.getMinNode(openSet)
            #get first conflict 
            currentNode.conflicts.pop(0) # assuming for now that conflicts is a list

            


        
        #from the collisons we want to create x new nodes on a tree based on the number of robots in the collison 
        #   can't be more than 4 if robots can only move L R U D - could be 8 if diagonal movements allowed - nawr 

        """
        I'm not sure this is the other loop I want to consider anymore
        currentCollisions = None
        while currentCollisions != None:
        
        I'm gonna ignore the outer loop for the moment and work solely on the inner loop
"""
        #spliting of tree
        parentConstraints = root.constraints
        for agent in currentCollisions.agentsInvolved:
            childNode = node()
            parentConstraints[agent] = currentCollisions
            childNode.constraints = currentCollisions
            #run path finding - only need to run it for at most 4 agents, but only twice if theres only 2 agents involved in the collision
            paths = self.findPathsForAll()
            childNode.cost = self.calculateNodeCost(paths)
            



            #run path finding for everynode with new collisons
            #lowlevel 
            #currentCollisions = self.checkForcollsions(paths)
        print("d")

    def calculateNodeCost(self,paths):
        totalCost = 0
        for agent in paths:
            totalCost += agent.time
        return totalCost - len(paths) # minusing the len(paths) as the path includes end pos and want to not include that in this calculation

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
                        if agent in collisions:
                            if newConstraint not in collisions[agent]: #or newConstraint in collisions[agent]:
                                collisions[agent].append(newConstraint)
                                collisions[agent2].append(newConstraint)
                        else:
                            collisions[agent] = [newConstraint]
                            collisions[agent2] = [newConstraint]
                        #collison detected
                    i += 1
        return collisions
    
    #this will return constraints in order found in
    def AlternativecheckForcollsions(self,paths): #returns the collsions found as a list or dict etc 
        collisions = []
        for agent in paths:
            for agent2 in paths:
                if agent == agent2:
                    continue
                i = 0
                while i < len(paths[agent]) or i < len(paths[agent2]):
                    stepAgentOne = paths[agent][i]
                    stepAgentTwo = paths[agent2][i]
                    if stepAgentOne == stepAgentTwo:
                        newCollision = Collision(stepAgentOne.x,stepAgentOne.y,stepAgentOne.time,[agent,agent2])
                        if newCollision not in collisions:
                            collisions.append(newCollision)
                        #collison detected
                    i += 1
        return collisions

    def findPathsForAll(self,constraints):
        paths = {}
        for agent in self.agents:
            paths[agent] = self.aStar.findPath(constraints,agent)
        return paths