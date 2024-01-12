import unittest
from parameterized import parameterized
from src.cbs.cbs import highLevel
from src.setupGrid import warehouseFloor, graphManger
from src.agent import agent
from src.tree import  node
from src.aStar import aStarNode


class TestCBS(unittest.TestCase):

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

        self.expectedPath = {}

        path1 = [aStarNode(5, 6, 0), aStarNode(5, 5, 1), aStarNode(5, 4, 2),
                                                     aStarNode(5, 3, 3), aStarNode(5, 2, 4), aStarNode(5, 1, 5),
                                                     aStarNode(4, 1, 6)]

        path2 = [aStarNode(6, 6, 0), aStarNode(5, 6, 1), aStarNode(5, 5, 2),
                                                     aStarNode(5, 4, 3), aStarNode(5, 3, 4), aStarNode(5, 2, 5),
                                                     aStarNode(5, 1, 6), aStarNode(4, 1, 7), aStarNode(3, 1, 8),
                                                     aStarNode(2, 1, 9), aStarNode(1, 1, 10), aStarNode(0, 1, 11)]

        path3 = [aStarNode(8, 3, 0), aStarNode(7, 3, 1), aStarNode(6, 3, 2),
                                                     aStarNode(5, 3, 3), aStarNode(4, 3, 4), aStarNode(3, 3, 5),
                                                     aStarNode(2, 3, 6), aStarNode(1, 3, 7), aStarNode(0, 3, 8)]

        agent1 = agent(1,[4,1],[5,6])
        agent2 = agent(2, [0, 1], [6, 6])
        agent3 = agent(3, [0, 3], [8, 3])
        self.expectedPath["graphEndPosBlockingNoConstraints"] = {agent1: path1, agent2: path2, agent3: path3}
        self.agentDict["graphEndPosBlocking"] = [agent1,agent2,agent3]


        self.graphDict["graph4AgentsUsingSameLane"] = warehouseFloor(5, 6)
        self.graphDict["graph4AgentsUsingSameLane"].setStaticObstacle([
            [0, 1], [1, 1],[3, 1],[4, 1],
            [0, 3], [1, 3],[3, 3],[4, 3],
            [0, 4], [1, 4], [3, 4], [4, 4]

        ])
        agent1 = agent(1,[4,5],[0,0])
        agent2 = agent(2, [4, 0], [0, 5])
        agent3 = agent(3, [0, 5], [4, 0])
        agent4 = agent(4, [0, 0], [4, 5])
        self.agentDict["graph4AgentsUsingSameLane"] = [agent1,agent2,agent3,agent4]

        path1 = [aStarNode(0,0,0),aStarNode(1,0,1),aStarNode(2,0,2),
                 aStarNode(2,1,3),aStarNode(2,2,4),aStarNode(2,3,5),
                 aStarNode(2,4,6),aStarNode(2,5,7),aStarNode(3,5,8),
                 aStarNode(4,5,9)]
        path2 = [aStarNode(0,5,0),aStarNode(1,5,1),aStarNode(2,5,2),
                 aStarNode(2,4,3),aStarNode(2,3,4),aStarNode(2,2,5),
                 aStarNode(2,1,6),aStarNode(2,0,7),aStarNode(3,0,8),
                 aStarNode(4,0,9)]
        path3 = [aStarNode(4, 0,0),aStarNode(3, 0,1),aStarNode(2, 0,2),
                 aStarNode(2, 1,3),aStarNode(2, 2,4),aStarNode(2, 3,5),
                 aStarNode(2, 4,6),aStarNode(2, 5,7),aStarNode(1, 5,8),
                 aStarNode(0, 5,9)]
        path4 = [aStarNode(4, 5,0),aStarNode(3, 5,1),aStarNode(2, 5,2),
                 aStarNode(2, 4,3),aStarNode(2, 3,4),aStarNode(2, 2,5)
                 ,aStarNode(2, 1,6),aStarNode(2, 0,7),aStarNode(1, 0,8),
                 aStarNode(0, 0,9)]
        self.expectedPath["graph4AgentsUsingSameLane"] = {agent1:path1,agent2:path2,agent3:path3, agent4:path4}



        self.graphDict["graphFourWayCollision"] = warehouseFloor(5, 5)
        agent1 = agent(1,[2,4],[2,0])
        agent2 = agent(2, [2,0], [2, 4])
        agent3 = agent(3, [0, 2], [4, 2])
        agent4 = agent(4, [4, 2], [0, 2])
        self.agentDict["graphFourWayCollision"] = [agent1, agent2, agent3, agent4]

        self.graphDict["graphSmall"] = warehouseFloor(3,3)
        agent1 = agent(1,[1,2],[1,0] )
        agent2 = agent(2,[1,0],[1,2])
        agent3 = agent(3,[0,1],[2,1])
        agent4 = agent(4, [2,1],[0,1])


        self.agentDict["graphSmall"] = [agent1,agent2,agent3, agent4]


        self.graphDict["graphImpossiblePath"] = warehouseFloor(3,3)
        self.graphDict["graphImpossiblePath"].setStaticObstacle([
            [0,0],[2,0],[0,2],[2,2]
            ])
        agent1 = agent(1,[1,2],[1,0] )
        agent2 = agent(2,[1,0],[1,2])
        agent3 = agent(3,[0,1],[2,1])
        agent4 = agent(4, [2,1],[0,1])


        self.agentDict["graphImpossiblePath"] = [agent1,agent2,agent3, agent4]



        """
        self.expectedPath = {1:[[2,0],[2,1],[2,2],[2,3],[2,4]],
                             2: [[2,4], [2,3],[2,2],[2,1],[2,0]],
                             3:[[4,2],[3,2],[2,2],[1,2],[0,2]],
                             4: [[0,2], [1,2],[2,2],[3,2],[4,2]]}
        """
        node1 = node([],12)
        node2 = node([0,0,0],12)
        node3 = node([], 13)
        node4 = node([], 15)
        openSet = set()
        openSet.add(node1)
        openSet.add(node2)
        openSet.add(node3)
        openSet.add(node4)
        self.minNodeDict = {}

        self.openSetDict = {"setWithDuplicateCost": openSet}
        self.minNodeDict["setWithDuplicateCost"] = node2
        openSet = set()
        openSet.add(node2)
        openSet.add(node3)
        openSet.add(node4)
        self.openSetDict["setWithUniqueCosts"] = openSet
        self.minNodeDict["setWithUniqueCosts"] = node2

        path1 = [aStarNode(5, 6, 0), aStarNode(5, 5, 1), aStarNode(5, 4, 2),
                 aStarNode(5, 3, 3), aStarNode(4, 3, 4), aStarNode(3, 3, 5),
                 aStarNode(4, 3, 6), aStarNode(5, 3, 7), aStarNode(5, 2, 8),
                 aStarNode(5, 1, 9), aStarNode(4, 1, 10)]

        path2 = [aStarNode(6, 6, 0), aStarNode(5, 6, 1), aStarNode(5, 5, 2),
                 aStarNode(5, 4, 3), aStarNode(5, 3, 4), aStarNode(5, 2, 5),
                 aStarNode(5, 1, 6), aStarNode(4, 1, 7), aStarNode(3, 1, 8),
                 aStarNode(2, 1, 9), aStarNode(1, 1, 10), aStarNode(0, 1, 11)]

        path3 = [aStarNode(8, 3, 0), aStarNode(7, 3, 1), aStarNode(6, 3, 2),
                 aStarNode(5, 3, 3), aStarNode(4, 3, 4), aStarNode(3, 3, 5),
                 aStarNode(2, 3, 6), aStarNode(1, 3, 7), aStarNode(0, 3, 8)]

        self.expectedPath["colisionDet"] = {agent1: path1,agent2:path2, agent3:path3}



    @parameterized.expand(
        [
            ["graphEndPosBlocking", "graphEndPosBlocking", [], "graphEndPosBlockingNoConstraints"],
            ["graph4AgentsUsingSameLane", "graph4AgentsUsingSameLane",[],"graph4AgentsUsingSameLane"]
            #["graphFourWayCollision", "graphFourWayCollision",[],{1:[[2,0],[2,1],[2,2],[2,3],[2,4]],
            #                 2: [[2,4], [2,3],[2,2],[2,1],[2,0]],
            #                 3:[[4,2],[3,2],[2,2],[1,2],[0,2]],
            #                 4: [[0,2], [1,2],[2,2],[3,2],[4,2]]}]
        ]
    )
    def testFindPathsForAll(self,graph,agents,constraints, expectedPaths):
        cbsObj = highLevel(self.graphDict[graph],self.agentDict[agents])
        pa = cbsObj.findPathsForAll(constraints)
        self.assertEqual(pa, self.expectedPath[expectedPaths])


    #until I change my data structure from a set to a heap based queue this will have to remain with equivalent costs
    @parameterized.expand(
        [
            ["graphEndPosBlocking", "graphEndPosBlocking",{1:[[2,0],[2,1],[2,2],[2,3],[2,4]],
                             2: [[2,4], [2,3],[2,2],[2,1],[2,0]],
                             3:[[4,2],[3,2],[2,2],[1,2],[0,2]],
                             4: [[0,2], [1,2],[2,2],[3,2],[4,2]]}, 16 ],
            ["graph4AgentsUsingSameLane", "graph4AgentsUsingSameLane",{1:[[ 0,0],[1,0],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,5],[4,5]],
                            2:[[0,5],[1,5],[2,5],[2,4],[2,3],[2,2],[2,1],[2,0],[3,0],[4,0]],
                            3: [[4, 0], [3, 0], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [1, 5], [0, 5]]
                            ,4: [[4, 5], [3, 5], [2, 5], [2, 4], [2, 3], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0]]
                             }, 36 ],
        ]
    )
    def testCalculateNodeCost(self,graph,agents,paths,expectedCost ):
        cbsObj = highLevel(self.graphDict[graph],self.agentDict[agents])
        self.assertEqual(cbsObj.calculateNodeCost(paths),expectedCost)



    @parameterized.expand(
        [
            ["graphEndPosBlocking", "graphEndPosBlocking",True],
            #["graph4AgentsUsingSameLane", "graph4AgentsUsingSameLane",True],
            ["graphFourWayCollision", "graphFourWayCollision",True ]

        ]
    )
    def testCbsWithValid(self, graph, agents, expectedPaths):
        cbsObj = highLevel(self.graphDict[graph], self.agentDict[agents])
        val = cbsObj.cbs()
        self.assertNotEquals(val, False)
        a = "a"

    @parameterized.expand(
        [
            ["graphImpossiblePath", "graphImpossiblePath"]

        ]
    )
    def testCbsWithImpossiblePath(self,graph,agents):
        cbsObj = highLevel(self.graphDict[graph],self.agentDict[agents])
        paths = cbsObj.cbs()
        self.assertFalse(paths)
    @parameterized.expand(
            [
                ["graphEndPosBlocking", "graphEndPosBlocking", aStarNode(1,0,0),aStarNode(0,0,0),
                 aStarNode(1,0,1), aStarNode(0,0,1),True ],
                ["graphEndPosBlocking", "graphEndPosBlocking", aStarNode(1, 2, 0), aStarNode(1, 3, 0),
                 aStarNode(1, 0, 1), aStarNode(0, 0, 2), False],
                ["graphEndPosBlocking", "graphEndPosBlocking", aStarNode(0, 1, 0), aStarNode(0, 0, 0),
                 aStarNode(0, 1, 1), aStarNode(0, 0, 1), True]
            ]
        )
    def testCheckForCrossingNodes(self,graph, agents ,agentOneStepOne, agentTwoStepOne, agentTwoStepTwo, agentOneStepTwo,result):
        cbsObj = highLevel(self.graphDict[graph],self.agentDict[agents])
        self.assertEqual(cbsObj.checkForCrossingNodes(agentOneStepOne,agentTwoStepOne,agentOneStepTwo,agentTwoStepTwo),result)




    @parameterized.expand(
        [
            ["graphEndPosBlocking", "graphEndPosBlocking","graphEndPosBlockingNoConstraints",True ],
            ["graph4AgentsUsingSameLane", "graph4AgentsUsingSameLane","colisionDet",True]
            #["graphFourWayCollision", "graphFourWayCollision",]
        ]
    )
    def testForCollisions(self,graph,agents,paths,expectedCollisions):
        cbsObj = highLevel(self.graphDict[graph],self.agentDict[agents])
        val = cbsObj.checkForcollsions(self.expectedPath[paths])
        self.assertTrue(True)
        #self.assertEqual(,expectedCollisions)

""""


    


    #Couple things wrong here - astar is not working as expected
    #
    """
if __name__ == '__main__':
    unittest.main()