'''--------------------Bubble Sort--------------------'''
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i - 1
        key = nums[i]
        while nums[j] > key and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

# arr = [12, 11, 13, 5, 6]
# print(insertion_sort(arr))
'''--------------------------------------------------'''

'''--------------------Bubble Sort--------------------'''
def bubble_sort(nums):
    for i in range(0, len(nums)):
        sorted = True
        for j in range(0, len(nums) - 1):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                sorted = False
        if sorted == True:
            return nums

# arr = [12, 11, 13, 5, 6]
# print(bubble_sort(arr))
'''--------------------------------------------------'''

'''--------------------Quick Sort--------------------'''
def partition(start, end, arr):
    pivot_index = start
    pivot_val = arr[start]
    while start < end:
        while arr[start] <= pivot_val:
            start += 1
        while arr[end] > pivot_val:
            end -= 1
        if start < end: 
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
    temp2 = arr[pivot_index]
    arr[pivot_index] = arr[end]
    arr[end] = temp2
    return end 
    
def quick_sort(start, end, arr):
    if start < end:
        pivot = partition(start, end, arr)
        quick_sort(start, pivot - 1, arr)
        quick_sort(pivot + 1, end, arr)
    return arr

arr = [12, 11, 13, 5, 6]
print(quick_sort(0, 4, arr))

'''--------------------------------------------------'''