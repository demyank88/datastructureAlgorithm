class Graph():
    def __init__(self, vCount):
        self.vCount = vCount
        self.eCount = 0
        self.adjacent = [0] * vCount

    def getVerticeCnt(self):
        return self.vCount

    def getEdgeCnt(self):
        return self.eCount

    def addEdge(self, pos, dest):
        self.adjacent[pos].append(dest)
        self.eCount += 1

    def adj(self, pos):
        return self.adjacent[pos]