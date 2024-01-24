import src.aStar as aStar
import src.setupGrid as setupGrid
import src.agent as agent
import src.cbs.cbs as cbs


graph = setupGrid.warehouseFloor(4,4)
graph.setStaticObstacle([[0,2],[1,2],[2,2]])
graphm= setupGrid.graphManger(graph)
agent1 = agent.agent(1,[0,1],[0,3])
agent2 =  agent.agent(2,[0,3],[0,1])
current = aStar.aStar(graphm)
agent1path = current.findPath([],agent1, 4*4)
agent2path = current.findPath([[3,2,4]],agent2,4*4)
paths = {agent1.agentId:agent1path, agent2.agentId: agent2path}
algo = cbs.highLevel(graph,[agent1,agent2] )
"""
constraints = algo.AlternativecheckForcollsions(paths)
agent1path = current.findPath([[3,2,4]],agent1)
agent2path = current.findPath([],agent2)
constraints = algo.AlternativecheckForcollsions({agent1.agentId:agent1path, agent2.agentId: agent2path})
agent1path = current.findPath([[3,2,4],[3,3,4]],agent1)
agent2path = current.findPath([[3,2,4]],agent2)
constraints = algo.AlternativecheckForcollsions({agent1.agentId:agent1path, agent2.agentId: agent2path})
print("g")
"""

finalpaths = algo.cbs()
collisions = algo.AlternativecheckForcollsions(paths)
print(type(collisions))
print("e")


