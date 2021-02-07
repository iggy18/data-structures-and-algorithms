
from hashtable import HashTable
import pytest

def test_create():
    hashtable = HashTable()
    assert hashtable


def test_predictable_hash():
    hashtable = HashTable()
    initial = hashtable.hash('spam')
    secondary = hashtable.hash('spam')
    assert initial == secondary


def test_same_hash():
    hashtable = HashTable()
    initial = hashtable.hash('listen')
    secondary = hashtable.hash('silent')
    assert initial == secondary


def test_different_hash():
    hashtable = HashTable()
    initial = hashtable.hash('glisten')
    secondary = hashtable.hash('silent')
    assert initial != secondary
