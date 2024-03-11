

from src.graphPartition.graphPartitionDecider import graphPartitionDecider,graphPartitionDeciderV1,clusterPartition
from src.setupGrid import warehouseFloor
from src.agent import agent


graph = warehouseFloor(11,9)
agent1 = agent(1,[4,3],[5,5])
agent2 = agent(2,[5,3],[4,5])
agent3 = agent(3,[0,4],[10,4])
agent4 = agent(4,[1,8],[6,8])
#a = graphPartitionDeciderV1(graph,[agent1,agent2,agent3])
#a.graphAnalysis(.1,.2)


a = clusterPartition(graph,[agent1,agent2,agent3,agent4])
a.getClusters()