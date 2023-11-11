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
        #flaw with constraint check
        dynamic= False
        if (suggestedMovement[0] >=0 and suggestedMovement[0] < self.graph.width) and (suggestedMovement[1] >=0 and suggestedMovement[1] < self.graph.length):
            if self.graph.floorPlan[suggestedMovement[1]][suggestedMovement[0]] != "Blocked":
                suggested = [suggestedMovement[0],suggestedMovement[1],time]
                if suggested in constraints:
                        #Idea is to recognise if theres a dynamic block which is passed back to the astar which will either allow waiting at current block
                        dynamic = True
                        return False, dynamic
                else:
                    return True, dynamic
        return False, dynamic
    
    
    def findValidNeighbours(self, currentNode,constraints):
        time = currentNode.time +1
        dynamic = False
        if currentNode.x == 3 and currentNode.y ==3 and currentNode.time ==3:
            print("whlep")
        if currentNode.x == 3 and currentNode.y ==3 and currentNode.time ==3:
            print("whlep")
        #should separate into sep functin
        #check up movement
        validNeighbours = []
        validMovement, dynamicFound = self.checkValidMovement([currentNode.x, currentNode.y-1],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x, currentNode.y-1])
        if dynamicFound:
            dynamic = True
        #check down movement
        validMovement, dynamicFound = self.checkValidMovement([currentNode.x, currentNode.y+1],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x, currentNode.y+1])
        if dynamicFound:
            dynamic = True

        #check left movement
        validMovement, dynamicFound = self.checkValidMovement([currentNode.x-1, currentNode.y],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x-1, currentNode.y])
        if dynamicFound:
            dynamic = True

        #check right movement
        validMovement, dynamicFound = self.checkValidMovement([currentNode.x+1, currentNode.y],constraints,time)
        if validMovement:
            validNeighbours.append([currentNode.x+1, currentNode.y])
        if dynamicFound:
            dynamic = True
        return validNeighbours,dynamic

if __name__ =="__main__":
    w = warehouseFloor(4,4)
    w.setStaticObstacle([[0,3]])
    print(w.checkValidMovement([0,2]))