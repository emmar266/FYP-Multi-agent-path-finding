import numpy as np
 
class warehouseFloor:
    def __init__(self,warehouseLenght, warehouseWidth) -> None:
        self.floorPlan = [[0] * warehouseLenght for _ in range(warehouseWidth)]
        self.width = warehouseWidth
        self.length = warehouseLenght


    def checkValidMovement(self,suggestedMovement):
        if self.floorPlan[suggestedMovement[0]][suggestedMovement[1]] != "Blocked":
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
        
        if (suggestedMovement[0] >=0 and suggestedMovement[0] < self.graph.width) and (suggestedMovement[1] >=0 and suggestedMovement[1] < self.graph.length):
            if self.graph.floorPlan[suggestedMovement[1]][suggestedMovement[0]] != "Blocked":
                if tuple(suggestedMovement) in constraints:
                    if time in constraints[tuple(suggestedMovement)]:
                        return False
                    return True
                else:
                    return True
        return False
    
    
    def findValidNeighbours(self, currentNode,constraints):
        time = currentNode.time +1

        #should separate into sep functin
        #check up movement
        validNeighbours = []
        if self.checkValidMovement([currentNode.x, currentNode.y-1],constraints,time):
            validNeighbours.append([currentNode.x, currentNode.y-1])

        #check down movement
        if self.checkValidMovement([currentNode.x, currentNode.y+1],constraints,time):
            validNeighbours.append([currentNode.x, currentNode.y+1])

        #check left movement
        if self.checkValidMovement([currentNode.x-1, currentNode.y],constraints,time):
            validNeighbours.append([currentNode.x-1, currentNode.y])

        #check right movement
        if self.checkValidMovement([currentNode.x+1, currentNode.y],constraints,time):
            validNeighbours.append([currentNode.x+1, currentNode.y])
        return validNeighbours

if __name__ =="__main__":
    w = warehouseFloor(4,4)
    w.setStaticObstacle([[0,3]])
    print(w.checkValidMovement([0,2]))