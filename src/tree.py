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

    

    