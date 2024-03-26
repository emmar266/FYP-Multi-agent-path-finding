from src.tree import node
import src.aStar as aStar
import src.setupGrid as setupGrid
from src.pq import PQ
import copy

"""
ToDo:
When generating paths for all agents should have some sort of way to reuse paths with no new constraints applied
Change openSet datastructure more heap based - set in python uses hashtable

 
"""


class collision:
    def __init__(self, agentOne, agentTwo, conflictOne, conflictTwo, delayAstar=0, extendAgent=None):
        self.agentOne = agentOne
        self.agentTwo = agentTwo
        self.agentOneCollidingPt = conflictOne
        self.agentTwoCollidingPt = conflictTwo
        self.delayAstar = delayAstar
        self.agentToExtend = extendAgent

    def __eq__(self, objToCmp) -> bool:
        if self.agentOne == objToCmp.agentTwo and self.agentTwo == objToCmp.agentOne:
            if self.agentOneCollidingPt == objToCmp.agentTwoCollidingPt and self.agentTwoCollidingPt == objToCmp.agentOneCollidingPt:
                return True
        elif self.agentOne == objToCmp.agentTwo and self.agentTwo == objToCmp.agentOne:
            if self.agentOneCollidingPt == objToCmp.agentTwoCollidingPt and self.agentTwoCollidingPt == objToCmp.agentOneCollidingPt:
                return True
        return False


class ConstraintsStructure:
    def __init__(self, agentId, constraints=[], delayAstar=0):
        self.agentId = agentId
        self.constraints = constraints
        self.delayAstar = delayAstar

    def addConstraint(self, constraint, delayAstar):
        self.constraints.append(constraint)
        if delayAstar > self.delayAstar:
            self.delayAstar = delayAstar

    def __eq__(self, other):
        if self.constraints == other.constraints and self.agentId == other.agentId:
            return True
        return False


