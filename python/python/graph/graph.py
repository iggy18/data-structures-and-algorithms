class WhatAreYouDoing(Exception):
    pass

class Vertex:
    def __init__(self, val):
        self.val = val
        self.next = None

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.neighbors = {}

    def add_node(self, val):
        node = Vertex(val)
        self.neighbors[node] = []
        return node

    def add_edge(self, origin, destination, weight=0):
        if origin not in self.neighbors:
            raise WhatAreYouDoing('you need an origin node')
        if destination not in self.neighbors:
            raise WhatAreYouDoing('you need a destination node')

        connect = Edge(destination, weight)
        connections = self.neighbors[origin]
        connections.append(connect)

    def get_nodes(self):
        return self.neighbors.keys()

    def get_neighbors(self, node):
        return self.neighbors[node]

    def size(self):
        return len(self.neighbors)
