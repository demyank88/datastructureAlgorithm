class node():
    def __init__(self, key):
        self.key = key

    def getKey(self):
        return self.key

# max heap
class heap():
    def __init__(self, size):
        self.hArr = [None] * size
        self.arrSize = size # size of arr
        self.crtCnt = 0 # num of arr

    def getSize(self):
        return self.crtCnt

    def isEmpty(self):
        return self.crtCnt == 0

    def insert(self, key):
        if self.crtCnt == self.arrSize:
            return False

        newNode = node(key)
        self.hArr[self.crtCnt] = newNode
        self.trickleUp(self.crtCnt)
        self.crtCnt += 1
        return True

    def trickleUp(self, idx):
        parentIdx = int((idx - 1) / 2)
        nodeToInsert = self.hArr[idx]

        # loop as long as we haven't reached the root and key of idx's parent is less than new node
        while idx > 0 and self.hArr[parentIdx].getKey() < nodeToInsert.getKey():
            # move parent down
            self.hArr[idx] = self.hArr[parentIdx]
            idx = parentIdx
            parentIdx = int((parentIdx - 1)/2)

        self.hArr[idx] = nodeToInsert

    def remove(self):
        root = self.hArr[0]
        self.trickleDown()

        return root

    def trickleDown(self):
        lastNode = self.hArr.pop(self.crtCnt - 1)
        self.crtCnt -= 1
        crtIdx = 0
        self.hArr[crtIdx] = lastNode
        crt = self.hArr[crtIdx]


        # loop as long as heap structed properly
        # (left.getKey() != None and right.getKey() != None)
        # Checking condition Variates depends on how implement it is
        # Need insight of height
        while crtIdx < self.arrSize:
            left = self.hArr[2 * crtIdx + 1] if 2 * crtIdx + 1 < len(self.hArr) else None
            right = self.hArr[2 * crtIdx + 2] if 2 * crtIdx + 2 < len(self.hArr) else None

            if right != None and (left.getKey() > crt.getKey() or right.getKey() > crt.getKey()):
                if left.getKey() >= right.getKey():
                    tmp = self.hArr[crtIdx]
                    self.hArr[crtIdx] = self.hArr[2*crtIdx + 1]
                    self.hArr[2*crtIdx + 1] = tmp
                    crtIdx = 2*crtIdx + 1
                else:
                    tmp = self.hArr[crtIdx]
                    self.hArr[crtIdx] = self.hArr[2*crtIdx + 2]
                    self.hArr[2 * crtIdx + 2] = tmp
                    crtIdx = 2 * crtIdx + 2
            elif left != None and left.getKey() > crt.getKey():
                tmp = self.hArr[crtIdx]
                self.hArr[crtIdx] = self.hArr[2 * crtIdx + 1]
                self.hArr[2 * crtIdx + 1] = tmp
                crtIdx = 2 * crtIdx + 1
            else:
                break

            # if






if __name__ == '__main__':
    newHeap = heap(7)
    newHeap.insert(12)
    newHeap.insert(42)
    newHeap.insert(35)
    newHeap.insert(16)
    newHeap.insert(88)
    newHeap.insert(42)
    newHeap.insert(7)

    newHeap.remove()
    newHeap.remove()
    pass