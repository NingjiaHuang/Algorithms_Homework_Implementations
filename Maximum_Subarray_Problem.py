'''
Maximum Subarray Problem: find a contiguous subarray with the largest sum in a given array. This implementation uses the divide
and conquer technique to reduce the runtime to Theta(nlogn). 
'''
import math
def find_max_crossing_subarray(arr, low, mid, high):
    left_sum = -math.inf
    max_left = mid
    sum = 0 
# Reverse the decrement by using -1.
    for i in range(mid, low - 1, -1): 
        sum = sum + arr[i]
        if(sum > left_sum): 
            left_sum = sum
            max_left = i
    right_sum = -math.inf
    max_right = mid + 1
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + arr[j]
        if(sum > right_sum): 
            right_sum = sum
            max_right = j
    return (max_left, max_right, left_sum + right_sum)

#find maximum subarray by returning the start_index, end_index, and maximum sum
def find_max_subarray(arr, low, high):
    if low == high: 
        return (low, high, arr[low])
    else: 
        mid = (low + high)//2
        (left_low, left_high, left_sum) = find_max_subarray(arr, low, mid)
        (right_low, right_high, right_sum) = find_max_subarray(arr, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum: 
            return (left_low, left_high, left_sum)
        elif right_sum > left_sum and right_sum >= cross_sum: 
            return (right_low, right_high, right_sum)
        else: 
            return (cross_low, cross_high, cross_sum)

#Test
arr = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
arr2 = [-1, -2, -3, -4, -5]
#print(find_max_subarray(arr, 0, 15))
print(find_max_subarray(arr2, 0, 4))