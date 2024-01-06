import unittest
from parameterized import parameterized
from src.aStar import aStar,aStarNode
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent

class TestAstar(unittest.TestCase):

    def setUp(self):
        self.graphDict = {}
        self.agentDict = {}


        self.graphDict["graphEndPosBlocking"] = warehouseFloor(9,7)
        self.graphDict["graphEndPosBlocking"].setStaticObstacle([
            [0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]
            ,[6,1],[7,1],[8,1]
            ,[0,2],[1,2],[2,2],[3,2],[4,2],[6,2],[7,2],[8,2]

            ,[0,4],[1,4],[2,4],[3,4],[4,4],[6,4],[7,4],[8,4]
            ,[4,5],[6,5]
            ,[4,6],[7,6]
        ])
        agent1 = agent(1,[4,1],[5,6])
        agent2 = agent(2, [0, 1], [6, 6])
        agent3 = agent(3, [0, 3], [8, 3])
        self.agentDict["graphEndPosBlocking1"] = agent1
        self.agentDict["graphEndPosBlocking2"] = agent2
        self.agentDict["graphEndPosBlocking3"] = agent3
        self.expectedPath = {}

        self.expectedPath["graphEndPosBlocking1"] = [aStarNode(5,6,0), aStarNode(5,5,1), aStarNode(5,4,2),
                                                    aStarNode(5,3,3), aStarNode(5,2,4),aStarNode(5,1,5),
                                                    aStarNode(4,1,6)]


        self.expectedPath["graphEndPosBlocking2"] = [aStarNode(6,6,0), aStarNode(5,6,1), aStarNode(5,5, 2),
                                                     aStarNode(5,4,3), aStarNode(5,3,4), aStarNode(5,2,5),
                                                     aStarNode(5,1,6), aStarNode(4,1,7), aStarNode(3,1,8),
                                                     aStarNode(2,1,9), aStarNode(1,1,10), aStarNode(0,1,11)]

        self.expectedPath["graphEndPosBlocking3"] = [aStarNode(8,3,0), aStarNode(7,3,1), aStarNode(6,3,2),
                                                     aStarNode(5,3, 3), aStarNode(4,3,4), aStarNode(3,3, 5),
                                                     aStarNode(2,3, 6), aStarNode(1,3, 7), aStarNode(0,3, 8)]


        node1 = aStarNode(0,1,0)
        node1.setTotalCost(12)
        node1.setMovementCost(12)

        node2 = aStarNode(4,8,1)
        node2.setTotalCost(15)
        node2.setMovementCost(16)

        node3 = aStarNode(2,3,0)
        node3.setTotalCost(13)
        (node3.setMovementCost(13))

        self.minNodeDict = {}
        self.openSetDict = {}

        set1 = set()
        set1.add(node1)
        set1.add(node2)
        set1.add(node3)
        self.openSetDict["setNoDuplicateCosts"] = set1
        self.minNodeDict["setNoDuplicateCosts"] = node1
        self.aStarNodesDict = {}
        self.aStarNodesDict["node1"] = node1
        self.aStarNodesDict["node2"] = node2
        self.aStarNodesDict["node3"] = node3


    #add more scenarios with various constraints x
    @parameterized.expand(
        [

           ["graphEndPosBlocking",[],"graphEndPosBlocking1",8,"graphEndPosBlocking1"],
            ["graphEndPosBlocking", [], "graphEndPosBlocking2", 8, "graphEndPosBlocking2"],
            ["graphEndPosBlocking", [], "graphEndPosBlocking3", 8, "graphEndPosBlocking3"]

        ]
    )
    def testAstarPossiblePath(self,graph,constraints,agent,previousLongestPath,expectedPath):
        wh = graphManger(self.graphDict[graph])
        aStarObj = aStar(wh)
        self.assertEqual(aStarObj.findPath(constraints,self.agentDict[agent],previousLongestPath), self.expectedPath[expectedPath])


    @parameterized.expand(
        [
        ["graphEndPosBlocking", [], agent(1,[5,0], [5,6]), 8],
        ["graphEndPosBlocking",[], agent(2,[5,3], [8,6]), 8 ]
    ]
    )
    def testAstarNoPossiblePath(self,graph,constraints,agent,previousLongestPath):
        wh = graphManger(self.graphDict[graph])
        aStarObj = aStar(wh)
        self.assertFalse(aStarObj.findPath(constraints,agent,previousLongestPath))


    #similar to the getLeastCostFunction in cbs this test will need to be improved when i change set to pq
    @parameterized.expand(
        [
            ["graphEndPosBlocking", "setNoDuplicateCosts","setNoDuplicateCosts"]
        ]
    )
    def testGetLeastCost(self,graph,openSet, expectedResult):
        wh = graphManger(self.graphDict[graph])
        aStarObj = aStar(wh)
        self.assertEqual(aStarObj.getLeastCost(self.openSetDict[openSet]), self.minNodeDict[expectedResult])

    @parameterized.expand(
        [
            ["graphEndPosBlocking", [0,0], "node1",1 ],
            ["graphEndPosBlocking", [0, 0], "node2", 12],
            ["graphEndPosBlocking", [0, 0], "node3", 5]
        ]
    )
    def testHeuristicCalcultation(self, graph,goal, currentNode,expectedResult):
        wh = graphManger(self.graphDict[graph])
        aStarObj = aStar(wh)
        self.assertEqual(expectedResult,aStarObj.calculateHeurisitic(goal,self.aStarNodesDict[currentNode]))


    @parameterized.expand(
    [
        ["graphEndPosBlocking",[0,1], [0,1],True],
        ["graphEndPosBlocking", [0,1], [1,3 ], False]


    ]
    )
    def testAtGoal(self,graph, currentNode,goal, result):
        wh = graphManger(self.graphDict[graph])
        aStarObj = aStar(wh)
        self.assertEqual(aStarObj.atGoal(currentNode,goal),result)
""" 



    @parameterized.expand(
    [

    ]
    )
    def testBuildPath(self,graph,nodeCameFromDict, currentNode,startPos,expectedPath):
        wh = graphManger(self.graphDict[graph])
        aStarObj = aStar(wh)
        self.assertEqual(aStarObj.buildPath(currentNode), expectedPath)



"""
if __name__ == '__main__':
 unittest.main()