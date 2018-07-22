import heapq

def build_schedule(src, scoreCalc):
    dataHeap = []
    file = open(src)
    jobCount = file.readline()
    for line in file:
        weight, length = map(int, line.split())
        dataHeap.append([-scoreCalc(weight,length),-weight,length])

    heapq.heapify(dataHeap)
    weightedCompletionSum = 0
    time = 0
    while len(dataHeap) > 0:
        job = heapq.heappop(dataHeap)
        time += job[2]
        weightedCompletionSum+=-job[1]*time

    return weightedCompletionSum
        


def difference(a,b):
    return a-b

def ratio(a,b):
    return a/b

def test(src):
    a = build_schedule(src,difference)
    b = build_schedule(src,ratio)
    print(a,b)