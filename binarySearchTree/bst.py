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
        parent = self.root
        current = self.root
        isLeft = True
        while current != None:

            # match case
            if current.key == key:
                # leaf node
                if current.left == None and current.right == None:
                    # remove current node from parent
                    if self.root == key:
                        self.root = None
                    elif isLeft:
                        parent.left = None
                    else:
                        parent.right = None
                    return True

                # one child node
                if current.left == None:
                    if isLeft:
                        parent.left = current.right
                    else:
                        parent.right = current.right
                    return True
                elif current.right == None:
                    if isLeft:
                        parent.left = current.left
                    else:
                        parent.right = current.left
                    return True
                # two child node
                # overview picture give some guide
                else:
                    candidate = self.findMax(current.right)
                    isParentLeft = isLeft
                    isLeft = False
                    self.delete(candidate.key)
                    if isParentLeft:
                        candidate.left = current.left
                        parent.left = candidate
                    else:
                        candidate.left = current.left
                        parent.right = candidate
                    # candidate.right = current.right
                    return True

                return True

            # traversing
            parent = current
            if key > current.key:
                isLeft = False
                current = current.right
            elif key < current.key:
                isLeft = True
                current = current.left

        return False

if __name__ == '__main__':
    tree = bst()


    tree.insert(10, "Ten")
    tree.insert(20, "Twenty")
    tree.insert(15, "fifteen")
    tree.insert(25, "TwentyFive")
    tree.insert(30, "Thirty")
    tree.insert(5, "Five")
    tree.insert(8, "Eight")
    tree.insert(1, "One")


    print(tree.findMin(tree.root).key)
    print(tree.findMax(tree.root).key)
    tree.delete(5)