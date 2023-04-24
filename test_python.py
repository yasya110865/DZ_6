numbers = [1, 2, 4, 5, 7, 8, 10, 11]
filterlist = filter(lambda x: x > 3, numbers)
print(list(filterlist))

mapped_numbers = list(map(lambda x: x * 2 + 3, numbers))
print(mapped_numbers)

def test_filter():
    assert list(filter(lambda x: x > 3, numbers)) == [4, 5, 7, 8, 10, 11]

def test_map():
    assert list(map(lambda x: x * 2 + 3, numbers)) == [5, 7, 11, 13, 17, 19, 23, 25]

def test_sorted():
    assert sorted([2, 4, 1]) == [1, 2, 4]

import math

def test_pi():
    assert math.pi < 3.15

def test_pow():
    assert math.pow(2, 2) == 4

def testr_sqrt():
    assert math.sqrt(16) == 4

def test_hypot():
    assert math.hypot(-2, 0) == 2


