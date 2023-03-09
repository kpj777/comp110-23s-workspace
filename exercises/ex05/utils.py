"""Exercise 5 List Functions"""

__author__ = 730605045

def only_evens(numbers: list[int]) -> list[int]:
    """Given a list of ints, only_evens should return a new list with only even numbers."""
    evens: list[int] = []
    for i in numbers:
        if i % 2 == 0: #number is even:
            evens.append(i)
    return evens

def concat(firstlist: list[int], secondlist: list[int]) -> list[int]:
    """add elements of first list and second list."""
    result: list[int] =[]
    for i in firstlist:
        result.append(i)
    for i in secondlist:
        result.append(i)
    return result

def sub(a_list: list[int], start: int, end: int):
    """generate a subset of the input list between start and end."""
    if len(a_list) == 0 or start >= len(a_list) or end <= 0:
        return []
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    
    return a_list[start:end]
