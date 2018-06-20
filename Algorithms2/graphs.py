import queue
import sys

class Node(object):

    def __init__(self, vertex=None):
        self.explored = False

    def isExplored(self):
        return self.__explored

    def set_explored(self, explored):
        self.__explored = explored        

class Graph(object):

    def __init__(self, graph_dict=None):
        #inits a graph object.
        #if no dict or none is given, 
        #an empty dict will be used.
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        self.__vertex_explored = {}
        self.mark_all_explored(False)

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def mark_explored(self, vertex, isExplored):
        self.__vertex_explored[vertex] = isExplored

    def mark_all_explored(self, explored):
        for vertex in self.vertices():
            self.__vertex_explored[vertex] = explored

    def add_edge(self,edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex,neighbour})
        return edges

    def reverse_graph(self):
        rev_graph = Graph()
        for vertex in self.vertices():
            rev_graph.add_vertex(vertex)
            for w in self.__graph_dict[vertex]:
                rev_graph.add_edge({w,vertex})
        return rev_graph
    
    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res+=str(k) + " "
        res+= "\nedges: "
        for edge in self.__generate_edges():
            res+= str(edge) + " "
        return res

    def find_path(self, start_vertex, end_vertex, path=None):
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)

                if extended_path:
                    return extended_path
        return None

    def BFS_shortest_distance(self, start_vertex, end_vertex):
        dist = {}
        graph = self.__graph_dict
        explored = self.__vertex_explored
        self.mark_all_explored(False)
        self.mark_explored(start_vertex, True)
        Q = queue.Queue()
        dist[start_vertex] = 0
        if (start_vertex == end_vertex):
            dist[end_vertex] = 0
        else:
            dist[end_vertex] = sys.maxsize
        Q.put(start_vertex)        
        while Q.empty() == False:
            v = Q.get()
            for w in graph[v]:
                if (explored[w] == False):
                    dist[w] = dist[v] + 1
                    self.mark_explored(w, True)
                    Q.put(w)
        if (explored[end_vertex] == True):
            return dist[end_vertex]
        else:
            return -1
        

        
