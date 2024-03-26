import time
from src.reservedArea.reservedAreasStatic import reservedAreasStatic
from src.reservedArea.reservedAreaBuffer import reservedAreaBufferArea
from src.cbs.cbs import highLevel
from src.pp.prioritised import prioritisedPlanning


#Something that needs to be added to this is a check if a valid response is generated
class ReservedAreasExperiments:
    def classicCBS(self,agents,graph):
        algo = highLevel(graph, agents)
        start = time.time()
        a =algo.cbs()
        if a is False:
            print(False)
        end = time.time()
        return end - start

    def classicPP(self, agents,graph):
        p = prioritisedPlanning(graph, agents)
        start = time.time()
        val = p.randomisedOrdering()
        end = time.time()
        return end - start


    def staticRaCBSV1(self,agents,graph,numreservedAgents):
        obja = reservedAreasStatic(graph, agents)
        start = time.time()
        paths = obja.reservedAreaDeciderVersionOne(numreservedAgents)
        end = time.time()
        return end - start

    def staticRaCBSV1_1(self,agents,graph,numreservedAgents):
        obja = reservedAreasStatic(graph, agents)
        start = time.time()
        paths = obja.reservedAreaDeciderVersionOne2(numreservedAgents)
        end = time.time()
        return end - start

    def staticRaCBSV2(self,agents,graph,numreservedAgents):
        obja = reservedAreasStatic(graph, agents)
        start = time.time()
        paths = obja.reservedAreaDeciderVersionTwo(numreservedAgents)
        end = time.time()
        return end - start

    def bufferRaCBS(self,agents,graph,reservedAgents):
        obja = reservedAreaBufferArea(graph,agents)
        start = time.time()
        paths = obja.dynamicCBSWithBuffer(reservedAgents)
        end = time.time()
        return end - start
    """
    def bufferRaPP(self,reservedAgents):
        obja = reservedAreasStatic(self.graph, self.agents)
        start = time.time()
        obja.staticPP(reservedAgents)
        end = time.time()
        return end - start
    """
if __name__ == '__main__':
    print("a")