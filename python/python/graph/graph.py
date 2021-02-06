from stacks import Queue

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
        vertex = Vertex(val)
        self.neighbors[vertex] = []
        return vertex

    def add_edge(self, origin, destination, weight=0):
        if origin not in self.neighbors:
            raise WhatAreYouDoing('you need an origin vertex')
        if destination not in self.neighbors:
            raise WhatAreYouDoing('you need a destination vertex')
        connect = Edge(destination, weight)
        connections = self.neighbors[origin]
        connections.append(connect)

    def get_nodes(self):
        return self.neighbors.keys()

    def get_neighbors(self, vertex):
        return self.neighbors[vertex]

    def size(self):
        return len(self.neighbors)

    def breadth_first(self, vertex):
        visited_vertex = [vertex]
        queue = Queue()
        queue.enqueue(vertex)
        while not queue.is_empty():
            vertex = queue.dequeue()
            neighbors = [edge.vertex for edge in self.get_neighbors(vertex)]
            for neighbor in neighbors:
                if neighbor not in visited_vertex:
                    visited_vertex.append(neighbor)
                    queue.enqueue(neighbor)
        return visited_vertex

