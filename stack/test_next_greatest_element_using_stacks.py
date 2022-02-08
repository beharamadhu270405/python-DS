
from next_greatest_element_using_stacks import nextLargestElment


def test_nextLargestElment():
    assert list(nextLargestElment([1, 2, 3, 4])) == [2, 3, 4, -1]


def test_nextLargestElment_Wrong():
    assert list(nextLargestElment([1, 2, 3, 4])) != [2, 3, 4, -4]
