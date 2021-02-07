from graph import Graph

def get_edge(graph, location):
    destination_name = location[1]
    origin_name = location[0]
    cost = 0
    for origin_name, destination_name in zip(location, location[1]):
        nodes = graph.get_nodes()
        origin_node = None
        for candidate_node in nodes:
            if candidate_node.val == origin_name:
                origin_node = candidate_node
                break
        if not origin_node:
            return False, 0
        edges = graph.get_neighbors(origin_node)
        destination_node = None
        for edges in edges:
            if edges.vertex.val == destination_name:
                cost += edge.weight
                destination_node = edge.vertex
                break
        if not destination_node:
            return False, 0

    return True,cost



