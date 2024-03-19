
class partitionExtension:
    def __init__(self):
        self.minX = None
        self.minY = None
        self.maxX = None
        self.maxY = None
        self.pathsToIncorporate = []

    def addPathToContension(self,path, minX,maxX, minY, maxY):
        if self.minX is None or self.minX > minX:
            self.minX = minX
        if self.minY is None or self.minY > minY:
            self.minY = minY
        if self.maxX is None or self.maxX < maxX:
            self.maxX = maxX
        if self.maxY is None or self.maxY < maxY:
            self.maxY = maxY
        self.pathsToIncorporate.append(path)