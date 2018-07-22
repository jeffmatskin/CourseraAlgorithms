import sys
sys.setrecursionlimit(300000)

def reverse_graph(g):
    rev_graph = {}
    for v in g.keys():
        for w in g[v]:
            if w in rev_graph:
                rev_graph[w].append(v)
            else:
                rev_graph[w] = [v]
    for i in g.keys():
        if i not in rev_graph.keys():
            rev_graph[i] = []
    return rev_graph

def convert_toGraph(srcFile):
    file = open(srcFile)
    graph = {}
    maxVertex = 0
    for line in file:
        row = [int(s) for s in line.split()]
        if row[0] > maxVertex:
            maxVertex = row[0]
        if row[1] > maxVertex:
            maxVertex = row[1]
        if row[0] not in graph.keys():
            graph[row[0]] = [row[1]]
        else:
            graph[row[0]].append(row[1])
    for i in range(1,maxVertex):
        if i not in graph.keys():
            graph[i] = []
    return graph


#globals
visited={}
finish={}
leader={}
t=0

def init(N):
    for i in range(1,N+1):
        visited[i]=0
        finish[i]=0
        leader[i]=0

def dfs(G, i):
    global t
    visited[i]=1
    leader[i]=s
    for j in G[i]:
        if(visited[j]==0): dfs(G,j)
    t+=1
    finish[i]=t

def dfs_loop(G):
    global t
    global s
    t=0 #number of nodes processed so far
    s=0 #current source vertex
    i=max(G.keys())
    while(i>0):
        if(visited[i]==0):
            s=i
            dfs(G,i)
        i=i-1

def kosaraju(g):
    N = max(g.keys())
    grev = reverse_graph(g)
    init(N)
    dfs_loop(grev) #THE FIRST LOOP ON REVERSE GRAPH
    print("first loop done")
    # construct new graph
    newGraph={}
    for i in range(1,N+1):
        temp=[]
        for x in g[i]: temp.append(finish[x])
        newGraph[finish[i]]=temp

    init(N)    
    dfs_loop(newGraph) #THE SECOND LOOP 

    print("second loop done")
    # statistics
    lst= sorted(leader.values())
    stat=[]
    pre=0
    for i in range(0,N-1):
        if lst[i]!=lst[i+1]:
            stat.append(i+1-pre)
            pre=i+1
    stat.append(N-pre)
    L= sorted(stat)
    L.reverse()
    print(L[0:10])