import numpy as np
import math

#merge subroutine naturally uncovers split inversions
#counting the sort
def Sort_Pair(C,D):
    if len(C) > len(D):
        return C,D
    else:
        return D,C

def Merge_Count(A,B):
    inversions = 0
    result = []
    iA = 0
    iB = 0
    while len(A)>iA and len(B) > iB:
        if (A[iA] <= B[iB]):
            result.append(A[iA])
            iA+=1
        else:
            inversions+= len(A) - iA
            result.append(B[iB])
            iB+=1
    if (len(A) == iA):
        result += B[iB:]
    elif(len(B) == iB):
        result += A[iA:]
    return result, inversions

def sort(A):
    length = len(A)
    mid = length//2
    if length >=2:
        sorted_0, count_0 = sort(A[:mid])
        sorted_1, count_1 = sort(A[mid:])
        results, counts = Merge_Count(sorted_0, sorted_1)
        return results, counts + count_0 + count_1
    else:
         return A, 0

def count_inversions(a):
    final_array, inversions = sort(a)
    return inversions