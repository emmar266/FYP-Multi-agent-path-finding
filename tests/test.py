from src.aStar import  aStar
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent
from src.cbs.cbs import highLevel

graphDict = {}
graphDict["graphEndPosBlocking"] = warehouseFloor(9,7)
graphDict["graphEndPosBlocking"].setStaticObstacle([
    [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]
    ,[6,1],[7,1],[8,1]
    ,[0,2],[1,2],[2,2],[3,2],[4,2],[6,2],[7,2],[8,2]

    ,[0,4],[1,4],[2,4],[3,4],[4,4],[6,4],[7,4],[8,4]
    ,[4,5],[6,5]
    ,[4,6],[7,6]
])

agentDict = {}
agent1 = agent(1, [4, 1], [5, 6])
agent2 = agent(2, [0, 1], [6, 6])
agent3 = agent(3, [0, 3], [6, 3])

agentDict["graphEndPosBlocking"] = [agent1, agent2, agent3]

a = graphManger(graphDict["graphEndPosBlocking"])
aStar(a).findPath([],agent1,9)

print("aaaaaa")
"""
a = highLevel(graphDict["graphEndPosBlocking"],[agent1,agent2,agent3])
b = a.cbs()
print("yee")"""

