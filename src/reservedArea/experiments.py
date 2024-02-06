import time
from src.reservedArea.reservedAreas import reservedAreasStatic
from src.cbs.cbs import highLevel
from src.pp.prioritised import prioritisedPlanning


#Something that needs to be added to this is a check if a valid response is generated
class ReservedAreasExperiments:
    def __init__(self,graph,agents):
        self.graph = graph
        self.agents = agents

    def classicCBS(self):
        algo = highLevel(self.graph, self.agents)
        start = time.time()
        algo.cbs()
        end = time.time()
        return end - start

    def classicPP(self):
        p = prioritisedPlanning(self.graph, self.agents)
        start = time.time()
        val = p.randomisedOrdering()
        end = time.time()
        return end - start

    def staticRaPP(self,reservedAgents):
        obja = reservedAreasStatic(self.graph, self.agents)
        start = time.time()
        obja.staticPP(reservedAgents)
        end = time.time()
        return end - start

    def staticRaCBS(self,reservedAgents):
        obja = reservedAreasStatic(self.graph, self.agents)
        start = time.time()
        obja.staticCBS(reservedAgents)
        end = time.time()
        return end - start

    def dynamicRaPP(self,reservedAgents):
        obja = reservedAreasStatic(self.graph, self.agents)
        start = time.time()
        obja.staticPP(reservedAgents)
        end = time.time()
        return end - start

    def dynamicRaCBS(self,reservedAgents):
        obja = reservedAreasStatic(self.graph, self.agents)
        start = time.time()
        obja.staticCBS(reservedAgents)
        end = time.time()
        return end - start

if __name__ == '__main__':
    #