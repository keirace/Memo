def bubble_sort(list_):
    n = len(list_)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_[j] > list_[j + 1]:
                list_[j], list_[j + 1] = list_[j + 1], list_[j]

def insertion_sort(list_):
    for i in range(1, len(list_)):
        key = list_[i]
        j = i - 1
        while j >= 0 and key < list_[j]:
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key

def selection_sort(list_):
    for i in range(len(list_)):
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j
        list_[i], list_[min_index] = list_[min_index], list_[i]

def merge_sort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2
        left_half = list_[:mid]
        right_half = list_[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_[k] = left_half[i]
                i += 1
            else:
                list_[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list_[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list_[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(list_):
    if len(list_) <= 1:
        return list_
    pivot = list_[0]
    less = [x for x in list_[1:] if x < pivot]
    greater = [x for x in list_[1:] if x >= pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

def heapify(list_, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and list_[i] < list_[left]:
        largest = left
    if right < n and list_[largest] < list_[right]:
        largest = right
    if largest != i:
        list_[i], list_[largest] = list_[largest], list_[i]
        heapify(list_, n, largest)

def heap_sort(list_):
    n = len(list_)
    for i in range(n // 2 - 1, -1, -1):
        heapify(list_, n, i)
    for i in range(n - 1, 0, -1):
        list_[i], list_[0] = list_[0], list_[i]
        heapify(list_, i, 0)

import random

def quickselect(nums, k):
    if len(nums) == 1:
        return nums[0]
    
    pivot = random.choice(nums)
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    
    if k <= len(left):
        return quickselect(left, k)
    elif k <= len(left) + len(mid):
        return mid[0]
    else:
        return quickselect(right, k - len(left) - len(mid))
    

arr = [3, 6, 8, 10, 1, 2, 1]
arr_copy = arr.copy()
merge_sort(arr_copy)
print("Sorted array using merge sort:", arr_copy)
quick_sort_result = quick_sort(arr)
print("Sorted array using quick sort:", quick_sort_result)
quickselect_result = quickselect(arr, 4)  # Find the 4th smallest element
print(f"The 4th smallest element is: {quickselect_result}")