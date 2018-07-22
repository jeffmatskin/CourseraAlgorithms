from heapq import *
from collections import defaultdict
# list of nodes, list of edges defined in the order vertex, vertex, cost/weight
def prim(nodes, edges): 
    edgeDict = defaultdict(list) # dictionary of edges to each vertex, in both directions (since graph not directed)
    for u, v, c in edges:
        edgeDict[u].append([c,u,v])
        edgeDict[v].append([c,v,u])

    T = [] #minimal spanning tree
    X = set(nodes[0])

    #list of all edges connected to the set X with one vertex outside X.
    #since X starts with just one point, this initializes with all edges connected to that one point (nodes[0])
    crossing_edges = X[nodes[0]][:] 
    heapify(crossing_edges) #heap sorted
    totalCost = 0
    while crossing_edges: #continue until we exhaust the heap
        cost, u, v = heappop(usable_edges) #by construction u is in X

        #taking the edge with the minimal cost, if its second endpoint is not in X, 
        #then we add it to the minimal spanning tree T as well as to X.        
        if v not in used: 
            X.add(v)
            mst.append((n1,n2,cost))
            totalCost+=cost

            #now that we have added v, we must reinsert each
            #edge associated with v that has an endpoint outside X.
            for e in edgeDict[v]:
                if e[2] not in used:
                    heappush(usable_edges, e)
    return mst, totalCost

def readData(src):
    dataIn = open(src)
    edgeCount, vertexCount = dataIn.readline().split() #not needed but in text file.
    edges = []
    vertices = []
    for line in dataIn:
        x, y, z = line.split()
        if x not in vertices:
            vertices.append(x)
        if y not in vertices:
            vertices.append(y)
        edges.append([x,y,int(z)])
    return vertices,edges

