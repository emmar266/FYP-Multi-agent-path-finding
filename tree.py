class node:
    def __init__(self,constraints,cost) -> None:
        self.constraints = constraints
        self.collisions = []
        self.children = []
        self.cost = cost 
        self.paths = []
    


class Tree:
    def __init__(self,startNode) -> None:
        self.root = startNode 


    def findMinCost():
        #might not need this
        #would be more efficient to keep track of what leaf node to expand next
        pass

    