from src.pp.prioritised import prioritisedPlanning
from src.setupGrid import graphManger
from src.cbs.cbs import highLevel, ConstraintsStructure
from src.aStar import aStar
from src.pathObj import Paths

class reservedAreaBufferArea:
    def __init__(self,graph, agents):
        self.graph = graphManger(graph)
        self.graphArea = self.graph.graph.width * self.graph.graph.length
        self.agents = agents

    #I don't think this is necessary - the constraints shouldn't be
    def setupInitialConstraintsCBS(self,paths):
        constraints = {}
        for agent in self.agents:
            constraints[agent.agentId] = ConstraintsStructure(agent.agentId, paths)
        return constraints

    def addBuffer(self, currentNode,constraints):
        time = currentNode.time
        validNeighbours = []
        validMovement = self.graph.checkValidMovement([currentNode.x, currentNode.y - 1], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x, currentNode.y - 1,time])
        validMovement = self.graph.checkValidMovement([currentNode.x-1, currentNode.y - 1], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x-1, currentNode.y - 1,time])
        validMovement = self.graph.checkValidMovement([currentNode.x+1, currentNode.y - 1], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x, currentNode.y - 1,time])


        validMovement = self.graph.checkValidMovement([currentNode.x, currentNode.y + 1], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x, currentNode.y + 1,time])

        validMovement = self.graph.checkValidMovement([currentNode.x-1, currentNode.y + 1], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x-1, currentNode.y + 1,time])
        validMovement = self.graph.checkValidMovement([currentNode.x+1, currentNode.y + 1], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x+1, currentNode.y + 1,time])

        validMovement = self.graph.checkValidMovement([currentNode.x - 1, currentNode.y], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x - 1, currentNode.y,time])

        validMovement = self.graph.checkValidMovement([currentNode.x + 1, currentNode.y], constraints, time)
        if validMovement:
            validNeighbours.append([currentNode.x + 1, currentNode.y,time])
        return validNeighbours


    #need to check if this is a dynamic buffer
    def addBufferConstraints(self,constraints):
        initialLengthOfConstraints = len(constraints.pathAsList[1])
        i = 0
        toAdd =[]
        while i < initialLengthOfConstraints:
            current = constraints.paths[1][i]
            toAdd+=(self.addBuffer(current, constraints.pathAsList[1]))#) the time here to be current.time -1
            i+=1
        #add time to toAdd
        return toAdd

    #things that need to be redone
    # ReservedAgents have to avoid each other
    # constraints should be the same for all agents
    def cBSWithBuffer(self,reservedAgents):
        aStarObj = aStar(self.graph)
        agents = self.agents
        constraints = [] # need these to be of type [x,y,t]
        for agent in reservedAgents:
            agents.remove(agent)
            paths =  aStarObj.findPath(constraints, agent,self.graphArea)
            paths = Paths({1:paths})
            #should add buffer area now
            paths.makePathAsList()
            toadd = self.addBufferConstraints(paths)
            constraints += paths.pathAsList[1]
            constraints += toadd
        cbsAlgo =highLevel(self.graph.graph,agents)
        #this need
        finalPaths = cbsAlgo.cbs(constraints)
        return

    def bufferPP(self,reservedAgents):
        aStarObj = aStar(self.graph)
        agents = self.agents
        constraints = [] # need these to be of type [x,y,t]
        for agent in reservedAgents:
            agents.remove(agent)
            paths = aStarObj.findPath(constraints, agent,self.graphArea)
            paths = Paths({1:paths})
            #should add buffer area now
            paths.makePathAsList()
            toadd = self.addBufferConstraints(paths)
            constraints += paths.pathAsList[1]
            constraints += toadd
        pp = prioritisedPlanning(self.graph,agents)
        finalPaths =pp.randomisedOrdering(constraints)
        return finalPaths