
class Paths():
    def __init__(self, paths):
        self.paths = paths
        self.pathAsList = None
        self.pathWithoutTime = None

    def makePathAsList(self):
        pathAsList = {}
        withoutTime = {}
        for agent,path in self.paths.items():
            temp = []
            tempWithoutTime = []
            for step in path:
                temp.append([step.x, step.y, step.time])
                tempWithoutTime.append([step.x, step.y])
            pathAsList[agent] = temp
            withoutTime[agent] = tempWithoutTime
        self.pathAsList = pathAsList
        self.pathWithoutTime = withoutTime
        return pathAsList
