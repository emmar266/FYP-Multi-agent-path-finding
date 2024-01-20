import unittest
from parameterized import parameterized
from src.setupGrid import warehouseFloor
from src.agent import agent

class TestCBS(unittest.TestCase):

    def setUp(self):
        self.graphDict = {}
        self.agentDict = {}

        self.graphDict["graphEndPosBlocking"] = warehouseFloor(9, 7)
        self.graphDict["graphEndPosBlocking"].setStaticObstacle([
            [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]
            , [6, 1], [7, 1], [8, 1]
            , [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [6, 2], [7, 2], [8, 2]

            , [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [6, 4], [7, 4], [8, 4]
            , [4, 5], [6, 5]
            , [4, 6], [7, 6]
        ])
        agent1 = agent(1,[4,1],[5,6])
        agent2 = agent(2, [0, 1], [6, 6])
        agent3 = agent(3, [0, 3], [8, 3])

        self.agentDict["graphEndPosBlocking"] = [agent1, agent2, agent3]


    @parameterized.expand(
        [
        ]
    )
    def testPrioritisedPlanningValid(self):
        pass

    @parameterized.expand(
        [
            ["graphEndPosBlocking","graphEndPosBlocking"]
        ]
    )
    def testPrioritisedPlanningInvalid(self,graph, agents):
        pass


    @parameterized.expand(
        [
        ]
    )
    def testRandomiseOrdering(self):
        pass