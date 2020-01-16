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
    def findMin(self, node):
        current = node
        last = None
        while current != None:
            last = current
            current = current.left
        return last

    def findMax(self, node):
        current = node
        last = None
        while current != None:
            last = current
            current = current.right
        return last

    def delete(self, key):
        parent = None
        current = self.root

        while current != None:

            # match case
            if current.key == key:
                parentChild = None
                if parent.right != None and parent.right.key == current.key:
                    parentChild = parent.right
                else:
                    parentChild = parent.left

                # leaf node
                if current.left == None and current.right == None:
                    # remove current node from parent
                    # This doesn't change parent.left or parent.right to None, but only parentChild to None
                    parentChild = None


                # one child node
                if current.left == None:
                    parentChild = current.right
                elif current.right == None:
                    parentChild = current.left
                # two child node
                # overview picture give some guide
                else:
                    candidate = self.findMax(current.right)
                    self.delete(candidate.key)
                    parentChild = candidate
                    candidate.right = current.right

                return True

            # traversing
            parent = current
            if key > current.key:
                current = current.right
            elif key < current.key:
                current = current.left

        return False

if __name__ == '__main__':
    tree = bst()

    tree.insert(10, "Ten")
    tree.insert(20, "Twenty")
    tree.insert(15, "fifteen")

    print(tree.findMin(tree.root).key)
    print(tree.findMax(tree.root).key)
    tree.delete(15)