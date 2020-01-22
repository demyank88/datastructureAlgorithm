
class Node():
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

def isLeaf(node):
    return not node.left and not node.right

def traverse(node, maxarr):
    if isLeaf(node):
        return node.value

    if node.right == None:
        return max(node.value, traverse(node.left, maxarr) + node.value)
    if node.left == None:
        return max(node.value, traverse(node.right, maxarr) + node.value)

    leftChild = traverse(node.left, maxarr)
    rightChild = traverse(node.right, maxarr)
    maxarr.append(max(node.value, leftChild + node.value, rightChild + node.value, leftChild + node.value + rightChild))

    return max(node.value, leftChild + node.value, rightChild + node.value)

def findMaxSum(node):

    if isLeaf(node):
        return node.value

    maxarr = [node.value]
    traverse(node, maxarr)
    return max(maxarr)


if __name__ == '__main__':
    # Driver program
    root = Node(10)
    root.left = Node(2)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(1)
    root.right.right = Node(-25)
    root.right.right.left = Node(3)
    root.right.right.right = Node(4)
    print("Max path sum is ", findMaxSum(root))
