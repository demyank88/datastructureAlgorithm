# class node():
#     def __init__(self, v):
#         self.value = v
#         self.left = None

# def swapping(arr, node):

class heap():
    def __init__(self):
        self.arr = []
        self.length = 0

    def insert(self, v):
        self.arr.append(v)
        self.length += 1
        crtIdx = self.length - 1
        parentIdx = int((crtIdx - 1)/2)

        # root case
        if crtIdx == 0:
            return
        # checking whether swapping or not
        # swapping downTop wards
        while crtIdx != 0 and self.arr[parentIdx] < v:
            self.arr[parentIdx], self.arr[crtIdx] = self.arr[crtIdx], self.arr[parentIdx]
            crtIdx = parentIdx
            parentIdx = int((crtIdx - 1)/2)

    # heap remove from root as characteristic
    #
    def remove(self):
        crtIdx = 0
        self.arr[crtIdx], self.arr[self.length - 1] = self.arr[self.length - 1], self.arr[crtIdx]
        self.length -= 1

        #initialization
        leftIdx = 2*crtIdx + 1
        rightIdx = 2*crtIdx + 2
        crtValue = self.arr[crtIdx]
        leftValue = self.arr[leftIdx]
        rightValue = self.arr[rightIdx]

        if self.length == 1:
            return self.arr
        elif self.length < 3:
            if crtValue < leftValue:
                self.arr[crtIdx], self.arr[leftIdx] = leftValue, crtValue
                crtIdx = 2 * crtIdx + 1
            return self.arr

        # loop of swapping topDown wards
        while leftValue != None and rightValue != None and (crtValue < leftValue or crtValue < rightValue):
            if leftValue > rightValue:
                self.arr[crtIdx], self.arr[leftIdx] = leftValue, crtValue
                crtIdx = 2*crtIdx + 1
            else:
                self.arr[crtIdx], self.arr[rightIdx] = rightValue, crtValue
                crtIdx = 2 * crtIdx + 2
            leftIdx = 2 * crtIdx + 1 if 2 * crtIdx + 1 < self.length else None
            rightIdx = 2 * crtIdx + 2 if 2 * crtIdx + 2 < self.length else None
            crtValue = self.arr[crtIdx]
            leftValue = self.arr[leftIdx] if leftIdx != None and leftIdx < self.length else None
            rightValue = self.arr[rightIdx] if rightIdx != None and rightIdx < self.length else None

        return self.arr



def heapSort(arr):
    h = heap()
    for e in arr:
        h.insert(e)

    for _ in range(len(arr) - 1):
        arr = h.remove()
    return arr


if __name__ == '__main__':
    # Driver code to test above
    arr = [12, 11, 13, 5, 17, 6, 7, 32]
    arr = heapSort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i]),
        # This code is contributed by Mohit Kumra