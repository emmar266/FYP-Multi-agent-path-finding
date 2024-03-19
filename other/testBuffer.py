from src.reservedArea.reservedAreaBuffer import reservedAreaBufferArea
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent


graph = warehouseFloor(16,16)
#graphm= graphManger(graph)
agent1 = agent(1,[0,0],[15,14])
agent2 = agent(2,[15,9],[0,9])
a = reservedAreaBufferArea(graph,[agent1,agent2])
a.test([agent1])
