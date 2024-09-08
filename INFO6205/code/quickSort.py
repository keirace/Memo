def partition(A, low, high):
    pivot = A[high]  # last index
    i = low - 1
    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            print(i, j, A[i], A[j])
            (A[i], A[j]) = (A[j], A[i])
    (A[i+1], A[high]) = (A[high], A[i+1])
    return i+1 # get index of partition

def quickSort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        print("pi = ", pi)
        quickSort(A, low, pi - 1)
        quickSort(A, pi + 1, high)

arr = [0,4,9,2,1,-2,-6]
arr = [i * i for i in arr]
quickSort(arr, 0, len(arr) - 1)
print(arr)
