class agent:
    def __init__(self, agentId,goal,startPos):
        self.agentId = agentId
        self.startPos = startPos
        self.goal = goal


    def __eq__(self, other):
        if self.agentId == other.agentId:
            return True
        return False

    def __hash__(self):
        return hash(self.agentId)

    