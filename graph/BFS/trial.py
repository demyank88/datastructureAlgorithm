from collections import defaultdict

class Node():
    def __init__(self, v):
        self.v = v
        self.next = None

class Graph():
    def __init__(self):
        self.adjnode = None
        self.vertexs = dict()
        self.cq = []
        self.visit = dict()


    def addEdge(self, origin, next):
        if origin not in self.vertexs:
            self.vertexs[origin] = Node(origin)
            self.vertexs[origin].next = Node(next)
            self.visit[origin] = False
        else:
            crtNode = self.vertexs[origin]
            while crtNode.next:
                crtNode = crtNode.next
            else:
                crtNode.next = Node(next)

    def BFS(self, start):
        self.cq.append(self.vertexs[start].v)

        while len(self.cq):
            crtVertex = self.vertexs[self.cq.pop(0)]
            if not self.visit[crtVertex.v]:
                print(crtVertex.v, end=' ')
                self.visit[crtVertex.v] = True
            while crtVertex.next:
                if self.visit[crtVertex.v]:
                    crtVertex = crtVertex.next
                    continue
                if not self.visit[crtVertex.v]:
                    self.cq.append(crtVertex.v)
                print(crtVertex.v, end=' ')
                self.visit[crtVertex.v] = True
                crtVertex = crtVertex.next
            else:
                if not self.visit[crtVertex.v]:
                    self.cq.append(crtVertex.v)
                    print(crtVertex.v, end=' ')
                    self.visit[crtVertex.v] = True



# if node exist having 1, but another node having 1 create.
# manage key value pairs of vertexs in graph dict
# managing each node's linkedlist which is created newly on each start node


if __name__ == '__main__':
    # Driver code

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    # g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.BFS(2)