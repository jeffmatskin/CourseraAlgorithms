#have weights with first index set to 0
def max_weights(weights):
    A = [0]*len(weights)
    A[0] = 0
    A[1] = weights[1]
    for i in range(2,len(weights)):
        A[i] = max(A[i-1],A[i-2]+weights[i])
    return A

def read_weights(src):
    weights = [0]
    file = open(src)
    n = file.readline()
    for line in file:
        weights.append(int(line))
    return weights


def max_subset(weights):
    A = max_weights(weights)
    S = []
    i = len(weights)-1
    while i >=1:
        if A[i-1] >=A[i-2] + weights[i]:
            i-=1
        else:
            S.append(i)
            i-=2
    maxSum = 0
    for i in S:
        maxSum +=weights[i]
    return S, maxSum
