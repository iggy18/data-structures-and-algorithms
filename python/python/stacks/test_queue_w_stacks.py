import pytest

from queue_with_stack import Node, Stack, Pseudo_Queue


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


@pytest.mark.skip
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

@pytest.mark.skip
def test_empty_peek():
    q = Pseudo_Queue()
    actual = q.first_stack.peek()
    expected = "Method not allowed on empty collection"
    assert actual == expected

@pytest.mark.skip
def test_empty_dequeue():
    pass

@pytest.mark.skip
def test_is_empty():
    pass

@pytest.mark.skip
def test_fill_and_empty():
    pass
