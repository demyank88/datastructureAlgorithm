

class Node():
    def __init__(self, v):
        self.v = v
        self.adjEdges = []
        self.weights = []

class Graph():
    def __init__(self, vcnt):
        self.vcnt = vcnt
        # self.

    def addEdge(self, start, end, weight):

        newNode = Node(start)

        pass

if __name__ == '__main__':
    # Driver code
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.KruskalMST()