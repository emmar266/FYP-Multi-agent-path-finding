from src.setupGrid import warehouseFloor


class Partition:
    def __init__(self):
        self.partitionGraph = None
        self.subGraphs = []
        self.originalGraphMatchX =[]
        self.originalGraphMatchY = []
        #This will keep track of
        self.minX= None
        self.minY = None
        self.maxX = None
        self.maxY = None

    def addSubGraph(self, subGraphToAdd):
        #Keep track of the dimension of partition
        if  self.minX is None or subGraphToAdd.leftX < self.minX:
            self.minX = subGraphToAdd.leftX
        if  self.maxX is None or subGraphToAdd.rightX > self.maxX:
            self.maxX = subGraphToAdd.rightX
        if self.minY is None or subGraphToAdd.topY < self.minY:
            self.minY = subGraphToAdd.topY
        if self.maxY is None or subGraphToAdd.bottomY > self.maxY:
            self.maxY = subGraphToAdd.bottomY
        self.subGraphs.append(subGraphToAdd)


    #this should only be called once all the subgraphs have been assigned to a partition
    # i.e there should not be a case where once built it needs to be rebuilt
    def buildPartiion(self,originalGraph):
        #need to build the matrix based on the dimensions found
        self.partitionGraph = warehouseFloor((self.maxX- self.minX), (self.maxY - self.minY),"Blocked")

        #in theory i should mark every node in this new graph as blocked and then unblock it as necessary
        for subgraph in self.subGraphs:
            #need to get the current value in reference to the original graph
            for j in range(subgraph.bottomY - subgraph.topY+1):
                currentYPosOriginal = subgraph.topY + j
                currentYPos = j
                for i in range( subgraph.rightX-subgraph.leftX+1):
                    #check if the value in the original graph is blocked or not
                    currentXPosOriginal = subgraph.leftX +i
                    currentXPos = i
                    if originalGraph.floorPlan[currentYPosOriginal][currentXPosOriginal] != "Blocked":
                        self.partitionGraph.floorPlan[currentYPos][currentXPos] = 0

    #if the step is blocked in the partiiton then it is not part of the partition - it would
    def checkIfInPartition(self,step):
        #check if in min max range
        if self.minX <= step[0] <= self.maxX and self.minY <= step[1] <= self.maxY:
            if self.partitionGraph.floorPlan[step[1]][step[0]] == "Blocked":
                #not in partition
                return False
        return True


    def mergeOldGraph(self,newGraph, oldminX,oldminY,oldmaxX, oldmaxY ):
        indMinX = abs(oldminX - self.minX)
        indMinY = abs(self.minY - oldminY)
        for index,row in self.partitionGraph.floorPlan:
            for index2,item in row:
                newGraph.floorPlan[indMinY][indMinX] == self.partitionGraph.floorPlan[index2][index]
                indMinX+= 1
            indMinY +=1
        return newGraph


    def extendGraph(self, toAdd ):
        #create new subgraph
        oldminX, oldminY, oldmaxX, oldmaxY = self.minX,self.minY, self.maxX, self.maxY
        if toAdd.minX < self.minX:

            self.minX = toAdd.minX
        if toAdd.maxX > self.maxX:
            self.maxX = toAdd.maxX
        if toAdd.minY < self.minY:
            self.minY = toAdd.minY
        if toAdd.maxY > self.maxY:
            self.maxY = toAdd.maxY


        newGraph = warehouseFloor((self.maxX- self.minX), (self.maxY - self.minY),"Blocked")
        newGraph = self.mergeOldGraph(newGraph, oldminX,oldminY,oldmaxX, oldmaxY)
        for path in toAdd.pathsToIncorporate:
            newGraph.floorPlan[self.minY - path[1]][self.minX - path[0]] = 0

        self.partitionGraph = newGraph



