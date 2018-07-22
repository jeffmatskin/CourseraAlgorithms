from unionFind import UnionFind
from operator import itemgetter

def max_spacing_kcluster(nodes, edges, k):
    
    unionSet = UnionFind()
    unionSet.addNodes(nodes)
    edges = sorted(edges,key = itemgetter(2))
    i = 0
    min_edge = None
    while not unionSet.cardinality < k:
        min_edge = edges[i]
        i+=1
        u,v = min_edge[0], min_edge[1]
        x = unionSet.find(u)
        y = unionSet.find(v)
        if x!=y:
            unionSet.union(x,y)
    
    return edges[i-1][2]

def readBitData(src):    
    nodes = set()
    file = open(src)
    n,bitLength = map(int, file.readline().split())
    for line in file:
        bit_rep = map(int, line.split())
        v=0
        for i in range(0,bitLength):
            if bit_rep[i]:
                v+=2**(i)        
        nodes.add(v)
    return nodes, bitLength

def switch_bit(v,index):
    v ^= (1 << index)
    return v

def clustersNeeded(nodes, bitLength):
    unionSet = UnionFind()    
    unionSet.addNodes(nodes)
    for node in nodes:        
        one_bit_difference = oneBitVaried(node,bitLength)
        for u in one_bit_difference:
            if u in nodes:
                unionSet.union(node,u)
            two_bit_difference = oneBitVaried(u,bitLength)
            for v in two_bit_difference:            
                if v in nodes:
                    unionSet.union(node,v)
    return unionSet.cardinality, unionSet

def oneBitVaried(x,bitLength):
    variations = []
    for i in range (0,bitLength):
        u = switch_bit(x,i)
        variations.append(u)
    return variations