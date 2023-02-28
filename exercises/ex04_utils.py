"""Working with and generating lists"""

__author__ = "730605045"

def all(numbers: list[int], target: int) -> bool:
    listidx: int = 0
    
    while listidx < len(numbers):
    #Returns True if all numbers in the given list are equal to the given target number.
    #Returns False otherwise, or if the list is empty.
        if numbers[listidx] != target:
            return False
        else:
            listidx += 1
    return True



def max(maxnumbers: list[int]) -> int:
    if len(maxnumbers) == 0:
        raise ValueError("max() arg is an empty List")
    
    maxidx: int = 0
    maxval: int = 0
    maxval = maxnumbers[0]
    while maxidx < len(maxnumbers):
        #The max function is given a list of ints, max should return the largest in the List
        if maxnumbers[maxidx] > maxval:
            maxval = maxnumbers[maxidx]
        maxidx += 1
    return maxval
    
def is_equal(firstlist: list[int], secondlist: list[int]) -> bool:
    equalidx: int = 0
    #return True if every element at every index is equal in both lists.
    if len(firstlist) != len(secondlist):
        raise ValueError("firstlist() has unequal amounts compared to secondlist()")
    while equalidx < len(firstlist):
        if firstlist[equalidx] != secondlist[equalidx]:
            return False
        equalidx += 1
    return True
