import sys

def Find_Max_Subarray(A,low,high):
    left_low = 0
    left_high = 0
    left_sum = 0
    right_low = 0
    right_high = 0
    right_sum = 0
    cross_low = 0
    cross_high = 0
    cross_sum = 0
    if high == low:
        return (low,high,A[low])
    else:
        mid = (low + high)//2
        left_low, left_high, left_sum = Find_Max_Subarray(A,low,mid)
        right_low,right_high,right_sum = Find_Max_Subarray(A,mid+1,high)
        cross_low, cross_high, cross_sum = Find_Max_Crossing_Subarray(A,low,mid,high)
        if (left_sum >= right_sum and left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum>= left_sum and right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def Find_Max_Crossing_Subarray(A,low,mid,high):
    left_sum = -sys.maxsize
    max_left = mid
    allsum = 0
    for i in range(mid,low-1,-1):
        allsum+=A[i]
        if allsum > left_sum:
            left_sum = allsum
            max_left = i
    right_sum = -sys.maxsize
    max_right = mid+1
    allsum = 0
    for j in range (mid+1,high):
        allsum+=A[j]
        if allsum > right_sum:
            right_sum = allsum
            max_right = j
    return (max_left, max_right, left_sum+right_sum)
