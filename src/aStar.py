import copy
from src.pq import PQ

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
        self.areaOfGraph = graph.graph.width * graph.graph.length
        self.getValidNeighbours = graph.findValidNeighbours

    def findPath(self,constraints,agent,previousLongestPath):
        #return path
        startPos = agent.startPos
        nodeCameFrom = {}

        openPQ = PQ()
        openSet = set()
        closedSet = set()

        node = aStarNode(startPos[0],startPos[1],0)
        node.setMovementCost(0)
        node.setTotalCost(self.calculateHeurisitic(agent.goal,node))
        startNode = node

        openPQ.put((node.totalCost, node))
        openSet.add(node)

        currentTime = 0

        while openPQ.qsize() != 0 and currentTime < 2*(previousLongestPath + self.areaOfGraph):
            currentNode = openPQ.get()#need to remove from closed set rn
            openSet.remove(currentNode)


            closedSet.add(currentNode)

            neighbours = self.getValidNeighbours(currentNode,constraints) #of what type is neighbour - should be like a node in the graph
            currentTime = currentNode.time +1
            if currentTime < previousLongestPath:
                #add current node to set
                waitNode = copy.deepcopy(currentNode)
                waitNode.time = currentTime
                if [waitNode.x,waitNode.y,waitNode.time] in constraints:
                    openPQ.put((waitNode.totalCost ,waitNode))
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
                #this should be set
                if neighbourNode in openSet or neighbourNode in closedSet: #this is a flawed statement, neighbour is of type list and 
                    continue
                neighbourNode.movementCost = currentNode.movementCost + self.costPerStep #g = movement cost from start
                neighbourNode.totalCost= self.calculateHeurisitic(agent.goal,currentNode ) + neighbourNode.movementCost  # movementCost + heuristic  f
                #neightbourNode = aStarNode(neighbour[0],neighbour[1],currentTime,totalCost, movementCost)
                openPQ.put((neighbourNode.totalCost,neighbourNode))
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


    def atGoal(self,currentNode,goal):
        if currentNode[0] == goal[0] and currentNode[1] == goal[1]:
            return True
        return False



    def calculateHeurisitic(self,goal,currentNode):
        return abs(currentNode.x - goal[0]) + abs(currentNode.y - goal[1])
