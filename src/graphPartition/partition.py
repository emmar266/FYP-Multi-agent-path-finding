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
            self.maxX = subGraphToAdd.topRight
        if self.minY is None or subGraphToAdd.topY < self.minY:
            self.minY = subGraphToAdd.topY
        if self.maxX is None or subGraphToAdd.bottomY > self.maxX:
            self.maxX = subGraphToAdd.bottomY
        self.subGraphs.append(subGraphToAdd)


    #this should only be called once all the subgraphs have been assigned to a partition
    # i.e there should not be a case where once built it needs to be rebuilt
    def buildPartiion(self,originalGraph):
        #need to build the matrix based on the dimensions found
        self.partitionGraph = warehouseFloor((self.maxX- self.minX), (self.maxY - self.minY),"Blocked")

        #in theory i should mark every node in this new graph as blocked and then unblock it as necessary
        for subgraph in self.subGraphs:
            #need to get the current value in reference to the original graph
            for j in range(subgraph.topY, subgraph.bottomY):
                currentYPosOriginal = subgraph.topY +j
                currentYPosCurrent = (subgraph.bottomY - subgraph.topY) + j
                for i in range(subgraph.leftX, subgraph.rightX):
                    #check if the value in the original graph is blocked or not
                    currentXPosOriginal = subgraph.leftX +i
                    currentXPosCurrent = (subgraph.rightX - subgraph.leftX )+i
                    if originalGraph[currentXPosOriginal][currentYPosOriginal] != "Blocked":
                        self.partitionGraph.floorPlan[currentXPosOriginal][currentYPosOriginal] = 0


