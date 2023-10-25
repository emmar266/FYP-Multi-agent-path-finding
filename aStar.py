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

        #this version of a star must be able to handle constraints 
        #TODO need to keep track of the node before 
    def findPath(self,constraints,agent):
        #return path
        startPos = agent.startPos

        closedSet = set() #in this set items should look like (node,time), (node,time) etc
        openSet = set()
        node = aStarNode(startPos[0],startPos[1],0)
        node.setMovementCost(0)
        node.setTotalCost(self.calculateHeurisitic(agent.goal,node))

        openSet.add(node) 

        while len(openSet) != 0:
            currentNode = self.getLeastCost(openSet)#need to remove from closed set rn
            openSet.remove(currentNode)

            closedSet.add(currentNode)


            neighbours = self.getValidNeighbours(currentNode,constraints) #of what type is neighbour - should be like a node in the graph
            currentTime = currentNode.time +1
            for neighbour in neighbours:
                neighbourNode = aStarNode(neighbour[0],neighbour[1],currentTime)
                if self.atGoal(neighbour,agent.goal):
                    #stop search and return path
                    return
                if neighbourNode in openSet or neighbourNode in closedSet: #this is a flawed statement, neighbour is of type list and 
                    continue
                neighbourNode.movementCost = currentNode.movementCost + self.costPerStep #g = movement cost from start
                neighbourNode.totalCost= self.calculateHeurisitic(agent.goal,currentNode ) + neighbourNode.movementCost  # movementCost + heuristic  f
                #neightbourNode = aStarNode(neighbour[0],neighbour[1],currentTime,totalCost, movementCost)
                openSet.add(neighbourNode)
                #need to keep track of path - not sure if that should be done per node or not?

        return False #path does not exist
    
    def checkIfEquivalentNodeInSet(self,openSet,checkNode):
        for node in openSet:
            if node == checkNode:
                return True
        return False

    def atGoal(self,currentNode,goal):
        if currentNode[1] == goal[0] and currentNode[0] == goal[1]:
            return True
        return False

    def getLeastCost(self,openSet):
        minTotalCost = None
        minNode = None
        for node in openSet:
            if minTotalCost == None or node.totalCost < minTotalCost:
                minTotalCost = node.totalCost
                minNode = node    
        return minNode
    

    def calculateHeurisitic(self,goal,currentNode):
        return abs(currentNode.x - goal[0]) + abs(currentNode.y - goal[1])

"""
    #will also need to add the manual check of two agents swapping squares - not allowed 
    def getValidNeighbouringNodes(self,currentNode,constraints):
        #Constraints should look like (x,y,time)
        #constraints here will be the ones for the particular agent so won't have to check that
        time = currentNode.time +1


        #CheckUp
        upCoords = (currentNode.x,currentNode.y-1)
        if currentNode.y-1 >=0 

        return """""