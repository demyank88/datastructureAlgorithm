
def insertionSort(arr):
    idx = 0
    while idx < len(arr) - 1:
        for idx2 in range(idx, -1, -1):
            nextIdx = idx + 1
            nextValue = arr[idx + 1]
            if arr[idx2] < nextValue:
                arr[idx2 + 1:nextIdx + 1] = [arr[nextIdx]] + arr[idx2 + 1:nextIdx]
                break
            else:
                continue
        else:
            arr[idx2:nextIdx + 1] = [arr[nextIdx]] + arr[idx2:nextIdx]
        idx += 1

if __name__ == '__main__':
    # Driver code to test above
    # arr = [12, 11, 13, 5, 6]
    arr = [1,2,3,4,5,10,12,6]
    insertionSort(arr)
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")