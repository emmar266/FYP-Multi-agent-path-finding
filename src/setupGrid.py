 
class warehouseFloor:
    def __init__(self,x, y, valueInMatrix=0) -> None:
        self.floorPlan = [[valueInMatrix] * x for _ in range(y)]
        self.width = x
        self.length = y


    def checkValidMovement(self,suggestedMovement):
        if self.floorPlan[suggestedMovement[1]][suggestedMovement[0]] != "Blocked":
            return True
        return False
    

    def setStaticObstacle(self,obstaclesList):
        for obstacle in obstaclesList:
            self.floorPlan[obstacle[1]][obstacle[0]] = "Blocked"


""""""
class graphManger:
    def __init__(self,graph):
        self.graph = graph

    def checkValidMovement(self,suggestedMovement,constraints,time):
        #flaw with constraint check
        if (suggestedMovement[0] >=0 and suggestedMovement[0] < self.graph.width) and (suggestedMovement[1] >=0 and suggestedMovement[1] < self.graph.length):
            val = self.graph.floorPlan[suggestedMovement[1]][suggestedMovement[0]]
            if self.graph.floorPlan[suggestedMovement[1]][suggestedMovement[0]] != "Blocked":
                suggested = [suggestedMovement[0],suggestedMovement[1],time]
                if suggested in constraints:
                        #Idea is to recognise if theres a dynamic block which is passed back to the astar which will either allow waiting at current block
                        return False
                else:
                    return True
        return False
    
    
    def findValidNeighbours(self, currentNode,constraints):
        time = currentNode.time +1
        #should separate into sep functin
        #check up movement
        validNeighbours = []
        validMovement= self.checkValidMovement([currentNode.x, currentNode.y-1],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x, currentNode.y-1])
        #check down movement
        validMovement = self.checkValidMovement([currentNode.x, currentNode.y+1],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x, currentNode.y+1])

        #check left movement
        validMovement = self.checkValidMovement([currentNode.x-1, currentNode.y],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x-1, currentNode.y])

        #check right movement
        validMovement = self.checkValidMovement([currentNode.x+1, currentNode.y],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x+1, currentNode.y])
        return validNeighbours

if __name__ =="__main__":
    w = warehouseFloor(4,4)
    w.setStaticObstacle([[0,3]])
    print(w.checkValidMovement([0,2]))