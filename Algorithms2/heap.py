class heap:

    def __init__(self):
        self.heapList = []

    def __len__(self):
        return len(self.heapList)

    def insert(self,i):
        self.heapList.append(i)
        self.satisfyHeap(len(self.heapList)-1)

    def children(self,j): # base 0 array
        a = j*2+1
        b = j*2+2
        if a > len(self.heapList)-1:
            return None, None
        if b > len(self.heapList)-1:
            return a, None
        return a, b

    def parent(self,j): # base 0 array
        if j == 0 : return 0
        return (j-1)//2

    def satisfyHeap(self,j): # base 0 array for entry j
        k = self.parent(j)
        while self.heapList[k]>self.heapList[j] and j > 0:            
            temp = self.heapList[k]
            self.heapList[k] = self.heapList[j]
            self.heapList[j] = temp
            j = k
            k = self.parent(j)

    def extract_min(self):
        if len(self.heapList) == 0 : return None
        minVal = self.heapList[0]
        if len(self.heapList) == 1:
            self.heapList.pop()
            return minVal
        self.heapList[0] = self.heapList.pop()
        currentRoot = 0
        while True:
            childA, childB = self.children(currentRoot)
            if childA != None:
                if childB != None:
                    if self.heapList[childA] < self.heapList[childB]:
                        smaller = childA
                    else:
                        smaller = childB
                    if self.heapList[currentRoot] > self.heapList[smaller]:
                        temp = self.heapList[smaller]
                        self.heapList[smaller] = self.heapList[currentRoot]
                        self.heapList[currentRoot] = temp
                        currentRoot = smaller
                    else:
                        return minVal
                elif self.heapList[currentRoot] > self.heapList[childA]:
                    smaller = childA
                    temp = self.heapList[smaller]
                    self.heapList[smaller] = self.heapList[currentRoot]
                    self.heapList[currentRoot] = temp
                    currentRoot = smaller
                else:
                    return minVal
            else:
                return minVal



class maxHeap:

    def __init__(self):
        self.heapList = []

    def __len__(self):
        return len(self.heapList)

    def insert(self,i):
        self.heapList.append(i)
        self.satisfyHeap(len(self.heapList)-1)

    def children(self,j): # base 0 array
        a = j*2+1
        b = j*2+2
        if a > len(self.heapList)-1:
            return None, None
        if b > len(self.heapList)-1:
            return a, None
        return a, b    

    def parent(self,j): # base 0 array
        if j == 0 : return 0
        return (j-1)//2

    def satisfyHeap(self,j): # base 0 array for entry j
        k = self.parent(j)
        while self.heapList[k]<self.heapList[j] and j > 0:            
            temp = self.heapList[k]
            self.heapList[k] = self.heapList[j]
            self.heapList[j] = temp
            j = k
            k = self.parent(j)

    def extract_max(self):
        if len(self.heapList) == 0 : return None
        maxVal = self.heapList[0]
        if len(self.heapList) == 1:
            self.heapList.pop()
            return maxVal
        self.heapList[0] = self.heapList.pop()
        currentRoot = 0
        while True:
            childA, childB = self.children(currentRoot)
            if childA != None:
                if childB != None:
                    if self.heapList[childA] > self.heapList[childB]:
                        larger = childA
                    else:
                        larger = childB
                    if self.heapList[currentRoot] < self.heapList[larger]:
                        temp = self.heapList[larger]
                        self.heapList[larger] = self.heapList[currentRoot]
                        self.heapList[currentRoot] = temp
                        currentRoot = larger
                    else:
                        return maxVal
                elif self.heapList[currentRoot] < self.heapList[childA]:
                    larger = childA
                    temp = self.heapList[larger]
                    self.heapList[larger] = self.heapList[currentRoot]
                    self.heapList[currentRoot] = temp
                    currentRoot = larger
                else:
                    return maxVal
            else:
                return maxVal


class medianHeaping():

    def __init__(self):
        self.leftHeap = maxHeap()
        self.rightHeap = heap()        
    
    def insert(self,j):
        leftMedian = self.leftHeap.extract_max()
        rightMedian = self.rightHeap.extract_min()        
        if leftMedian != None:
            if rightMedian != None:
                if j < rightMedian:
                    if (j >= leftMedian):
                        self.leftHeap.insert(leftMedian)    
                        temp = leftMedian
                        leftMedian = j
                        j = temp
                    else: self.leftHeap.insert(j)
                else:
                    self.rightHeap.insert(j)

                if len(self.leftHeap)<len(self.rightHeap):                    
                    self.leftHeap.insert(leftMedian)
                    self.leftHeap.insert(rightMedian)
                    
                elif len(self.leftHeap)-1>len(self.rightHeap):                    
                    self.rightHeap.insert(leftMedian)
                    self.rightHeap.insert(rightMedian)
                else:                    
                    self.leftHeap.insert(leftMedian)
                    self.rightHeap.insert(rightMedian)
                    
                median = self.leftHeap.heapList[0]

            else:
                if j < leftMedian:
                    self.leftHeap.insert(j)
                    self.rightHeap.insert(leftMedian)
                    median = j
                else:
                    self.leftHeap.insert(leftMedian)
                    self.rightHeap.insert(j)
                    median = leftMedian
        else:
            self.leftHeap.insert(j)
            median = j

        return median


def calculate_median_sums(srcFile):
    medianHeap = medianHeaping()
    fl = open(srcFile)
    heapSum = 0
    for line in fl:
        heapSum +=medianHeap.insert(int(line))
    return heapSum%10000