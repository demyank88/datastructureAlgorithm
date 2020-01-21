import sys
# class Stack():
#

# Actually, Deque
class Queue():

    def __init__(self):
        self.q = []

    def put(self, v):
        self.q.append(v)

    def qsize(self):
        return len(self.q)

    def pull(self, n=0):
        return self.q.pop(n)

    def isEmpty(self):
        return len(self.q)

    def peek(self):
        return self.q[len(self.q) - 1]

def checkSorted(sz, q):

    if sz == 0:
        return True

    stack = []
    nQueue = Queue()
    while(q.isEmpty()):
        n = q.pull()
        if nQueue.isEmpty():
            if nQueue.peek() < n:
                nQueue.put(n)
            else:
                if len(stack) == 0:
                    stack.append(nQueue.pull())
                else:
                    # Check stack reverse order
                    if stack[len(stack) - 1] > nQueue.peek():
                        stack.append(nQueue.pull(nQueue.qsize() - 1))
                    else:
                        return False
        else:
            nQueue.put(n)
    return True

# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.put(7)
    q.put(1)
    q.put(2)
    q.put(6)
    q.put(3)
    q.put(4)

    n = q.qsize()

    if checkSorted(n, q):
        print("Yes")
    else:
        print("No")

        # This code is contributed by PranchalK