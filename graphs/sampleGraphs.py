from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent


def randomise(upperBound, numbToRandomise):
    startPts = []
    endPts = []



#4x4 no static objects
graph = warehouseFloor(4,4)
graphm = graphManger(graph)

agent1 = agent(1,[0,0],[3,3])
agent2 = agent(2,[3,3], [0,0])
agent3 = agent(3,[0,1], [3,1])




#8X8 no static objects
graph = warehouseFloor(8,8)
graphm = graphManger(graph)




#16x16 no static objects
graph = warehouseFloor(16,16)
graphm = graphManger(graph)


#32x32 no static objects
graph = warehouseFloor(32,32)
graphm = graphManger(graph)

#64x64 no static objects
graph = warehouseFloor(8,8)
graphm = graphManger(graph)
