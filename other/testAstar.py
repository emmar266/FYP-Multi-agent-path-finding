import src.aStar as aStar
import src.setupGrid as setupGrid
import src.agent as agent

"""
n1 = aStar.aStarNode(1,2,1)
n2 = aStar.aStarNode(1,2,3)
n3 = aStar.aStarNode(1,2,1)
openSet = set()
openSet.add(n1)
if n2 in openSet:
    print("wRONG")
if n3 in openSet:
    print("Correct")

"""
graph = setupGrid.warehouseFloor(4,4)
graph.setStaticObstacle([[0,1],[0,2],[1,2]])
graphm= setupGrid.graphManger(graph)
agent1 = agent.agent(1,[0,0],[0,3])
current = aStar.aStar(graphm)
path = current.findPath([[2,2,3]],agent1,16)
print("we")


##want to ensure the astar stops 
graph = setupGrid.warehouseFloor(4,4)
graph.setStaticObstacle([[0,0]])
graphm= setupGrid.graphManger(graph)
current = aStar.aStar(graphm)
agent1 = agent.agent(1,[0,0],[0,3])
path = current.findPath([[2,2,3]],agent1,4*4)
print("end")