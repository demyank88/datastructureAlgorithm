import sys
class Node():
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.visit = False

def isLeaf(node):
    return not node.left and not node.right

def traverse(node, h, mh):
    h = h + 1
    if isLeaf(node):
        node.visit = True
        return min(mh, h)

    if node.left and not node.left.visit:
        mh = min(traverse(node.left, h, mh), mh)
    if node.right and not node.right.visit:
        mh = min(traverse(node.right, h, mh), mh)
    node.visit = True
    return mh


def minDepth(root):
    if isLeaf(root):
        return 1
    return traverse(root, 0, sys.maxsize)

if __name__ == '__main__':
    # Driver Program
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(4)
    root.left.left.left = Node(1)
    root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    print(minDepth(root))