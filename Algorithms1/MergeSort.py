import numpy as np
import math

#merge subroutine naturally uncovers split inversions
#counting the sort


#runtime -> merge is linear over k loop
# count 1 more thing, so O(n) + O(n) ~ O(n)
def mergeSort(A):
    n=len(A)
    if n>1:
        B = A[:n//2]
        C = A[n//2:]

        mergeSort(B)
        mergeSort(C)

        i,j,k = 0,0,0
        while i<len(B) and j<len(C):
            if B[i] < C[j]:
                A[k]=B[i]
                i+=1
            else:
                A[k]=C[j]
                j+=1
            k+=1
        
        while i < len(B):
            A[k]=B[i]
            i+=1
            k+=1
        
        while j < len(C):
            A[k]=C[j]
            j+=1
            k+=1
    return A