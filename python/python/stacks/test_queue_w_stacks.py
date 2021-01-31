import pytest

from queue_with_stack import Node, Stack, Pseudo_Queue, InvalidOperationError


def test_enqueue():
    q = Pseudo_Queue()
    q.enqueue("charles")
    q.enqueue("bukowsi")
    actual = q.first_stack.top_of_stack.value
    expected = "charles"
    assert actual == expected


def test_dequeue():
    q = Pseudo_Queue()
    q.enqueue("charles")
    q.dequeue()
    actual =q.first_stack.is_empty()
    expected = True
    assert actual == expected


def test_dequeue_when_empty():
    q = Pseudo_Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


def test_peek():
    q = Pseudo_Queue()
    q.enqueue("peek-a-boo")
    actual = q.first_stack.peek()
    expected = "peek-a-boo"
    assert actual == expected


def test_empty_peek():
    q = Pseudo_Queue()
    with pytest.raises(InvalidOperationError):
        q.first_stack.peek()


def test_is_empty():
    q = Pseudo_Queue()
    q.enqueue("test")
    q.dequeue()
    actual = q.first_stack.is_empty()
    expected = True
    assert actual == expected

def test_fill_and_empty():
    q = Pseudo_Queue()
    q.enqueue("one")
    q.enqueue("two")
    q.enqueue("three")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.first_stack.is_empty()
    expected = True
    assert actual == expected
