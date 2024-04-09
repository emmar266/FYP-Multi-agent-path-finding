import src.aStar as aStar
import src.setupGrid as setupGrid
import src.agent as agent
import src.pp.prioritised as prioritised
import src.cbs.cbs as cbs

graph = setupGrid.warehouseFloor(8,8)

graphm= setupGrid.graphManger(graph)

agent1 = agent.agent(1,[7,6],[3,7])
agent2 =  agent.agent(2,[0,6],[4,7])
agent3 =  agent.agent(3,[0,7],[0,1])
p = prioritised.prioritisedPlanning(graphm,[agent1,agent2,agent3])
val = p.randomisedOrdering()
cb = cbs.highLevel(graph, [agent1,agent2,agent3])
val2 =cb.cbs()

graph = setupGrid.warehouseFloor(8,8)
graph.setStaticObstacle([
    [0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5],
[0,6],[1,6],[2,6],[3,6],[4,6],[5,6],[6,6],
])
graphm= setupGrid.graphManger(graph)
agent1 = agent.agent(1,[0,4],[0,7])
agent2 =  agent.agent(2,[0,7],[0,4])
p = prioritised.prioritisedPlanning(graphm,[agent1,agent2])
val = p.randomisedOrdering()
cb = cbs.highLevel(graph, [agent1,agent2])
val2 =cb.cbs()
print("v")