class highLevel:
    def __init__(self, graph, agents):
        self.graphManager = setupGrid.graphManger(graph)
        self.aStar = aStar.aStar(self.graphManager)
        self.agents = agents

    def cbs(self, initialConstraints={}):

        # run path finding algo for all paths no constraints - should return list of all paths for each robot/task
        currentPaths = self.findPathsForAll({})
        # currentCollisions = self.collsionsFound(currentPaths)

        root = node(initialConstraints, self.calculateNodeCost(currentPaths))
        root.paths = currentPaths

        # highLevelTree.setInitialNode = node(currentCollisions,self.calculateNodeCost(paths))
        # need check which will break out of function if there's no collisons
        openPQ = PQ()
        openPQ.put((root.cost, root))

        while openPQ.qsize() != 0:
            currentNode = openPQ.get()

            # get first conflict

            # run collision finder
            currentCollisions = self.checkForcollsions(currentNode.paths)
            if len(currentCollisions) == 0:
                # no collisions, Valid paths found for all agents
                return currentNode.paths
            collision = currentCollisions.pop(0)  # assuming for now that conflicts is a list

            for i in range(0, 2):
                delayEnd = 0
                if i == 0:
                    agent = collision.agentOne
                    newConstraint = collision.agentOneCollidingPt
                    if collision.delayAstar != 0 and collision.agentToExtend =="agentOne":
                        delayEnd = collision.delayAstar
                else:
                    agent = collision.agentTwo
                    newConstraint = collision.agentTwoCollidingPt
                    if collision.delayAstar != 0 and collision.agentToExtend =="agentTwo":
                        delayEnd = collision.delayAstar

                constraints = copy.deepcopy(currentNode.constraints)
                if agent.agentId in constraints:
                    constraints[agent.agentId].addConstraint(newConstraint,delayEnd )
                else:
                    new = ConstraintsStructure(agent.agentId, [newConstraint],delayEnd)
                    constraints[agent.agentId] = new #[newConstraint]
                # run path finding - only need to run it for at most 4 agents, but only twice if theres only 2 agents involved in the collision
                paths = self.findPathsForAll(constraints)
                if type(paths) == bool:
                    continue
                cost = self.calculateNodeCost(paths)
                childNode = node(constraints, cost)
                childNode.paths = paths
                if currentNode.left is None:
                    currentNode.setLeftChild(childNode)
                else:
                    currentNode.setLeftChild(childNode)
                # currentNode.children.append(childNode)
                openPQ.put((childNode.cost, childNode))
        return False

    def printPaths(self, paths, appliedConstraints):
        for agent in paths:
            for currentPt in paths[agent]:
                print("[", currentPt.x, currentPt.y, currentPt.time, "]", end=",")
            print(" ")
        print("Applied constraints")
        for constraint in appliedConstraints:
            print(constraint, end=",")

    def calculateNodeCost(self, paths):
        totalCost = 0
        for agent in paths:
            totalCost += len(paths[agent])
        return totalCost - len(
            paths)  # minusing the len(paths) as the path includes end pos and want to not include that in this calculation

    def checkForCrossingNodes(self, lastAgent1Step, lastAgentTwoStep, currentAgentOneStep, currentAgentTwoStep):
        if lastAgent1Step is not None and lastAgentTwoStep is not None:
            if lastAgent1Step.x == currentAgentTwoStep.x and lastAgent1Step.y == currentAgentTwoStep.y:
                if lastAgentTwoStep.x == currentAgentOneStep.x and lastAgentTwoStep.y == currentAgentOneStep.y:
                    return True
        return False

    # this will return constraints in order found in
    def checkForcollsions(self, paths):  # returns the collsions found as a list or dict etc
        collisions = []
        for agent in paths:
            for agent2 in paths:
                if agent == agent2:
                    continue
                i = 0
                blockingCol = None
                agentsLastPos = None
                agentTwoLastPos = None
                while i < len(paths[agent]) or i < len(paths[agent2]):
                    if i > len(paths[agent]) - 1:
                        stepAgentOne = agentsLastPos
                        stepAgentOne.time += 1
                        stepAgentTwo = paths[agent2][i]
                        blockingCol = "agentOne"
                    elif i > len(paths[agent2]) - 1:
                        stepAgentTwo = agentTwoLastPos
                        stepAgentTwo.time += 1
                        stepAgentOne = paths[agent][i]
                        blockingCol = "agentTwo"
                    else:
                        stepAgentOne = paths[agent][i]
                        stepAgentTwo = paths[agent2][i]

                    # Collison Type: Agents in square at the same time
                    if (stepAgentOne == stepAgentTwo) or self.checkForCrossingNodes(agentsLastPos, agentTwoLastPos,
                                                                                    stepAgentOne, stepAgentTwo):
                        if blockingCol is not None:
                            newCollision = collision(agent, agent2,
                                                     [stepAgentOne.x, stepAgentOne.y, stepAgentOne.time],
                                                     [stepAgentTwo.x, stepAgentTwo.y, stepAgentTwo.time],
                                                     stepAgentOne.time, blockingCol)

                        else:
                            newCollision = collision(agent, agent2, [stepAgentOne.x, stepAgentOne.y, stepAgentOne.time],
                                                     [stepAgentTwo.x, stepAgentTwo.y, stepAgentTwo.time])

                        if newCollision not in collisions:  # need to check catching duplicates
                            collisions.append(newCollision)
                    agentsLastPos = stepAgentOne
                    agentTwoLastPos = stepAgentTwo
                    i += 1
        return collisions

    # need to some check for valid paths
    # need some way to pass in whether its a blocking collision or not
    def findPathsForAll(self, constraints):
        paths = {}
        previousLongestPath = 0
        for agent in self.agents:
            if agent.agentId in constraints:
                a = constraints[agent.agentId]
                paths[agent] = self.aStar.findPath(constraints[agent.agentId].constraints, agent, previousLongestPath,constraints[agent.agentId].delayAstar )

            else:
                paths[agent] = self.aStar.findPath([], agent, previousLongestPath)
            if paths[agent] is False:
                return False
            elif len(paths[agent]) > previousLongestPath:
                previousLongestPath = len(paths)
        return paths
