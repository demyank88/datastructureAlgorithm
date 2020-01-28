from collections import defaultdict

class Node():
    def __init__(self, v):
        self.v = v
        self.next = None

class Graph():
    def __init__(self):
        self.adjnode = None
        self.visit: False
        self.nodes = dict()

    def addEdge(self, origin, next):
        if origin not in self.nodes:
            self.nodes[origin] = Node(origin)
        else:
            crtNode = self.nodes[origin]
            while crtNode.next:
                crtNode = crtNode.next
            else:
                crtNode.next = Node(next)


# if node exist having 1, but another node having 1 create.
# manage key value pairs of nodes in graph dict
# managing each node's linkedlist which is created newly on each start node


if __name__ == '__main__':
    # Driver code

    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    # g.BFS(2)