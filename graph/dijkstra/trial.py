import sys
import operator

class Graph():
    def __init__(self, cnt):
        self.cnt = cnt
        self.graph = None
        self.spt = []
        self.adjDistances = [0] + [sys.maxsize] * (cnt - 1)

    def dijkstra(self, start):
        culShortest = 0
        self.spt.append(start)
        for idx in range(self.cnt):
            arr = [x if x != 0 else sys.maxsize for x in self.graph[idx]]
            # selected node sequence
            # shorted distance integer
            #
            idx, minVal = min(enumerate(arr), key=lambda x: x[1])
            # idx, minVal = min(enumerate(arr), key=operator.itemgetter(1))
            print(idx, minVal)
            self.spt.append(idx)
            self.dijkstra(1)
            pass


if __name__ == '__main__':
    # Driver program
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)