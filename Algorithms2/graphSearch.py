import queue
import sys
import time
from itertools import groupby
from collections import defaultdict

sys.setrecursionlimit(10**6)


finishing_time = 0
finishing_times = None
current_source_vertex = None
current_label = None
order = None
leader = None
explored = None

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

def DFS_leaders(G,s,firstPass):
    global finishing_time, finishing_times, leader, explored    
    explored.append(s)
    leader[s] = current_source_vertex
    for v in G[s]:
        if v not in explored:
            DFS_leaders(G,v,firstPass)
    if(firstPass):
        finishing_time+=1
        finishing_times[s]=finishing_time
    return explored


def kosaraju_two_pass(g):
    global current_source_vertex, finishing_time, finishing_times, leader, explored
    grev = reverse_graph(g)
    explored = []
    finishing_times = {}
    finishing_time = 0    
    leader = {}
    #first pass on reverse
    for i in range(max(g.keys()),0,-1):
        if i not in explored:            
            current_source_vertex = i
            DFS_leaders(grev,i, True)
    #second pass in order of leader vertices    
    explored = []
    
    for j in range(max(g.keys()),0,-1):        
        i = finishing_times[j]        
        if i not in explored:
            current_source_vertex = i
            DFS_leaders(g,i,False)
    return leader

def findLargestConnectedComponents(g):
    leaderList = kosaraju_two_pass(g)
    leaderCounts = [0]*len(leaderList.keys())

    for k in leaderList.keys():
        leaderCounts[leaderList[k]-1]+=1
    return sorted(leaderCounts,reverse=True)[0:5]

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


