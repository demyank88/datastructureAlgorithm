
def quickSort(arr, low, high):
    if high - low < 2:
        if arr[high] < arr[low]:
            arr[high], arr[low] = arr[low], arr[high]
        return
    pivot = arr[high]
    sIdx = 0
    idx = 0
    while low + idx < high:
        if arr[low + idx] < pivot:
            arr[low + sIdx], arr[low + idx] = arr[low + idx], arr[low + sIdx]
            sIdx += 1
        idx += 1
    arr[low + sIdx], arr[high] = arr[high], arr[low + sIdx]
    quickSort(arr, low, low + sIdx)
    quickSort(arr, low + sIdx + 1, high)

if __name__ == '__main__':
    # Driver code to test above
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i]),

        # This code is contributed by Mohit Kumra