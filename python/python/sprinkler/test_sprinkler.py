from sprinkler import Sprinkler, SprinklerSystem

def test_import_sprinkler():
    assert Sprinkler

def test_import_sprinkler_system():
    assert SprinklerSystem

def test_get_usage():
    system = SprinklerSystem()
    a = Sprinkler()
    b = Sprinkler()
    c = Sprinkler()
    d = Sprinkler(5)
    system.inlet = a
    system.inlet.left_line = b
    system.inlet.right_line = c
    system.inlet.left_line.left_line = d
    actual = system.get_usage()
    expected = 11
    assert actual == expected


def test_get_usage_with_default():
    system = SprinklerSystem()
    a = Sprinkler()
    b = Sprinkler()
    c = Sprinkler()
    d = Sprinkler()
    system.inlet = a
    system.inlet.left_line = b
    system.inlet.right_line = c
    system.inlet.left_line.left_line = d
    actual = system.get_usage()
    expected = 8
    assert actual == expected

def test_get_usage_with_no_default():
    system = SprinklerSystem()
    a = Sprinkler(1)
    b = Sprinkler(2)
    c = Sprinkler(3)
    d = Sprinkler(4)
    system.inlet = a
    system.inlet.left_line = b
    system.inlet.right_line = c
    system.inlet.left_line.left_line = d
    actual = system.get_usage()
    expected = 10
    assert actual == expected



