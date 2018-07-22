import random as rand

def RSelect(A,i):    
    if len(A) == 1:
        return A[0]
    p = choosePivot(len(A))    
    swap(A,p,0) #pivot now at 0th position
    j= Partition(A,0,len(A)) #p now in position j, its proper position.
    if j+1 == (i):
        return A[j]
    elif j+1>i:
        return RSelect(A[:j],i)
    else:
        return RSelect(A[j+1:],i-(j+1))


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

def choosePivot(n):
    return rand.randint(0,n-1)
