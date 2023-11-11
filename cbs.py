from tree import Tree, node
import aStar
import setupGrid
import copy

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
    
class collision:
    def __init__(self,agentOne,agentTwo, conflictOne, conflictTwo) -> None:
        self.agentOne = agentOne
        self.agentTwo = agentTwo
        self.agentOneCollidingPt = conflictOne
        self.agentTwoCollidingPt = conflictTwo

    def __eq__(self, objToCmp) -> bool:
        if self.agentOne == objToCmp.agentTwo and self.agentTwo == objToCmp.agentOne:
            if self.agentOneCollidingPt == objToCmp.agentTwoCollidingPt and self.agentTwoCollidingPt == objToCmp.agentOneCollidingPt:
                return True
        elif self.agentOne == objToCmp.agentTwo and self.agentTwo == objToCmp.agentOne:
            if self.agentOneCollidingPt == objToCmp.agentTwoCollidingPt and self.agentTwoCollidingPt == objToCmp.agentOneCollidingPt:
                return True
        return False
class highLevel:
    def __init__(self,graph,agents):
        self.graphManager =setupGrid.graphManger(graph)
        self.aStar = aStar.aStar(self.graphManager)
        self.agents = agents


    def cbs(self):

        #run path finding algo for all paths no constraints - should return list of all paths for each robot/task
        currentPaths = self.findPathsForAll({}) 
        #currentCollisions = self.collsionsFound(currentPaths)

        root = node({},self.calculateNodeCost(currentPaths))
        root.paths = currentPaths

        #highLevelTree.setInitialNode = node(currentCollisions,self.calculateNodeCost(paths))
        #need check which will break out of function if there's no collisons 
        openSet = set()
        openSet.add(root)

        while len(openSet) != 0:
            currentNode = self.getMinNode(openSet)

            openSet.remove(currentNode)
            #get first conflict 

            #run conflict finder 
            currentCollisions = self.AlternativecheckForcollsions(currentNode.paths) # list of type collision
            #based on this collision we want to construct a conflict
            if len(currentCollisions) ==0:
                #no collisions, Valid paths found for all agents
                return currentNode.paths
            collision = currentCollisions.pop(0) # assuming for now that conflicts is a list

            for i in range(0,2):
                if i == 0:
                    agent = collision.agentOne
                    newConstraint = collision.agentOneCollidingPt
                else:
                    agent = collision.agentTwo
                    newConstraint = collision.agentTwoCollidingPt
                
                constraints = copy.deepcopy(currentNode.constraints)
                if agent.agentId in constraints:
                    constraints[agent.agentId].append(newConstraint)
                else:
                    constraints[agent.agentId] = [newConstraint]
                #run pa th finding - only need to run it for at most 4 agents, but only twice if theres only 2 agents involved in the collision
                paths = self.findPathsForAll(constraints)
                cost = self.calculateNodeCost(paths) 
                childNode = node(constraints, cost)
                childNode.paths = paths
                currentNode.children.append(childNode)
                openSet.add(childNode)


    def getMinNode(self,openSet):
        minCostNode = None
        minNode = None
        for node in openSet:
            if minCostNode == None or node.cost < minCostNode:
                minCostNode = node.cost
                minNode = node  
        return minNode

    def calculateNodeCost(self,paths):
        totalCost = 0
        for agent in paths:
            totalCost += len(paths[agent])
        return totalCost - len(paths) # minusing the len(paths) as the path includes end pos and want to not include that in this calculation

    def checkForCrossingNodes(self,lastAgent1Step,lastAgentTwoStep,currentAgentOneStep,currentAgentTwoStep):
        if lastAgent1Step is not None and lastAgentTwoStep is not None:
            if lastAgent1Step.x == currentAgentTwoStep.x and lastAgent1Step.y == currentAgentTwoStep.y:
                if lastAgentTwoStep.x == currentAgentOneStep.x and lastAgentTwoStep.y == currentAgentOneStep.y:    
                    return True
        return False

    #this will return constraints in order found in
    def AlternativecheckForcollsions(self,paths): #returns the collsions found as a list or dict etc 
        collisions = []
        for agent in paths:
            for agent2 in paths:
                if agent == agent2:
                    continue
                i = 0
                agentsLastPos = None
                agentTwoLastPos = None
                while i < len(paths[agent]) and i < len(paths[agent2]):
                    stepAgentOne = paths[agent][i]
                    stepAgentTwo = paths[agent2][i]
                    if (stepAgentOne == stepAgentTwo):
                        #newCollision = Collision(stepAgentOne.x,stepAgentOne.y,stepAgentOne.time,[agent,agent2])
                        newCollision = collision(agent, agent2,[stepAgentOne.x, stepAgentOne.y, stepAgentOne.time],
                                                 [stepAgentTwo.x,stepAgentTwo.y,stepAgentTwo.time])
                        if newCollision not in collisions:
                            collisions.append(newCollision)
                        #collison detected
                    if  self.checkForCrossingNodes(agentsLastPos, agentTwoLastPos,stepAgentOne ,stepAgentTwo):
                        newCollision = collision(agent,agent2, [agentsLastPos.x,agentsLastPos.y,agentsLastPos.time],[agentTwoLastPos.x,agentTwoLastPos.y,agentTwoLastPos.time])
                        if newCollision not in collisions:
                            collisions.append(newCollision)
                        #because of the way this check is done a duplicate collisions of this type won't be found in further iterations
                    agentsLastPos = stepAgentOne
                    agentTwoLastPos = stepAgentTwo
                    i += 1
        return collisions

    def findPathsForAll(self,constraints):
        paths = {}
        for agent in self.agents:
            if agent.agentId in constraints:
                paths[agent] = self.aStar.findPath(constraints[agent.agentId],agent)
            else:
                paths[agent] = self.aStar.findPath([],agent)
        return paths
    
    """
    #returns collsions per agent
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
        return collisions"""