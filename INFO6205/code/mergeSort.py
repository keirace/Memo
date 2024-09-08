def mergeSort(A, lowerBound, upperBound):
    if lowerBound == upperBound:
        return 
    else:
        mid = (lowerBound + upperBound) // 2
        mergeSort(A, lowerBound, mid)  # sort left
        mergeSort(A, mid + 1, upperBound)  # sort right
        merge(A, lowerBound, mid + 1, upperBound)


def merge(A, lower, r, upper):
    temp = A
    start = lower
    mid = r - 1
    j = 0  # index of temp array
    while (lower <= mid) and (r <= upper):
        if A[lower] < A[r]:
            temp[j] = A[lower]
            lower += 1
        else:
            temp[j] = A[r]
            r += 1
        j += 1
    # copy the rest
    while lower <= mid:
        temp[j] = A[lower]
        j += 1
        lower += 1
    while r <= upper:
        temp[j] = A[r]
        j += 1
        r += 1
    # copy all items from temp back to A
    n = upper - start + 1
    for j in range(n):
        A[start+j] = temp[j]


arr = [15, -4, 0, 1, -3]
mergeSort(arr, 0, len(arr)-1)
print(arr)
