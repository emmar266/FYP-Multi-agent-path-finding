import unittest
from parameterized import parameterized
import src.setupGrid as setupGrid
from src.aStar import aStarNode, aStar




class TestGridSetup(unittest.TestCase):

    def setUp(self):
        self.gridDicts = {}
        self.gridDicts["graphNoStatic"] = setupGrid.warehouseFloor(4,4)

        graphStaticObj = setupGrid.warehouseFloor(4,4)
        graphStaticObj.setStaticObstacle([[0,0],[3,3],[3,0]])
        self.gridDicts["graphStaticObj"] = graphStaticObj


    @parameterized.expand([
           ["graphNoStatic",[0,0]], 
           ["graphStaticObj",[0,1]]
           ]
    )
    def testWarehouseValidMovement(self,grid,suggestedMove):
        self.assertTrue(self.gridDicts[grid].checkValidMovement(suggestedMove))


    @parameterized.expand([
       ["graphNoStatic", [[0,0],[0,1]]],
       ["graphStaticObj",[[0,0],[3,3],[3,0]]]  
       ]
    )
    def testSetStaticObstacle(self,grid,obstacls):
        self.gridDicts[grid].setStaticObstacle(obstacls)
        for obstacle in obstacls:
            a = (self.gridDicts[grid].floorPlan[obstacle[1]][obstacle[0]])
            if self.gridDicts[grid].floorPlan[obstacle[1]][obstacle[0]] == "Blocked":
                self.assertTrue(True)
            else:
                self.assertTrue(False)


    @parameterized.expand(
        [
           ["graphNoStatic", [0,1], [[0,1,2]], 0 ],
           ["graphStaticObj",[2,3],[[]],1]
        ]
    )
    def testGraphValidMovement(self, graph,suggestedMovement,constraints, currentTime):
        gm = setupGrid.graphManger(self.gridDicts[graph])
        self.assertTrue(gm.checkValidMovement(suggestedMovement,constraints,currentTime))

    @parameterized.expand(
        [
           ["graphNoStatic", [0,1], [[0,1,2]],2 ],
           ["graphStaticObj",[-1,0],[[]],9]
        ]
    )
    def testGraphValidMovemementWithInvalid(self,graph,suggestedMovement,constraints,currentTime):
        gm = setupGrid.graphManger(self.gridDicts[graph])
        self.assertFalse(gm.checkValidMovement(suggestedMovement,constraints,currentTime))

    @parameterized.expand(
        [
           ["graphNoStatic", [0,1], [[0,1,2]],2 ],
           ["graphStaticObj",[-1,0],[[]],9]
        ]
    )
    def testFindValidNeighbours(self,graph,currentNode, contraints,expectedValidNeighbours):
        
        self.assertTrue(True)
        pass

