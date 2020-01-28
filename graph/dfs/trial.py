from collections import defaultdict

class Graph():
    def __init__(self):
        self.vertexs = defaultdict(list)

    def addEdge(self, k, v):
        if self.vertexs[k]:
            self.vertexs[k].append(v)
        else:
            self.vertexs[k].append(k)
            if v not in self.vertexs[k]:
                self.vertexs[k].append(v)

    def DFS(self, start):
        visitQueue = [False] * len(self.vertexs)
        self.recurtion(start, visitQueue)

    # recursion is stack
    def recurtion(self, vertex, visitQueue):
        if visitQueue[vertex]:
            return
        crtVertex = vertex
        print(vertex, end=' ')
        visitQueue[vertex] = True
        # check unvisited adjacent vertex
        adjArr = self.vertexs[crtVertex]
        for newVertex in adjArr:
            self.recurtion(newVertex, visitQueue)

if __name__ == '__main__':
    # Driver code

    # Create a graph given
    # in the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)