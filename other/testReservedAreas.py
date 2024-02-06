from src.reservedArea.reservedAreas import reservedAreasStatic
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent

graph = warehouseFloor(9, 7)
graphm = graphManger(graph)
agent1 = agent(1, [4, 1], [5, 6])
agent2 = agent(2, [0, 1], [6, 6])
agent3 = agent(3, [0, 3], [8, 3])
agents = [agent2,agent3]

obja = reservedAreasStatic(graph, agents)
obja.dynamicPP([agent1])
print("here")