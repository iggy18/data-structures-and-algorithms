from left_join import left_join
from collections import Counter

def test_left_join():
    assert left_join

def test_joined_hash_maps():
    synonym = {"fond":"enamored", "wrath":"anger", "diligent":"employed", "outfit":"garb", "guide":"usher"}
    antonym = {"fond":"averse", "wrath":"delight", "diligent":"idle", "guide":"follow", "flow":"jam"}
    actual = left_join(synonym, antonym)


