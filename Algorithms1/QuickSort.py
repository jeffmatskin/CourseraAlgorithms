def QuickSort(A,l,r):    
    if l>=r:
        return 0
    i = choosePivotR(A,l,r)    
    swap(A,i,l)
    j= Partition(A,l,r) # new pivot position
    counter = r-l
    counter += QuickSort(A,l,j-1)
    counter += QuickSort(A,j+1,r)
    return counter

def Partition(A,l,r):    
    p=A[l]
    i=l+1
    for j in range(l+1,r+1):        
        if(A[j] < p):
            swap(A,i,j)
            i+=1
    swap(A,l,i-1)
    return i-1

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def choosePivotL(A,l,r):
    return l

def choosePivotR(A,l,r):
    return r

def choosePivotM(A,l,r):
    front = A[l]
    end = A[r]
    midpt= (r+l)//2
    mid = A[midpt]
    B = [front,mid,end]    
    
    if (front == min(B)):
        if (mid == max(B)):
            return r
        else: return midpt
    elif(mid == min(B)):
        if (front == max(B)):
            return r
        else: return l
    else:
        if(front == max(B)):
            return midpt
        else: return l    

A=[]
f = open("IntegerArray.txt")
for line in f:
    A.append(int(line))

#A=[11,18,5,20,8,10,3,2,17,4,13,7,12,9,6,16,19,15,1,14]
counter = QuickSort(A,0,len(A)-1)
print(counter)
