import random as rand

def DSelect(A,i):    
    if len(A) == 1:
        return A[0]
    p = choosePivotD(A)
    swap(A,p,0) #pivot now at 0th position
    j= Partition(A,0,len(A)) #p now in position j, its proper position.
    if j+1 == (i):
        return A[j]
    elif j+1>i:
        return DSelect(A[:j],i)
    else:
        return DSelect(A[j+1:],i-(j+1))

def Partition(A,l,r):    
    p=A[l]
    i=l+1
    for j in range(l+1,r):        
        if(A[j] < p):
            swap(A,i,j)
            i+=1
    swap(A,l,i-1)
    return i-1

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def choosePivotD(A):#median of medians pivoting
    n = len(A)//5
    i = 0
    C = []
    return i

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