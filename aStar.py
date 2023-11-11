import copy
class aStarNode:
    def __init__(self,x,y,time) -> None:
        self.x = x
        self.y = y
        self.time = time
        self.totalCost = None
        self.movementCost = None

    def setTotalCost(self,totalCost):
        self.totalCost = totalCost

    def setMovementCost(self,movementCost):
        self.movementCost = movementCost

    def __eq__(self, equivalentObj) -> bool:
        if self.x == equivalentObj.x and self.y == equivalentObj.y and self.time == equivalentObj.time:
            return True
        return False
    
    def __hash__(self) -> int:
        return hash((self.x,self.y,self.time))

class aStar:
    def __init__(self, graph) -> None:
        self.costPerStep = 1
        self.getValidNeighbours = graph.findValidNeighbours

    def findPath(self,constraints,agent):
        #return path
        startPos = agent.startPos
        nodeCameFrom = {}
        closedSet = set() #in this set items should look like (node,time), (node,time) etc
        openSet = set()
        node = aStarNode(startPos[0],startPos[1],0)
        node.setMovementCost(0)
        node.setTotalCost(self.calculateHeurisitic(agent.goal,node))
        startNode = node
        openSet.add(node) 

        while len(openSet) != 0:
            currentNode = self.getLeastCost(openSet)#need to remove from closed set rn
            openSet.remove(currentNode)
            closedSet.add(currentNode)
            neighbours,dynamic = self.getValidNeighbours(currentNode,constraints) #of what type is neighbour - should be like a node in the graph
            currentTime = currentNode.time +1
            if dynamic:
                #add current node to set
                waitNode = copy.deepcopy(currentNode)
                waitNode.time = currentTime
                #
                if [waitNode.x,waitNode.y,waitNode.time] in constraints:
                    openSet.add(waitNode)
                    nodeCameFrom[waitNode] = currentNode
            for neighbour in neighbours:
                neighbourNode = aStarNode(neighbour[0],neighbour[1],currentTime)
                if self.atGoal(neighbour,agent.goal):
                    #stop search and return path
                    path = self.buildPath(nodeCameFrom,currentNode,startNode)
                    destNode = aStarNode(agent.goal[0],agent.goal[1],currentTime)
                    destNode.movementCost = currentNode.movementCost + self.costPerStep
                    destNode.totalCost = self.calculateHeurisitic(agent.goal,currentNode ) + destNode.movementCost
                    path.append(destNode)
                    return path
                if neighbourNode in openSet or neighbourNode in closedSet: #this is a flawed statement, neighbour is of type list and 
                    continue
                neighbourNode.movementCost = currentNode.movementCost + self.costPerStep #g = movement cost from start
                neighbourNode.totalCost= self.calculateHeurisitic(agent.goal,currentNode ) + neighbourNode.movementCost  # movementCost + heuristic  f
                #neightbourNode = aStarNode(neighbour[0],neighbour[1],currentTime,totalCost, movementCost)
                openSet.add(neighbourNode)
                if neighbourNode not in nodeCameFrom:
                    nodeCameFrom[neighbourNode] = currentNode
                #need to keep track of path - not sure if that should be done per node or not?
        return False #path does not exist
    
    def buildPath(self, cameFrom,current,startPos):
        path = []
        path.append(current)
        while startPos not in path:
            current = cameFrom[current]
            path.append(current)
        path.reverse()    
        return path

    
    def checkIfEquivalentNodeInSet(self,openSet,checkNode):
        for node in openSet:
            if node == checkNode:
                return True
        return False

    def atGoal(self,currentNode,goal):
        if currentNode[0] == goal[0] and currentNode[1] == goal[1]:
            return True
        return False

    def getLeastCost(self,openSet):
        minTotalCost = None
        minNode = None
        for node in openSet:
            if minTotalCost == None or node.totalCost + node.time < minTotalCost: # need to reval whether time here is relevant in this if
                minTotalCost = node.totalCost + node.time
                minNode = node  
        return minNode


    def calculateHeurisitic(self,goal,currentNode):
        return abs(currentNode.x - goal[0]) + abs(currentNode.y - goal[1])
