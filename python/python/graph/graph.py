class WhatAreYouDoing(Exception):
    pass

class Vertex:
    def __init__(self, val):
        self.val = val
        self.next = None

class Edge:
    def __init__(self, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.neighbors = {}

    def add_node(self):
        node = vertex(val)
        self.neighbors[node] = []
        return node

    def add_edge(self, origin, destination):
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
        neighborhood = []
        connetions = self.neighbors.get(node, [])
        for neighbor in connections:
            close = {}
            close[neighbor] = neighbor.weight
            neighbor.append(close)
        return neighborhood

    def size():
        return len(self.neighbors)
