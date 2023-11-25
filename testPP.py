import aStar
import setupGrid
import agent
import prioritised


graph = setupGrid.warehouseFloor(4,4)
graph.setStaticObstacle([[0,2],[1,2],[2,2]])
graphm= setupGrid.graphManger(graph)
agent1 = agent.agent(1,[0,1],[0,3])
agent2 =  agent.agent(2,[0,3],[0,1])
p = prioritised.prioritisedPlanning(graphm,[agent1,agent2])
val = p.randomisedOrdering()


