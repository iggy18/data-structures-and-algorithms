
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


def test_get_apple():
    hashtable = HashTable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


def test_get_silent_and_listen():
    hashtable = HashTable()
    hashtable.set('listen', 'to me')
    hashtable.set('silent', 'so quiet')

    assert hashtable.get('listen') == 'to me'
    assert hashtable.get('silent') == 'so quiet'
