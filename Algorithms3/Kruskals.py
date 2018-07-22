from unionFind import *
from operator import itemgetter
#have edges defined in a list of lists, with inner list in
#the order (node1, node2, cost)
def kruskalsMST(nodes, edges):
    unionSet = UnionFind()    
    edges = sorted(edges,key = itemgetter(2))
    T=[]
            
    for i in edges:
        u,v = i[0],i[1]
        x = unionSet.find(u)
        y = unionSet.find(v)

        if x != y:
            T.append(i)
            unionSet.union(x,y)

    return T


       