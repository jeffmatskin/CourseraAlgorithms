import queue

current_label = None
order = {}

def reverse_graph(g):
    rev_graph = {}
    for v in g.keys():
        for w in g[v]:
            if w in rev_graph:
                rev_graph[w].append(v)
            else:
                rev_graph[w] = [v]

    return rev_graph

def undirected(g):
    h = reverse_graph(g)
    undir_graph = {}
    for v in g.keys():
        for w in g[v]:
            if v in undir_graph.keys():
                undir_graph[v].append(w)
            else:
                undir_graph[v] = [w]
    
    for v in h.keys():
        for w in h[v]:
            if v in undir_graph.keys():
                undir_graph[v].append(w)
            else:
                undir_graph[v]=[w]
    
    return undir_graph

def BFS(G,s):
    explored = []
    Q = queue.Queue()
    Q.put(s)
    explored.append(s)
    while Q.empty() == False:
        v = Q.get()
        for w in G[v]:
            if w not in explored:
                explored.append(w)
                Q.put(w)
    return explored

def BFS_shortest_distance(G, s, t):
    explored = []
    dist = {}  
    Q = queue.Queue()
    Q.put(s)
    explored.append(s)
    dist[s] = 0
    while Q.empty() == False:
        v = Q.get()        
        for w in G[v]:
            if w not in explored:
                explored.append(w)
                dist[w] = dist[v] + 1
                Q.put(w)
    if (t in explored):
        return dist[t]
    else:
        return -1

def BFS_undirected_connectivity(G):
    connected_components = []
    explored = []
    for i in G.keys():
        if i not in explored:
            search_results = BFS(G,i)
            for j in search_results:
                explored.append(j)
            connected_components.append(search_results)

    return connected_components

def DFS_looped(G, s):
    explored = []
    stack = [s]    
    explored.append(s)
    while len(stack) > 0:
        v = stack.pop()
        for w in G[v]:
            if w not in explored:
                explored.append(w)
                stack.append(w)
    return explored

def DFS(G,s,explored=None):
    if explored == None:
        explored = []
    explored.append(s)
    for v in G[s]:
        if v not in explored:
            DFS(G,v,explored)
    return explored    

def DFS_sort(G,s,explored=None):
    global current_label, order    
    if explored == None:
        explored = []
    explored.append(s)
    for v in G[s]:
        if v not in explored:
            DFS_sort(G,v,explored)
    order[s] = current_label
    current_label -=1
    return explored

def DFS_topological_sort(G):
    global current_label, order    
    current_label = len(G)
    order = {}
    outer_explored = []
    for v in G.keys():
        if v not in outer_explored:
            explored = DFS_sort(G,v)
            for w in explored:
                if w not in outer_explored:
                    outer_explored.append(w)
    return order
