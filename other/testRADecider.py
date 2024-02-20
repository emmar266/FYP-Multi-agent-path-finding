from src.reservedArea.reservedAreas import reservedAreasStatic
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent
from src.reservedArea.reservedAgentsDecider import reservedAgentDecider


graph = warehouseFloor(7, 8)
graph.setStaticObstacle([[0,3],[1,3],[2,3],[3,3]])
graphm = graphManger(graph)
agent1 = agent(1, [2,2], [4,7])
agent2 = agent(2, [0,5], [5,5])
agents = [agent1,agent2]
a = reservedAgentDecider(graph, agents)
a.attemptTwo()

