from collections import Counter

def isSubset(arr1, arr2, m, n):

    arr1Cnt = Counter(arr1)
    arr2Cnt = Counter(arr2)

    tmp = arr2Cnt - arr1Cnt

    return len(tmp) == 0

# Driver code
if __name__ == "__main__":

    # arr1 = [11, 1, 13, 21, 3, 7]
    # arr2 = [11, 3, 7, 1]
    # arr1 = [10, 5, 2, 23, 19]
    # arr2 = [19, 5, 3]
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = [1, 2, 4]

    m = len(arr1)
    n = len(arr2)

    if (isSubset(arr1, arr2, m, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[]")

        # This code is contributed by ita_c