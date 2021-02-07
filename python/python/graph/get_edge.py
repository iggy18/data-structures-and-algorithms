from graph import Graph

def get_edge(graph, location):
    destination_name = location[1]
    origin_name = location[0]
    cost = 0
    for origin_name, destination_name in zip(location, location[1]):
        nodes = graph.get_nodes()
        origin = None
        for node in nodes:
            if node.val == origin_name:
                origin = node
                break
        if not origin:
            return False, 0
        edges = graph.get_neighbors(origin)
        destination = None
        for edges in edges:
            if edges.vertex.val == destination_name:
                cost += edge.weight
                destination = edge.vertex
                break
        if not destination:
            return False, 0

    return True,cost



