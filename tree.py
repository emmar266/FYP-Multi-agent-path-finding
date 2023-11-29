class node:
    def __init__(self,constraints,cost) -> None:
        self.left = None
        self.right = None
        self.constraints = constraints
        self.cost = cost 
        self.paths = []

    def setCost(self,cost):
        self.cost = cost
    
    def setLeftChild(self,childNode):
        self.left = childNode

    def setRightChild(self,childNode):
        self.right = childNode

    


class Tree:
    def __init__(self,startNode) -> None:
        self.root = startNode 


    def findMinCost():
        #might not need this
        #would be more efficient to keep track of what leaf node to expand next
        pass

    