from collections import defaultdict

Graph = {}

Transpose_Graph = {}

Visited_Nodes_Graph = {}

Visited_Nodes_Transpose_Graph = {}

Component_Id = dict()

Stack = []

def dfs(graph, start):    
    Visited_Nodes_Graph.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited

def dfs_scc_loop(graph):
    connected = []
    for i in graph.keys():        
        connected.append(dfs(graph,i))
    return connected

