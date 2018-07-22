import numpy as np
import math

#merge subroutine naturally uncovers split inversions
#counting the sort
def Sort_and_Count(A, n):
    if n == 0: 
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        if (A[0]<=A[1]):
            return 0
        else:
            return 1
    else:
        x = Sort_and_Count(A[:n//2],n//2)
        y = Sort_and_Count(A[n//2:], n - n//2)
        z = Merge_and_CountSplitInv(A,n)
        print( x, y, z)
    return x + y + z


#runtime -> merge is linear over k loop
# count 1 more thing, so O(n) + O(n) ~ O(n)
def Merge_and_CountSplitInv(A,n):
    B = A[:n//2]
    C = A[n//2:]
    D = A
    z = 0
    i,j,k = 0,0,0
    if (n > 1):
        while i < n//2 and j < n//2:   
            if (B[i]<C[j]):
                D[k] = B[i]
                i+=1
            else:
                D[k] = C[j]
                j+=1
                z+= n//2-i
                #something copied, need to count B
            k+=1
        while i < n//2:
            D[k] = B[i]
            i+=1
            k+=1
        while j < n//2:
            D[k] = C[j]
            j+=1
            k+=1

        return z