from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent
from Experiments.RAExperiments import ReservedAreasExperiments
from Experiments.GraphPartitionExperiments import GraphPartitionExperiments
import copy
import sys

graph = warehouseFloor(16, 16)
graphm = graphManger(graph)
# 5 agents
print("######################################################")
print("Blank 16x16 4 agents")
agent1 = agent(1, [0, 0], [15, 9])  # purple
agent2 = agent(2, [15, 5], [0, 1])  # magenta
agent3 = agent(3, [11, 1], [6, 15])  # blue
agent4 = agent(4, [15, 8], [0, 9])  # green
# agent5 = agent(5, [0,14],[7,12]) #red
agents1 = [agent1, agent2, agent3]
v1 = ReservedAreasExperiments()
g1 = GraphPartitionExperiments()

try:
    tempGraph = copy.deepcopy(graph)
    print("time", v1.classicCBS(agents1,tempGraph))
    print("V1 pop 2 buf 1-----------------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("V2 pop 2 buf 1-----------------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
except Exception as e:
    print(e)
sys.stdout.flush()
print("######################################################")


#10
agent1 = agent(1,[0,0],[15,9]) # purple
agent2 = agent(2,[15,5],[0,1]) # magenta
agent3 = agent(3, [11,1],[6,15])#blue
agent4 = agent(4, [15,8],[0,9])# green
#agent5 = agent(5, [0,14],[7,12]) #red
agent6 = agent(6,[7,0],(14,13))#light purple
agent7 = agent(7,[0,2],[14,1])#black
agent8 = agent(8,[7,7],[3,3])# pink
agent9 = agent(9, [1,7],[4,8])#pastel green
#agent10 = agent(10, [3,12],[11,14])#orange
agents2 = [agent1,agent2,agent3, agent6, agent7]
print("######################################################")
print("Blank 16x16 5 agents")

try:
    tempGraph = copy.deepcopy(graph)
    print("Time",v1.classicCBS(agents2,tempGraph))
    print("V1 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV1(tempAgents,graph,1,1 ))
    print("V2 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
except Exception as e:
    print(e)
print("######################################################")
sys.stdout.flush()


#15 agents
agent1 = agent(1,[0,0],[15,9]) # purple
agent2 = agent(2,[15,5],[0,1]) # magenta
agent3 = agent(3, [11,1],[6,15])#blue
agent4 = agent(4, [15,8],[0,9])# green
#agent5 = agent(5, [0,14],[7,12]) #red
agent6 = agent(6,[7,0],(14,13))#light purple
agent7 = agent(7,[0,2],[14,1])#black
agent8 = agent(8,[7,7],[3,3])# pink
agent9 = agent(9, [1,7],[4,8])#pastel green
#agent10 = agent(10, [3,12],[11,14])#orange
#ignore light green
agent11 = agent(11, [4,0],[12,6])#brown
agent12 = agent(12, [7,9],[5,2])#light blue
agent13 = agent(13,[0,5], [2,15])#dark green
agent14 = agent(14,[15,12],[4,15])#grey
#agent15 = agent(15, [4,10], [15,7])#yellow
agents3 = [agent1,agent2,agent3, agent6, agent7,agent8, agent9,agent11]
print("Blank 16x16 8 agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("V1 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 - pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 - pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")
sys.stdout.flush()
agents3 = [agent1,agent2,agent3, agent6, agent7,agent8, agent9,agent11,agent12,agent13]
"""
print("######################################################")
print("Blank 16x16 10 agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("V1 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 -pop 2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 pop 2- buf2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")
"""
#16x16 40%
graph = warehouseFloor(16,16)
graphm = graphManger(graph)
graph.setStaticObstacle(
    [
        [11,0],[12,0],[13,0],[14,0],
        [12,1],
        [0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],[12,2],[13,2],[14,2],
        [13,4],[14,4],[15,4],
        [0,5],[1,5],[2,5],[5,5],[6,5],[7,5],[8,5],[9,5],[14,5],[15,5],
        [0,6],[2,6],[5,6],[6,6],[7,6],[8,6],[9,6],[11,6],[12,6],[14,6],[15,6],
        [2,7],[11,7],[12,7],[14,7],[15,7],
        [2,8],[3,8],[4,8],[6,8],[7,8],[8,8],[9,8],[10,8],[11,8],[12,8],[14,8],[15,8],

        [0,10],[1,10],[2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],[9,10],[13,10],[14,10],[15,10],
        [13,11],
        [0,12],[1,12],[2,12],[3,12],[8,12],[9,12],[10,12],[11,12],
        [2,13],[3,13],[6,13],[7,13],[8,13],[9,13],[10,13],[11,13],[14,13],[15,13],
        [0,14],[1,14],[13,14],[14,14],[15,14],
        [0,15],[11,15],[12,15],[13,15],[14,15],[15,15]
        ])

#5 agents
agent1 = agent(1,[0,0],[13,1])#magenta
agent2 = agent(2,[15,9],[0,1])#yellow
agent3 = agent(3,[1,15],[0,3])#red
agent4= agent(4,[3,7],[10,7])#orange
#agent5 = agent(5,[1,6],[10,15])#orangeRed
agents1 = [agent1,agent2,agent3]
print("######################################################")
print("16x16 40% 3agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents1,graph))
    print("V1 buf 1 pop 2---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("V2 buf 1 pop 2---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))

except Exception as e:
    print(e)
sys.stdout.flush()
print("######################################################")
#10 agents
agent1 = agent(1,[0,0],[13,1])#magenta
agent2 = agent(2,[15,9],[0,1])#yellow
agent3 = agent(3,[1,15],[0,3])#red
agent4= agent(4,[3,7],[10,7])#orange
#agent5 = agent(5,[1,6],[10,15])#orangeRed
agent6 = agent(6, [6,0],[6,3])#dark green
agent7 = agent(7,[15,11],[15,0]) #light green
agent8 = agent(8,[13,8],[0,7])#light blue
agent9= agent(9, [12,11], [4,15])#green
#agent10 = agent(10, [8,15],[0,11])#yellow
agents2 = [agent1,agent2,agent3,agent8, agent9]
print("######################################################")
print("16x16 40% 5agents")
try:
    tempGraph = copy.deepcopy(graph)
    print("Time",v1.classicCBS(agents2,tempGraph))
    print(" V1 pop2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("V2 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
    print("---------------------------------")
except Exception as e:
    print(e)

print("######################################################")
sys.stdout.flush()
"""
#15 agents
agent1 = agent(1,[0,0],[13,1])#magenta
agent2 = agent(2,[15,9],[0,1])#yellow
agent3 = agent(3,[1,15],[0,3])#red
agent4= agent(4,[3,7],[10,7])#orange
#agent5 = agent(5,[1,6],[10,15])#orangeRed
agent6 = agent(6, [6,0],[6,3])#dark green
agent7 = agent(7,[15,11],[15,0]) #light green
agent8 = agent(8,[13,8],[0,7])#light blue
agent9= agent(9, [12,11], [4,15])#green
#agent10 = agent(10, [8,15],[0,11])#yellow
agent11 = agent(11, [6,15],[9,0])#dark blue
agent12 = agent(12, [3,15],[7,12])#blue
agent13 = agent(13,[0,9],[0,4])#bluepurple
agent14 = agent(14,[12,14],[2,14])#purple
#agent15 = agent(15,[2,0],[10,0])#black
agents3 = [agent1,agent2,agent3,agent8, agent9,agent11,agent12,agent13]

print("######################################################")
print("16x16 40% 8agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v1 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 pop 2 buff 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")
sys.stdout.flush()
agents3 = [agent1,agent2,agent3,agent8, agent9,agent11,agent12,agent13, agent14, agent6]

print("######################################################")
print("16x16 40% 10agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop 2 buf 1 ---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v1 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 pop2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")
sys.stdout.flush()
#60% 16x16
graph = warehouseFloor(16,16)
graphm = graphManger(graph)
graph.setStaticObstacle(
    [
        [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0], [10,0],[11,0],[12,0],[13,0],[14,0],[15,0],
        [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1],[9,1],[10,1],[11,1],[12,1],[13,1],[14,1],[15,1],
        [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2],[9,2],[10,2],[11,2],[12,2],[13,2],[14,2],[15,2],
        [0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3],[10,3],[11,3],[12,3],[13,3],[14,3],[15,3],

        [0, 6], [1, 6], [2, 6], [3, 6], [4, 6], [5, 6],[8,6], [9,6],[10,6],[11,6],[12,6],[13,6],[14,6],[15,6],
        [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7],[8,7],[9,7],[10,7],[11,7],[12,7],[13,7],[14,7],[15,7],
        [14,8],[15,8],
        [4,9],[5,9],[6,9],[7,9],[8,9],[9,9],[10,9],[14,9],[15,9],
        [2,10],[3,10],[4,10],[5,10],[6,10],[7,10],[8,10],[9,10],[10,10],[11,10],[14,10],[15,10],
        [2,11],[3,11],[4,11],[5,11],[6,11],[7,11],[8,11],[9,11],[10,11],[11,11],[14,11],[15,11],
        [2,12],[3,12],[4,12],[5,12],[6,12],[7,12],[8,12],[9,12],[10,12],[11,12],
        [13,13],[14,13],[15,13],
        [2,14],[3,14],[4,14],[5,14],[6,14],[13,14],[14,14],[15,14],
        [2,15],[3,15],[4,15],[5,15],[6,15],[9,15],[10,15],[11,15],[12,15],[13,15],[14,15],[15,15]
    ]
)


#5 agents
agent1 = agent(1,[15,12],[8,0])#magenta
agent2 = agent(2, [7,3],[12,14]) #red
agent3 = agent(3, [0,4],[9,3])#blue
agent4= agent(4,[3,9],[15,4])#pink
#agent5 = agent(5,[7,15],[0,15])#light green
agents1 = [agent1,agent2,agent3,]
print("######################################################")
print("16x16 60% 4agents")
try:
    tempGraph = copy.deepcopy(graph)

    print(v1.classicCBS(agents1,graph))
    print("v1 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
except Exception as e:
    print(e)
print("#######################################################")
sys.stdout.flush()
#10 agents
agent1 = agent(1,[15,12],[8,0])#magenta
agent2 = agent(2, [7,3],[12,14]) #red
agent3 = agent(3, [0,4],[9,3])#blue
agent4= agent(4,[3,9],[15,4])#pink

#agent5 = agent(5,[7,15],[0,15])#light green
agent6 = agent(6, [9,0],[0,8])#slimegreen
agent7 = agent(7, [13,8],[11,5])#peach
agent8 = agent(8, [ 8,15],[11,9])#purple
agent9 = agent(9, [13,10],[1,15])#dark green
#agent10 = agent(10,[6,6],[12,14])# orangeRed
agents2 = [agent1,agent2,agent3, agent7,agent8]
print("######################################################")
print("16x16 60% 8agents")
try:
    tempGraph = copy.deepcopy(graph)
    print("Time",v1.classicCBS(agents2,tempGraph))
    print("v1 pop2 buf 1 ---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
except Exception as e:
    print(e)
print("######################################################")

sys.stdout.flush()
#15 agents
agent11 = agent(11,[4,4],[0,5])#pastel yellow
agent12 = agent(12,[13,5],[7,8] )#light blue
agent13 = agent(13,[0,13],[2,9])#pink peach
agent14 = agent(14, [11,14],[2,13])#orange
#agent15 = agent(15, [ 15,5],[7,4])#black
agents3 = [agent1,agent2,agent3, agent6, agent7,agent8, agent9,agent11]
print("######################################################")
print("16x16 60% 12agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop 2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop 2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 - pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")
sys.stdout.flush()
"""
#32x32 blank
graph = warehouseFloor(32,32)
graphm = graphManger(graph)

#inital
agent1 = agent(1,[0,0],[14,7])
agent2 = agent(2, [0,7],[18,0])
agent3= agent(3,[6,8],[1,23])
agent4 = agent(4, [24,14],[1,28])
agent5 = agent(5, [26,26],[12,12])
agent6 = agent(6,[27,1],[16,30])
agent7 = agent(7,[8,20],[26,20])
agent8 = agent(8,[8,1],[29,7])
agent9 = agent(9, [31,0], [31,31])
agent10 = agent(10, [18,10], [31,12])
agent11 = agent(11,[16,22], [10,15])
agent12 = agent(12, [0,12],[4,24])
agent13 = agent(13, [14,0],[5,31])
agent14 = agent(14, [11,26],[25,31])
agent15 = agent(15, [26,10],[22,0])
agents1 = [agent1,agent2,agent3,agent4,agent5, agent6, agent7,agent8, agent9,agent10]

print("######################################################")
print("32x32 blank 15 agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents1,graph))
    print("v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")

agent16 = agent(16,[17,16], [2,16])
agent17 = agent(17,[14,3],[23,5])
agent18 = agent(18,[22,16],[21,31])
agent19 = agent(19, [2,2],[8,5])
agent20 = agent(20, [16,25],[28,22]) #end of first example
agent21 = agent(21,[0,26],[9,31])
agent22 = agent(22, [0,21],[9,24])
agent23 = agent(23, [12,29],[20,27])
agent24 = agent(24,[21,29],[18,31])
agent25 = agent(25, [13,22],[12,19])
agent26 = agent(26, [26,28],[20,23])
agent27 = agent(27, [2,12],[2,18])
agent28 = agent(28,[0,4],[6,6])
agent29 = agent(29, [6,0],[12,9])
agent30 = agent(30,[17,3],[22,8])
agents2 = [agent1,agent2,agent3,agent4,agent5, agent6, agent7,agent8, agent9,agent10, agent11,agent12,agent13,agent14, agent15,
            agent16, agent17, agent18,agent19, agent20
           ]
print("######################################################")
print("32x32 blank 30agents")
"""
try:
    tempGraph = copy.deepcopy(graph)
    print("Time",v1.classicCBS(agents2,tempGraph))
    print(" v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")
""""""
agent31 = agent(31,[9,7],[17,12])
agent32 = agent(32, [14,14],[20,14])
agent33 = agent(33,[21,10],[21,3])
agent34 = agent(34,[30,9],[27,3])
agent35 = agent(35,[23,12],[28,13])
agent36 = agent(36,[21,18],[28,15])
agent37 = agent(37,[29,18],[24,21])
agent38 = agent(38, [29,28],[28,24])
agent39 = agent(39, [6,11],[6,17]) # endof second
agent40 = agent(40, [1,0], [0,8])
agent41 = agent(41, [2,4],[4,0])
agent42 = agent(42, [18,19],[23,23]) # equivalent to 11 blue
agent43 = agent(43, [5,14],[15,17])#5
agent44 = agent(44, [30,20], [24,17]) #14
agent45 = agent(45, [15,9],[19,5])#18
agents3 = [agent41,agent42,agent43,agent44,agent45, agent6, agent7,agent8, agent9,agent10, agent11,agent12,agent13,agent14, agent15,
           agent16, agent17, agent18, agent19, agent20, agent21, agent22, agent23, agent24, agent25, agent26, agent27, agent28,
           agent31, agent32
           ]
print("######################################################")
print("32x32 blank 45agents")
try:
    tempGraph = copy.deepcopy(graph)
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v1 pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 - pop 2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")

except Exception as e:
    print(e)
print("######################################################")
# 32x32 40%

graph = warehouseFloor(32,32)
graphm = graphManger(graph)
graph.setStaticObstacle(
    [
[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0], [15, 0],[20, 0], [21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0], [28, 0], [29, 0], [30, 0], [31, 0],
[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1],[20, 1], [21, 1], [22, 1], [23, 1], [24, 1], [25, 1], [26, 1], [27, 1], [28, 1], [29, 1], [30, 1], [31, 1],
[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [12, 2], [13, 2], [14, 2], [15, 2],
[10, 3], [11, 3], [12, 3], [13, 3], [14, 3], [15, 3], [16, 3], [17, 3],
[10, 4], [11, 4], [12, 4], [13, 4], [14, 4], [15, 4], [16, 4], [17, 4],
[10, 5], [11, 5], [12, 5], [13, 5], [14, 5], [15, 5], [16, 5], [17, 5],
[10, 6], [11, 6], [12, 6], [13, 6], [14, 6], [15, 6], [16, 6], [17, 6],
[10, 7], [11, 7], [12, 7], [13, 7], [14, 7], [15, 7], [16, 7], [17, 7],[20,7],[21,7],[22,7],[23,7],
[20,8],[21,8],[22,8],[23,8],
[20,9],[21,9],[22,9],[23,9],
[6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [11, 10], [12, 10], [13, 10], [14, 10], [15, 10], [16, 10], [17, 10], [18, 10], [19, 10], [20, 10], [21, 10],
[6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [11, 11], [12, 11], [13, 11], [14, 11], [15, 11], [16, 11], [17, 11], [18, 11], [19, 11], [20, 11], [21, 11],
[6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12], [15, 12], [16, 12], [17, 12], [18, 12], [19, 12], [20, 12], [21, 12],
[6, 13], [7, 13], [8, 13], [9, 13], [10, 13], [11, 13], [12, 13], [13, 13], [14, 13], [15, 13], [16, 13], [17, 13], [18, 13], [19, 13], [20, 13], [21, 13],
[6, 14], [7, 14], [8, 14], [9, 14], [10, 14], [11, 14], [12, 14], [13, 14], [14, 14], [15, 14], [16, 14], [17, 14], [18, 14], [19, 14], [20, 14], [21, 14],
[6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [14, 15], [15, 15], [16, 15], [17, 15], [18, 15], [19, 15], [20, 15], [21, 15],
[8, 18], [9, 18], [10, 18], [11, 18], [12, 18], [13, 18], [14, 18], [15, 18], [16, 18], [17, 18], [18, 18], [19, 18], [20, 18], [21, 18], [22, 18], [23, 18], [24, 18], [25, 18], [26, 18], [27, 18], [28, 18],
[8, 19], [9, 19], [10, 19], [11, 19], [12, 19], [13, 19], [14, 19], [15, 19], [16, 19], [17, 19], [18, 19], [19, 19], [20, 19], [21, 19], [22, 19], [23, 19], [24, 19], [25, 19], [26, 19], [27, 19], [28, 19],
[8, 20], [9, 20], [10, 20], [11, 20], [12, 20], [13, 20], [14, 20], [15, 20], [16, 20], [17, 20], [18, 20], [19, 20], [20, 20], [21, 20], [22, 20], [23, 20], [24, 20], [25, 20], [26, 20], [27, 20], [28, 20],
[0, 21], [1, 21], [2, 21], [3, 21], [4, 21], [5, 21],
[0, 22], [1, 22], [2, 22], [3, 22], [4, 22], [5, 22],
[0, 23], [1, 23], [2, 23], [3, 23], [4, 23], [5, 23],
[0, 24], [1, 24], [2, 24], [3, 24], [4, 24], [5, 24],[11, 24], [12, 24], [13, 24], [14, 24], [15, 24], [16, 24], [17, 24], [18, 24], [19, 24], [20, 24], [21, 24], [22, 24], [23, 24], [24, 24], [25, 24],
[0, 25], [1, 25], [2, 25], [3, 25], [4, 25], [5, 25],[11, 25], [12, 25], [13, 25], [14, 25], [15, 25], [16, 25], [17, 25], [18, 25], [19, 25], [20, 25], [21, 25], [22, 25], [23, 25], [24, 25], [25, 25],
[0, 26], [1, 26], [2, 26], [3, 26], [4, 26], [5, 26],[11, 26], [12, 26], [13, 26], [14, 26], [15, 26], [16, 26], [17, 26], [18, 26], [19, 26], [20, 26], [21, 26], [22, 26], [23, 26], [24, 26], [25, 26],
[0, 27], [1, 27], [2, 27], [3, 27], [4, 27], [5, 27],[11, 27], [12, 27], [13, 27], [14, 27], [15, 27], [16, 27],
[0, 28], [1, 28], [2, 28], [3, 28], [4, 28], [5, 28],[11, 28], [12, 28], [13, 28], [14, 28], [15, 28], [16, 28],
[0, 29], [1, 29], [2, 29], [3, 29], [4, 29], [5, 29],[11, 29], [12, 29], [13, 29], [14, 29], [15, 29], [16, 29],
[0, 30], [1, 30], [2, 30], [3, 30], [4, 30], [5, 30],
[0, 31], [1, 31], [2, 31], [3, 31], [4, 31], [5, 31]

    ]
)


#first 15
agent1 = agent(1, [16,0],[31,2])
agent2 = agent(2,[0,3],[9,7])
agent3 = agent(3,[5,3],[6,31])
agent4 = agent(4,[22,10],[18,4])
agent5= agent(5, [29,7],[27,24])
agent6 = agent(6,[17,27],[15,23])
agent7 = agent(7, [25,29],[21,16])
agent8 = agent(8, [1,9],[5,15])
agent9 = agent(9, [26,2], [29,18])
agent10 = agent(10, [11,31],[6,24])
agent11 = agent(11, [9,24],[22,27])
agent12 = agent(12, [0,20], [8,3])
agent13 = agent(13, [14,31],[29,31])
agent14 = agent(14, [28,3], [29,11])
agent15 = agent(15, [2,4],[0,11])
agents1 = [agent1,agent2,agent3,agent4,agent5, agent6, agent7,agent8, agent9,agent10]
print("######################################################")
print("32x32 40% 15agents")
try:
    tempGraph = copy.deepcopy(graph)
    print("Time",v1.classicCBS(agents1,tempGraph))
    print("v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")



agent16 = agent(16, [31,17],[0,17])
agent17 = agent(17, [26,25],[18,21])
agent18 = agent(18,[0,6],[20,31])
agent19 = agent(19, [22,3],[31,5])
agent20 = agent(20, [31,12],[22,12])#end one
agent21 = agent(21, [4,3],[5,7])
agent22 = agent(22, [11,8],[3,9])
agent23 = agent(23, [6,16],[0,13])
agent24 = agent(24, [3,18], [2,13])
agent25 = agent(25, [8,26],[8,31])
agent26 = agent(26, [9,22],[14,23])
agent27 = agent(27, [16,31],[21,27])
agent28 = agent(28, [24,31],[26,26])
agent29 = agent(29, [17,29],[30,31])
agent30 = agent(30, [27,21],[31,28])

agents2 = [agent1,agent2,agent3,agent4,agent5, agent6, agent7,agent8, agent9,agent10, agent11,agent12,agent13,agent14, agent15,
           agent16, agent17,agent18, agent19, agent20
           ]
print("######################################################")
print("32x32 40% 30 agents")
try:
    tempGraph = copy.deepcopy(graph)
    print("Time",v1.classicCBS(agents2,tempGraph))
    print("v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")

agent31 = agent(31, [29,25],[30,21])
agent32 = agent(32, [17,23],[25,21])
agent33 = agent(33, [22,14],[31,14])
agent34 = agent(34,[26,15],[25,9])
agent35 = agent(35,[21,5],[31,6] )
agent36 = agent(36, [17,0],[16,2])
agent37 = agent(37, [16,8],[6,23])
agent38 = agent(38,[26,6],[23,2])
agent39 = agent(39,[31,10],[30,8])# end two
agent40 = agent(40,[9,5],[8,9])
agent41 = agent(41,[10,16],[17,16])
agent42 = agent(42, [6,21],[6,28])
agent43 = agent(43,[8,28],[21,29])
agent44 = agent(44,[29,28], [23,17])
agent45 = agent(45, [21,22], [12,23])
agents3 = [agent1,agent2,agent3,agent4,agent5, agent6, agent7,agent8, agent9,agent10, agent11,agent12,agent13,agent14, agent15,
           agent16, agent17, agent18,agent19, agent20, agent21, agent22, agent23, agent24, agent25, agent26, agent27, agent28, agent29, agent30

           ]
print("######################################################")
print("32x32 40% 45 agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v1 pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 -pop2 buf 1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 -pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")

# 32x32 60%
graph = warehouseFloor(32, 32)
graphm = graphManger(graph)
graph.setStaticObstacle(
    [
        [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0],
        [13, 0], [14, 0], [15, 0], [20, 0], [21, 0], [22, 0], [23, 0], [24, 0], [25, 0], [26, 0], [27, 0], [28, 0],
        [29, 0], [30, 0], [31, 0],
        [0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1],
        [13, 1], [14, 1], [15, 1], [20, 1], [21, 1], [22, 1], [23, 1], [24, 1], [25, 1], [26, 1], [27, 1], [28, 1],
        [29, 1], [30, 1], [31, 1],
        [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2], [11, 2], [12, 2],
        [13, 2], [14, 2], [15, 2],
        [10, 3], [11, 3], [12, 3], [13, 3], [14, 3], [15, 3], [16, 3], [17, 3],
        [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4], [11, 4], [12, 4], [13, 4], [14, 4], [15, 4],
        [16, 4], [17, 4], [21, 4], [22, 4], [23, 4], [27, 4], [28, 4], [29, 4], [30, 4], [31, 4],
        [6, 5], [7, 5], [8, 5], [9, 5], [10, 5], [11, 5], [12, 5], [13, 5], [14, 5], [15, 5], [16, 5], [17, 5], [21, 5],
        [22, 5], [23, 5], [27, 5], [28, 5], [29, 5], [30, 5], [31, 5],
        [0, 6], [1, 6], [2, 6], [8, 6], [9, 6], [10, 6], [11, 6], [12, 6], [13, 6], [14, 6], [15, 6], [16, 6], [17, 6],
        [21, 6], [22, 6], [23, 6], [27, 6], [28, 6], [29, 6], [30, 6], [31, 6],
        [0, 7], [1, 7], [2, 7], [9, 7], [10, 7], [11, 7], [12, 7], [13, 7], [14, 7], [15, 7], [16, 7], [17, 7], [20, 7],
        [21, 7], [22, 7], [23, 7], [29, 7], [30, 7], [31, 7],
        [0, 8], [1, 8], [2, 8], [20, 8], [21, 8], [22, 8], [23, 8],
        [0, 9], [1, 9], [2, 9], [20, 9], [21, 9], [22, 9], [23, 9], [29, 9], [30, 9], [31, 9],
        [0, 10], [1, 10], [2, 10], [6, 10], [7, 10], [8, 10], [9, 10], [10, 10], [11, 10], [12, 10], [13, 10], [14, 10],
        [15, 10], [16, 10], [17, 10], [18, 10], [19, 10], [20, 10], [21, 10],
        [0, 11], [1, 11], [2, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11], [11, 11], [12, 11], [13, 11], [14, 11],
        [15, 11], [16, 11], [17, 11], [18, 11], [19, 11], [20, 11], [21, 11],
        [0, 12], [1, 12], [2, 12], [6, 12], [7, 12], [8, 12], [9, 12], [10, 12], [11, 12], [12, 12], [13, 12], [14, 12],
        [15, 12], [16, 12], [17, 12], [18, 12], [19, 12], [20, 12], [21, 12],
        [0, 13], [1, 13], [2, 13], [6, 13], [7, 13], [8, 13], [9, 13], [10, 13], [11, 13], [12, 13], [13, 13], [14, 13],
        [15, 13], [16, 13], [17, 13], [18, 13], [19, 13], [20, 13], [21, 13],
        [0, 14], [1, 14], [2, 14], [6, 14], [7, 14], [8, 14], [9, 14], [10, 14], [11, 14], [12, 14], [13, 14], [14, 14],
        [15, 14], [16, 14], [17, 14], [18, 14], [19, 14], [20, 14], [21, 14],
        [6, 15], [7, 15], [8, 15], [9, 15], [10, 15], [11, 15], [12, 15], [13, 15], [14, 15], [15, 15], [16, 15],
        [17, 15], [18, 15], [19, 15], [20, 15], [21, 15],
        [0, 16], [1, 16],
        [0, 18], [1, 18], [2, 18], [3, 18], [8, 18], [9, 18], [10, 18], [11, 18], [12, 18], [13, 18], [14, 18],
        [15, 18], [16, 18], [17, 18], [18, 18], [19, 18], [20, 18], [21, 18], [22, 18], [23, 18], [24, 18], [25, 18],
        [26, 18], [27, 18], [28, 18],
        [0, 19], [1, 19], [2, 19], [3, 19], [8, 19], [9, 19], [10, 19], [11, 19], [12, 19], [13, 19], [14, 19],
        [15, 19], [16, 19], [17, 19], [18, 19], [19, 19], [20, 19], [21, 19], [22, 19], [23, 19], [24, 19], [25, 19],
        [26, 19], [27, 19], [28, 19],
        [0, 20], [1, 20], [2, 20], [3, 20], [8, 20], [9, 20], [10, 20], [11, 20], [12, 20], [13, 20], [14, 20],
        [15, 20], [16, 20], [17, 20], [18, 20], [19, 20], [20, 20], [21, 20], [22, 20], [23, 20], [24, 20], [25, 20],
        [26, 20], [27, 20], [28, 20],
        [0, 21], [1, 21], [2, 21], [3, 21], [4, 21], [5, 21],
        [0, 22], [1, 22], [2, 22], [3, 22], [4, 22], [5, 22],
        [0, 23], [1, 23], [2, 23], [3, 23], [4, 23], [5, 23], [18, 23], [19, 23], [20, 23], [21, 23], [22, 23],
        [23, 23], [24, 23], [25, 23], [26, 23], [27, 23], [28, 23],
        [0, 24], [1, 24], [2, 24], [3, 24], [4, 24], [5, 24], [8, 24], [9, 24], [10, 24], [11, 24], [12, 24], [13, 24],
        [15, 24], [18, 24], [19, 24], [20, 24], [21, 24], [22, 24], [23, 24], [24, 24], [25, 24], [26, 24], [27, 24],
        [28, 24],
        [0, 25], [1, 25], [2, 25], [3, 25], [4, 25], [5, 25], [8, 25], [9, 25], [10, 25], [11, 25], [12, 25], [13, 25],
        [15, 25], [18, 25], [19, 25], [20, 25], [21, 25], [22, 25], [23, 25], [24, 25], [25, 25], [26, 25], [27, 25],
        [28, 25],
        [0, 26], [1, 26], [2, 26], [3, 26], [4, 26], [5, 26], [8, 26], [9, 26], [10, 26], [11, 26], [12, 26], [13, 26],
        [16, 26], [17, 26], [18, 26], [19, 26], [20, 26], [21, 26], [22, 26], [23, 26], [24, 26],
        [0, 27], [1, 27], [2, 27], [3, 27], [4, 27], [5, 27], [8, 27], [9, 27], [10, 27], [11, 27], [12, 27], [13, 27],
        [16, 27], [17, 27], [18, 27], [30, 27], [31, 27],
        [0, 28], [1, 28], [2, 28], [3, 28], [4, 28], [5, 28], [8, 28], [9, 28], [10, 28], [11, 28], [12, 28], [13, 28],
        [16, 28], [17, 28], [18, 28], [28, 28], [29, 28], [30, 28], [31, 28],
        [0, 29], [1, 29], [2, 29], [3, 29], [4, 29], [5, 29], [8, 29], [9, 29], [10, 29], [11, 29], [12, 29], [13, 29],
        [16, 29], [17, 29], [18, 29], [19, 29], [20, 29], [21, 29], [22, 29], [23, 29], [24, 29], [25, 29], [26, 29],
        [27, 29], [28, 29], [29, 29], [30, 29], [31, 29],
        [0, 30], [1, 30], [2, 30], [3, 30], [4, 30], [5, 30], [16, 30], [17, 30], [18, 30], [19, 30], [20, 30],
        [21, 30], [22, 30], [23, 30], [24, 30], [25, 30], [26, 30], [27, 30], [28, 30], [29, 30], [30, 30], [31, 30],
        [0, 31], [1, 31], [2, 31], [3, 31], [4, 31], [5, 31], [16, 31], [17, 31], [18, 31], [19, 31], [20, 31],
        [21, 31], [22, 31], [23, 31], [24, 31], [25, 31], [26, 31], [27, 31], [28, 31], [29, 31], [30, 31], [31, 31]

    ]
)
agent1 = agent(1, [16, 0], [31, 2])
agent2 = agent(2, [31, 8], [26, 4])
agent3 = agent(3, [8, 7], [19, 9])
agent4 = agent(4, [11, 8], [9, 3])
agent5 = agent(5, [18, 3], [31, 3])
agent6 = agent(6, [0, 5], [0, 15])
agent7 = agent(7, [3, 8], [18, 1])
agent8 = agent(8, [25, 15], [22, 10])
agent9 = agent(9, [4, 20], [31, 16])
agent10 = agent(10, [8, 17], [22, 12])
agent11 = agent(11, [20, 27], [29, 18])
agent12 = agent(12, [16, 24], [6, 31])
agent13 = agent(13, [6, 22], [25, 22])
agent14 = agent(14, [10, 31], [14, 27])
agent15 = agent(15, [20, 28], [10, 23])
agents1 = [agent1, agent2, agent3, agent4, agent5, agent6, agent7, agent8, agent9, agent10]
print("######################################################")
print("32x32 60% 15agents")
try:
    tempGraph = copy.deepcopy(graph)
    print("Time",v1.classicCBS(agents1,tempGraph))
    print("v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v2 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph,2,1 ))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents1)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
except Exception as e:
    print(e)
print("######################################################")

agent16 = agent(16, [13, 9], [5, 9])
agent17 = agent(17, [22, 17], [12, 17])
agent18 = agent(18, [0, 17], [12, 23])
agent19 = agent(19, [12, 31], [6, 26])
agent20 = agent(20, [11, 22], [23, 22])
agent21 = agent(21, [24, 28], [31, 23])
agent22 = agent(22, [25, 26], [25, 17])
agent23 = agent(23, [19, 0], [17, 23])
agent24 = agent(24, [20, 6], [21, 2])
agent25 = agent(25, [16, 16], [25, 8])
agent26 = agent(26, [0, 3], [24, 3])
agent27 = agent(27, [26, 22], [28, 27])
agent28 = agent(28, [14, 26], [15, 21])
agent29 = agent(29, [10, 17], [2, 16])
agent30 = agent(30, [6, 9], [4, 5])

agents2 = [agent1,agent2,agent3,agent4,agent5, agent6, agent7,agent8, agent9,agent10, agent11, agent12 ,agent14, agent15,
           agent16, agent17, agent19, agent18, agent22, agent23


           ]
print("######################################################")
print("32x32 60% 30agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents2,graph))
    print("v1- pop2 buf1--------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v1 pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 -pop2  buf1---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 - pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents2)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")

except Exception as e:
    print(e)
print("######################################################")

agent31 = agent(31, [16, 2], [29, 3])
agent32 = agent(32, [4, 12], [5, 18])
agent33 = agent(33, [29, 20], [19, 22])
agent34 = agent(34, [25, 12], [16, 17])
agent35 = agent(35, [28, 9], [23, 14])
agent36 = agent(36, [24, 5], [28, 7])
agent37 = agent(37, [5, 5], [9, 8])
agent38 = agent(38, [22, 28], [31, 26])
agent39 = agent(39, [9, 23], [8, 31])
agent40 = agent(40, [4, 3], [0, 4])
agent41 = agent(41, [15, 31], [29, 19])
agent42 = agent(42, [17, 17], [5, 7])
agent43 = agent(43, [15, 8], [30, 2])
agent44 = agent(44, [17, 0], [18, 4])
agent45 = agent(45, [6, 16], [5, 10])

agents3 = [agent1,agent2,agent3,agent4,agent5, agent6, agent7,agent8, agent9,agent10, agent11, agent12 ,agent14, agent15,
           agent16, agent17, agent19, agent18, agent22, agent23, agent24, agent25, agent28, agent29,agent30, agent31, agent34, agent35


           ]
print("######################################################")
print("32x32 60% 45agents")
try:
    tempGraph = copy.deepcopy(graph)
    print(v1.classicCBS(agents3,graph))
    print("v1 pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,1 ))
    print("v1 pop2 buf2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV1(tempAgents,graph,2,2 ))
    print("v2 - pop2 buf1---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,1))
    print("v2 - pop2 buf 2---------------------------------")
    tempAgents = copy.deepcopy(agents3)
    print(g1.graphPartitionV2(tempAgents,graph, 2,2))
    print("---------------------------------")
    
except Exception as e:
    print(e)
print("######################################################")
"""
