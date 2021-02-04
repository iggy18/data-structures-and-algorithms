from graph import WhatAreYouDoing, Vertex, Edge, Graph
import pytest

def test_what_are_you_doing():
    assert WhatAreYouDoing

def test_Vertex():
    assert Vertex

def test_edge():
    assert Edge

def test_graph():
    assert Graph

def test_add_node():
    x = Graph()
    vertex = x.add_node('spam')
    assert isinstance(vertex, Vertex)

def test_add_node_returns_correct_value():
    x = Graph()
    actual = x.add_node('spam').val
    expected = "spam"
    assert actual == expected

def test_add_edge():
    x = Graph()
    origin = x.add_node('start')
    destination = x.add_node('end')
    x.add_edge(origin, destination, 10)

def test_add_edge_with_weight():
    x = Graph()
    origin = x.add_node("start")
    destination = x.add_node("end")
    weight = 15
    graph = x.add_edge(origin, destination, weight)

def test_add_edge_interloper_start():
    x = Graph()
    start = Vertex("start")
    end = x.add_node("end")
    with pytest.raises(WhatAreYouDoing):
        x.add_edge(start, end)

def test_add_edge_interloper_end():
    x = Graph()
    end = Vertex("end")
    start = x.add_node("start")
    with pytest.raises(WhatAreYouDoing):
        x.add_edge(start, end)

def test_get_nodes():
    x = Graph()
    x.add_node("banana")
    x.add_node("apple")
    expected = 2
    actual = len(x.get_nodes())
    assert actual == expected

def test_get_neighbors_none():
    x = Graph()
    banana = x.add_node("banana")
    neighbors = x.get_neighbors(banana)
    assert len(neighbors) == 0

def test_get_neighbors_returns_edges():
    x = Graph()
    banana = x.add_node("banana")
    apple = x.add_node("apple")
    x.add_edge(apple, banana)
    neighbors = x.get_neighbors(apple)
    assert len(neighbors) == 1
    neighbor = neighbors[0]
    assert isinstance(neighbor, Edge)
    assert neighbor.vertex.val == 'banana'


def test_get_neighbors_returns_edges_with_default_weight():
    x = Graph()
    banana = x.add_node("banana")
    apple = x.add_node("apple")
    x.add_edge(apple, banana)
    neighbors = x.get_neighbors(apple)
    actual = neighbors[0].weight
    expected = 0
    assert actual == expected


def test_get_neighbors_returns_edges_with_custom_weight():
    x = Graph()
    banana = x.add_node("banana")
    apple = x.add_node("apple")
    x.add_edge(apple, banana, 44)
    neighbors = x.get_neighbors(apple)
    neighbor_edge = neighbors[0]
    assert neighbor_edge.weight == 44


def test_size_empty():
    x = Graph()
    expected = 0
    actual = x.size()
    assert actual == expected


def test_size_one():
    x = Graph()
    x.add_node("spam")
    expected = 1
    actual = x.size()
    assert actual == expected


def test_size_two():
    d = Graph()
    d.add_node("spam")
    d.add_node("bacon")
    expected = 2
    actual = d.size()
    assert actual == expected
