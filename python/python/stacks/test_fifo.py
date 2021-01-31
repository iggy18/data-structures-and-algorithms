from fifo_animal_shelter import Node, Queue, AnimalShelter, InvalidOperationError
import pytest

def test_node():
    assert Node

def test_queue_exists():
    assert Queue

def test_invalid_operation_error():
    assert InvalidOperationError

def test_enqueue():
    q = Queue()
    q.enqueue("sharp pointy teeth")
    actual = q.front.val
    expected = "sharp pointy teeth"
    assert actual == expected

def test_is_empty_is_true():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

def test_is_empty_is_false():
    q = Queue()
    q.enqueue("test")
    actual = q.is_empty()
    expected = False
    assert actual == expected

def test_dequeue():
    pass
    q = Queue()
    q.enqueue("dog")
    q.dequeue()
    actual = q.is_empty
    expected = True

def test_dequeue_multiple():
    q = Queue()
    q.enqueue("one")
    q.enqueue("two")
    q.enqueue("three")
    q.enqueue("four")
    q.dequeue()
    actual = q.front.val
    expected = "two"
    assert actual == expected

def test_peek():
    q = Queue()
    q.enqueue("one")
    q.enqueue("two")
    q.enqueue("three")
    q.dequeue()
    q.dequeue()
    actual = q.peek()
    expected = "three"
    assert actual == expected

def test_enqueue_dog():
    q = AnimalShelter()
    q.enqueue("dog")
    actual = q.dogs.peek()
    expected = "dog"
    assert actual == expected

def test_enqueue_dog_does_not_put_cats_in_dog_queue():
    q = AnimalShelter()
    q.enqueue("cat")
    actual = q.dogs.is_empty()
    expected = True
    assert actual == expected

def test_enqueue_cat():
    q = AnimalShelter()
    q.enqueue("cat")
    actual = q.cats.peek()
    expected = "cat"
    assert actual == expected


def test_enqueue_cat_does_not_put_dogs_in_cat_queue():
    q = AnimalShelter()
    q.enqueue("dog")
    actual = q.cats.is_empty()
    expected = True
    assert actual == expected

def test_returns_none_if_no_preference():
    q = AnimalShelter()
    q.enqueue("dog")
    q.enqueue("cat")
    q.enqueue("dog")
    actual = q.dequeue()
    expected = None
    assert actual == expected

def test_dequeue_returns_prefered_dog():
    q = AnimalShelter()
    q.enqueue("dog")
    q.enqueue("cat")
    q.enqueue("dog")
    actual = q.dequeue("dog")
    expected = 'dog'
    assert actual == expected

def test_dequeue_returns_prefered_cat():
    q = AnimalShelter()
    q.enqueue("dog")
    q.enqueue("cat")
    q.enqueue("dog")
    actual = q.dequeue("cat")
    expected = 'cat'
    assert actual == expected

def test_empty_Dogs_queue_peek_raises_invalidoperationerror():
    q = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        q.dogs.peek()

def test_empty_cats_queue_peek_raises_invalidoperationerror():
    q = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        q.cats.peek()

def test_empty_dog_dequeue_raises_invalidoperationerror():
    q = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        q.dequeue("dog")

def test_empty_cat_dequeue_raises_invalidoperationerror():
    q = AnimalShelter()
    with pytest.raises(InvalidOperationError):
        q.dequeue("cat")







