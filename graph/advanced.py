class node():
    def __init__(self, idx, node):
        self.vertexIdx = idx
        self.next = node

class vertex():
    def __init__(self, name, node):
        self.name = name
        self.adjList = node

class graph():
    def __init__(self, vCount, type):
        self.arrOfVertex = [None] * vCount
        self.idxCnt = 0
        self.undirected = True
        if type == 'directed':
            self.undirected = False

    def addVertex(self, vName):
        v = vertex(vName, None)
        self.arrOfVertex[self.idxCnt] = v
        self.idxCnt += 1

    def addEdge(self, srcVName, destVName):
        v1Idx = self.idxForName(srcVName)
        v2Idx = self.idxForName(destVName)
        self.arrOfVertex[v1Idx].adjList = node(v2Idx, self.arrOfVertex[v1Idx].adjList)
        if self.undirected:
            self.arrOfVertex[v2Idx].adjList = node(v1Idx, self.arrOfVertex[v2Idx].adjList)


    def idxForName(self, name):
        for i in range(len(self.arrOfVertex)):
            if self.arrOfVertex[i].name == name:
                return i
        return -1

    def print(self):
        for i in range(len(self.arrOfVertex)):
            print(self.arrOfVertex[i].name)
            while self.arrOfVertex[i].adjList != None:
                aNode = self.arrOfVertex[i].adjList
                print(f' --> {self.arrOfVertex[aNode.vertexIdx].name}')
                self.arrOfVertex[i].adjList = aNode.next
            print()

if __name__ == '__main__':
    myGraph = graph(5, 'directed')
    myGraph.addVertex("State")
    myGraph.addVertex("Avenel")
    myGraph.addVertex("Elm")
    myGraph.addVertex("Pocono")
    myGraph.addVertex("William")

    myGraph.addEdge('Avenel', 'Pocono')
    myGraph.addEdge("State", "Elm")
    myGraph.addEdge("Elm", "Avenel")
    myGraph.addEdge("Elm", "William")
    myGraph.addEdge("William", "State")
    myGraph.addEdge("William", "Pocono")
    myGraph.addEdge("Pocono", "Elm")
    myGraph.addEdge("State", "Avenel")

    myGraph.print()