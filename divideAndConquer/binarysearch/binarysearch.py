

def binarySearch(arr, l, r, x):
    mIdx = int((l + r)/2)
    mValue = arr[mIdx]
    if mValue == x:
        return mIdx
    elif l > r:
        return -1
    if mValue < x:
        # binarySearch(arr[mIdx+1:],mIdx+1, r, x)
        return binarySearch(arr, mIdx+1, r, x)
    else:
        # binarySearch(arr[:mIdx], l, mIdx - 1, x)
        return binarySearch(arr, l, mIdx - 1, x)


if __name__ == '__main__':
    # Driver Code
    arr = [2, 3, 4, 10, 40]
    x = 11

    # Function call
    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")