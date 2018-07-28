import sys

def readData(src):
    items = []
    fl = open(src)
    W, n = map(int, fl.readline().split())
    for line in fl:
        v,w = map(int, line.split())
        items.append([v,w])
    return items, W

def knapsack(items, W):
    n = len(items)-1    
    A = {}
    return knapsack_val(items, A, n, W)

def knapsack_val(items, A, i, w):    
    
    if (i,w) in A:
        return A[(i,w)]
    
    value = items[i][0]
    weight = items[i][1]
    if i == 0:
        val = 0
    elif weight <= w:
        val = max(knapsack_val(items, A, i-1, w-weight) +value, knapsack_val(items, A, i-1, w))
    else:
        val = knapsack_val(items, A, i-1, w)

    A[(i,w)] = val
    return val

def run_test(src):
    items, W = readData(src)
    maxVal = knapsack(items, W)
    return maxVal