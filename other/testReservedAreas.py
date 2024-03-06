from src.reservedArea.reservedAreasStatic import reservedAreasStatic
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent

##This commented out grpah should produce a result but does not - need to investigate
"""
graph = warehouseFloor(9, 7)
graphm = graphManger(graph)
agent1 = agent(1, [4, 1], [5, 6])
agent2 = agent(2, [0, 1], [6, 6])
agent3 = agent(3, [0, 3], [8, 3])
agents = [agent2,agent3]


obja = reservedAreasStatic(graph, agents)
obja.dynamicPP([agent1])
print("here")"""

graph = warehouseFloor(11, 11)
graphm = graphManger(graph)
agent1 = agent(1, [1,3], [1,9])
agent2 = agent(2, [7,3], [7,9])
agent3 = agent(3, [5,6], [10,6])
agents = [agent1,agent2,agent3]

obja = reservedAreasStatic(graph, agents)
obja.reservedAreaDeciderVersionTwo(2)