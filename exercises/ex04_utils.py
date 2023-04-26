"""EX04 - 'List' Utils Function."""


__author__ = "730617864"


def all(list1: list[int], parameter: int) -> bool:
    """Check whether the given number matches all numbers of the list."""
    idx = 0
    if list1 == []:
        return False
    while idx < len(list1):
        if list1[idx] != parameter:
            return False
        idx += 1
    return True


def max(list1: list[int]) -> int:
    """Returns the highest number from the list."""
    if not list1:
        raise ValueError("max() arg is an empty List")
    largestnumber = list1[0]
    idx = 1
    while idx < len(list1):
        if list1[idx] > largestnumber:
            largestnumber = list1[idx]
        idx += 1
    return largestnumber


def is_equal(firstnumber: list[int], secnumber: list[int]) -> bool:
    """Check whther all elements of the list are equal to each other at the respective indices."""
    idx = 0
    while idx < len(firstnumber) and idx < len(secnumber):
        if firstnumber[idx] != secnumber[idx]:
            return False
        idx += 1
    return len(firstnumber) == len(secnumber)
