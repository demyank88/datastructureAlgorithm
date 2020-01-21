import sys

class Queue():

    def __init__(self):
        self.q = []

    def put(self, v):
        self.q.append(v)

    def qsize(self):
        return len(self.q)

    def pull(self):
        return self.q.pop(0)

    def isEmpty(self):
        return len(self.q)

def checkSorted(sz, q):

    stack = []
    while(not q.isEmpty()):
        n = q.pull()

        pass


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.put(5)
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)

    n = q.qsize()

    if checkSorted(n, q):
        print("Yes")
    else:
        print("No")

        # This code is contributed by PranchalK