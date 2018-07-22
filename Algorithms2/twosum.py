
def readFile(srcFile):    
    fl = open(srcFile)
    dataSet = []    
    for line in fl:
        dataSet.append(int(line))
    return dataSet

def find_next_prime(n):
    i=n
    prime = True
    while True:
        prime = True
        for j in range(2,i):
            if i%j==0:
                prime = False
                break        
        if prime: return i
        i+=1

from bisect import bisect_left

def binary_search(a, x):
    hi = len(a)-1
    lo = 0
    if a[0] >= x: return 0
    if a[hi] <=x: return hi
    while lo <= hi:
        mid =  (hi + lo) //2
        if x <a[mid]:
            hi = mid - 1
        elif (x > a[mid]):
            lo = mid + 1
        else: return mid
    if (a[lo] - x < x - a[hi]): return lo
    else: return hi

def find_target_values(dataSet,minTarget=-10000,maxTarget=10000):   
    sums = {}
    dataSet.sort()
    for x in dataSet:
        y_low = minTarget-x
        y_high = maxTarget-x
        j_low = binary_search(dataSet,y_low)
        j_high = binary_search(dataSet,y_high)

        for j in range (j_low,j_high+1):
            if (dataSet[j_low] >= y_low and dataSet[j_high] <=y_high):
                sums[dataSet[j] + x] = 1
    return sums