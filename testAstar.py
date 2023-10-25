import aStar
import setupGrid
import agent

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
current.findPath([],agent1)
