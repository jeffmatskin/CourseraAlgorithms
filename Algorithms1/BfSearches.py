def BfS(G, s):
    queue = [s]
    visited = set()
    visited.add(s)
    while queue:
        v = queue.pop(0)        
        for adjacent in G.get(v, []):
            if (adjacent not in visited):
                visited.add(adjacent)
                queue.append(adjacent)
    return visited

def BfSConn_Compnents(G):
    visited = []
    connectedSets = []
    for i,j in enumerate(G.keys()):
        if j not in visited:
            connected = BfS(G,j)
            visited.extend(connected)
            connectedSets.append(connected)
    return connectedSets
        
def BfSDist(G,s,x):
    dist = {}
    if (s == x):
        return 0    
    dist.update({s:0})
    queue = [s]

    while queue:
        v = queue.pop(0)
        for adjacent in G.get(v, []):
            if (adjacent not in dist.keys()):
                dist.update({adjacent:dist[v]+1})                
                queue.append(adjacent)
    if (x not in dist):
        return -1
    else:
        return dist[x]
    
