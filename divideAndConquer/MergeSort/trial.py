
def printList(arr):
    print(*arr, sep=' ')

#firstly, I tried to solve it using recursion.
def mergeSort(arr):
    length = len(arr)
    if length == 1:
        return arr
    middle = int(length/2)
    # I can't find the way to combine recursion without additional reference parameter
    # solving it using auxiliary array
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])
    tmp = []
    # i, j = 0, 0
    i = j = 0
    while i + j < len(left) + len(right):
        if i < len(left) and j < len(right) and left[i] < right[j]:
            tmp.append(left[i])
            i += 1
        elif i < len(left) and j >= len(right):
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    return tmp

if __name__ == '__main__':
    # driver code to test the above code
    if __name__ == '__main__':
        arr = [12, 11, 13, 5, 6, 7]
        print("Given array is", end="\n")
        printList(arr)
        arr = mergeSort(arr)
        print("Sorted array is: ", end="\n")
        printList(arr)