from src.graphPartition.graphPartitionDecider.deciderV2 import graphPartitionDeciderV2
from src.graphPartition.graphPartitionDecider.deciderV1 import graphPartitionDeciderV1
from src.setupGrid import warehouseFloor
from src.agent import agent
from src.graphPartition.graphPartition import graphPartition

"""
graph = warehouseFloor(11,9)
agent1 = agent(1,[4,3],[5,5])
agent2 = agent(2,[5,3],[4,5])
agent3 = agent(3,[0,4],[10,4])
agent4 = agent(4,[1,8],[6,8])

graph = warehouseFloor(8,12)
agent1 = agent(1,[2,6],[5,7])
agent2 = agent(2,[3,5],[3,8])
agent3 = agent(3,[4,8],[3,0])
"""
graph = warehouseFloor(16,18)
agent1 = agent(1,[4,4],[1,0])
agent2 = agent(2,[4,5],[4,0])
agent3 = agent(3,[5,2],[0,2])
agent4 = agent(4,[11,17],[11,13])
agent5 = agent(5,[13,15],[9,15])
agent6 = agent(6,[10,17],[13,13])
a = graphPartition()
a.getPartitionsV2([agent1,agent2,agent3,agent4,agent5,agent6], graph,0.05,1)
a = graphPartitionDeciderV1(graph,[agent1,agent2,agent3,agent4,agent5,agent6])
a.graphAnalysis(.03,2)
#a.partitonV2(.1,2)


#a = clusterPartition(graph,[agent1,agent2,agent3,agent4])
#a.getClusters()