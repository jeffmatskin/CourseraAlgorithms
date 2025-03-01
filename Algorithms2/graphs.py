class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
    
    def __str__(self):
        return str(self.id) + " adjacent: " + str([x.id for x in self.adjacent])
    
    def add_neighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, weight = 0):
        if frm not in self.vert_dict.keys():
            self.add_vertex(frm)
        if to not in self.vert_dict.keys():
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbour(self.vert_dict[to], weight)

    def get_vertices(self):
        return self.vert_dict.keys()

