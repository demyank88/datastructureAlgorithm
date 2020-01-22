import sys

def selectionSort(arr):
    idx = 0
    while idx < len(arr):
        idx2 = 0
        targetIdx = idx
        minVal = arr[idx + idx2]
        while idx + idx2 < len(arr):
            tmp = arr[idx + idx2]
            if tmp < minVal:
                minVal = tmp
                targetIdx = idx + idx2
            idx2 += 1
        # tmp = arr[idx]
        # arr[idx] = arr[targetIdx]
        # arr[targetIdx] = tmp
        arr[idx], arr[targetIdx] = arr[targetIdx], arr[idx]
        idx += 1

if __name__ == '__main__':
    # Driver code to test above
    A = [64, 25, 12, 22, 11]
    selectionSort(A)
    print("Sorted array")
    print(*A, sep=' ')
