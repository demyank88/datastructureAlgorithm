
def bubbleSort(arr):

    i = len(arr) - 1
    while i > 0:
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i -= 1

if __name__ == '__main__':
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubbleSort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")