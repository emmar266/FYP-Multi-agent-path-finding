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
#empty
graph = warehouseFloor(8,8)
graphm = graphManger(graph)


#warehouse like
graph = warehouseFloor(8,8)
graph.setStaticObstacle(
    [
        [0,0],[1,0],[2,0],[6,0],[7,0],
        [0,2],[1,2],[2,2],[6,2],[7,2],
        [0,5],[1,5],[2,5],[6,5],[7,5]
    ]

)
graphm = graphManger(graph)



#longer shelves
graph = warehouseFloor(8,8)
graphm = graphManger(graph)
graph.setStaticObstacle(
    [
        [0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1],
        [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],
        [0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6]

    ]
)




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
