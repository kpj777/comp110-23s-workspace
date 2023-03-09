"""Working with and generating lists."""

__author__ = "730605045"


def all(numbers: list[int], target: int) -> bool: 
    """Given a list of ints and an int, all should return True if all ints in list are same as given int."""
    if len(numbers) == 0:
        return False
    listidx: int = 0
    while listidx < len(numbers):
        # Returns True if all numbers in the given list are equal to the given target number.
        # assert the list is not empty.
        if numbers[listidx] != target:
            return False
        else:
            listidx += 1
    return True


def max(maxnumbers: list[int]) -> int:
    """In a list of int, return max value."""
    if len(maxnumbers) == 0:
        raise ValueError("max() arg is an empty List")
    maxidx: int = 0
    maxval: int = 0
    maxval = maxnumbers[0]
    while maxidx < len(maxnumbers):
        # The max function is given a list of ints, max should return the largest in the List.
        if maxnumbers[maxidx] > maxval:
            maxval = maxnumbers[maxidx]
        maxidx += 1
    return maxval
    

def is_equal(firstlist: list[int], secondlist: list[int]) -> bool:
    """is_equal should return True if all values in first list are equal to all values in second list."""
    equalidx: int = 0
    # assert Lists length is not equal.
    if len(firstlist) < 0:
        return False
    if len(secondlist) < 0:
        return False
    if len(firstlist) != len(secondlist):
        return False
    # return True if every element at every index is equal in both lists.
    while equalidx < len(firstlist):
        if firstlist[equalidx] != secondlist[equalidx]:
            return False
        equalidx += 1
    return True