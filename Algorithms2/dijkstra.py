import collections
import math

class Graph:

    def __init__(self):
        self.vertices = set()
        
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self,value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex: pass #no cycles
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)

        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex,to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string        

def dijkstra_minpaths(G, start):
    S = set()

    A = dict.fromkeys(list(G.vertices), math.inf)
    previous = dict.fromkeys(list(G.vertices), None)

    A[start] = 0

    while S!= G.vertices:
        v = min((set(A.keys()) - S), key=A.get)

        for neighbour in set(G.edges[v]) - S:
            new_path = A[v] + G.weights[v,neighbour]

            if new_path < A[neighbour]:
                A[neighbour] = new_path
            previous[neighbour] = v
        S.add(v)

    return A,previous

def import_weighted_graph(srcFile):
    file = open(srcFile)
    graph = Graph()
    for line in file:
        arrayLine = line.split()
        vertex = int(arrayLine[0])
        for i in range(1,len(arrayLine)):
            neighbourInfo = arrayLine[i].split(",")
            neighbour = int(neighbourInfo[0])
            weight = int(neighbourInfo[1])
            graph.add_edge(vertex,neighbour, weight)
    return graph
    
def dijkstra_get_required(srcFile, start):
    distances,paths = dijkstra_minpaths(import_weighted_graph(srcFile),start)
    required = [7,37,59,82,99,115,133,165,188,197]
    for i in required:
        print(distances[i])
