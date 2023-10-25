import treeStructure
import aStar
import setupGrid

class highLevel:
    def __init__(self,graph) -> None:
        self.agents = {} # gonna be structured with id:path
        self.constraints = {} #"agent": (x,y) : [time1,time2 ...]
        
        self.graphManager =setupGrid.graphManger(graph)
        self.aStar = aStar(self.graphManager)


    def cbs(self,warehouse,agents):
        #tree = x
        #first iteration of path finding for all agents
        #   return paths 
        #   check for collisions 
        highLevelTree = treeStructure()
        #run path finding algo for all paths no constraints - should return list of all paths for each robot/task
        paths = self.findPathsForAll([]) 
        currentCollisions = self.collsionsFound(paths)
        #need check which will break out of function if there's no collisons 
        
        #from the collisons we want to create x new nodes on a tree based on the number of robots in the collison 
        #   can't be more than 4 if robots can only move L R U D - could be 8 if diagonal movements allowed - nawr 
        

        #find constraints
        # run first 
        currentCollisions = None
        while currentCollisions != None:
            #run path finding for everynode with new collisons
            #lowlevel 
            currentCollisions = self.collsionsFound(paths)

    def collsionsFound(self,paths): #returns the collsions found as a list or dict etc 
        collisions = {}
        return collisions

    def findPathsForAll(self,constraints):
        paths = []
        for agent in self.agents:
            paths.append(self.aStar.findPath(constraints,agent)) # this will return the paths
        return paths