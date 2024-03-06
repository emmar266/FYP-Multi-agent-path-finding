from src.reservedArea.reservedAreasStatic import reservedAreasStatic
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent
from src.reservedArea.reservedAgentsDecider import reservedAgentDecider

"""
graph = warehouseFloor(7, 8)
graph.setStaticObstacle([[0,3],[1,3],[2,3],[3,3]])
graphm = graphManger(graph)
agent1 = agent(1, [2,2], [4,7])
agent2 = agent(2, [0,5], [5,5])
agents = [agent1,agent2]
a = reservedAgentDecider(graph, agents)
a.attemptTwo(1)
"""


graph = warehouseFloor(11, 11)
graphm = graphManger(graph)
agent1 = agent(1, [1,3], [1,9])
agent2 = agent(2, [7,3], [7,9])
agent3 = agent(3, [5,6], [10,6])
agents = [agent1,agent2,agent3]
a = reservedAgentDecider(graph, agents)
a.attemptTwo(2)



