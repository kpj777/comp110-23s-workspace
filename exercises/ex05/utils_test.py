"""test the utils in utils.py"""

__author__ = 730605045

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

def test_only_evens() -> None:
    """Asserts that list will only result in evens."""
    assert only_evens([1, 2, 3]) == [2]

def test_sub() -> None:
    a_list = [10, 20, 30, 40]
    """Asserts that list will only result in the idx range given"""
    assert sub(a_list, 1, 3) == [20, 30]

def test_concat() -> None:
    firstlist = [1, 2, 3]
    secondlist = [4, 5, 6]
    """Asserts first list is added correctly to second list in order."""
    assert concat(firstlist, secondlist) == [1, 2, 3, 4, 5, 6]

