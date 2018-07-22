import random as rand
import copy

def RandCut(V,E):
    if len(V) <=2:
        return V,E
    u,v = pickRand(V)
    mergeVertices(V,E,u,v)
    RandCut(V,E)

def mergeVertices(V,E,u,v):
    mergedVertex = V[u]
    E.pop(v)
    vertex = V.pop(v)
    mergedVertex.append(vertex)
    
def karger(G):
    cut = []
    while len(G) > 2:
        u, v = pickRand(G)
        G[u].extend(G[v])
        for x in G[v]:
            G[x].remove(v)
            G[x].append(u)
        while u in G[u]:
            G[u].remove(u)
        del G[v]
    for key in G.keys():
        cut.append(len(G[key]))
    return cut[0]

def pickRand(G):
    u=rand.choice(list(G.keys()))
    v=rand.choice(list(G[u]))    
    return u, v

def MinCut(G):
    data = copy.deepcopy(G)
    mincut = karger(data)
    for i in range(0,len(G)*len(G)):
        data = copy.deepcopy(G)
        thiscut = karger(data)
        if thiscut < mincut:
            mincut = thiscut
    return mincut
    


f = open("Graph.txt")
G={}

for line in f:    
    row = [int(s) for s in line.split()]
    G[row[0]] = row[1:]

print(MinCut(G))