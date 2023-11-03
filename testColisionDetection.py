import aStar
import setupGrid
import agent
import cbs

if set([0,1]) == set([1,0]):
    print("yee")



graph = setupGrid.warehouseFloor(4,4)
graph.setStaticObstacle([[0,2],[1,2],[2,2]])
graphm= setupGrid.graphManger(graph)
agent1 = agent.agent(1,[0,1],[0,3])
agent2 =  agent.agent(2,[0,3],[0,1])
current = aStar.aStar(graphm)
agent1path = current.findPath([],agent1)
agent2path = current.findPath([],agent2)
paths = {agent1.agentId:agent1path, agent2.agentId: agent2path}
algo = cbs.highLevel(graph)
collisions = algo.checkForcollsions(paths)
print("e")


