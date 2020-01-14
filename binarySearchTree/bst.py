class node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class bst():
    def __init__(self):
        self.root = None

    def insert(self, k, v):
        newNode = node(k, v)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            parent = None

            while True:
                parent = current
                if k < current.key:
                    current = current.left
                    # It's parent is the leaf node
                    if current == None:
                        parent.left = newNode
                        return
                else:
                    current = current.right
                    if current == None:
                        parent.right = newNode
                        return
    def findMin(self):
        current = self.root
        last = None
        while current != None:
            last = current
            current = current.left
        return last

    def findMax(self):
        current = self.root
        last = None
        while current != None:
            last = current
            current = current.right
        return last

if __name__ == '__main__':
    tree = bst()

    tree.insert(10, "Ten")
    tree.insert(20, "Twenty")
    tree.insert(15, "fifteen")

    print(tree.findMin().key)
    print(tree.findMax().key)