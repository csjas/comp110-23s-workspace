"""EX05 - 'list' Utility functions."""

__author__ = "730617864"


def only_evens(list1: list[int]) -> list[int]:
    """Even value is only returned."""
    # Dividing by 2 as we awant even number.
    start: int = 0
    compare: list[int] = []
    while start < len(list1):
        if list1[start] % 2 == 0:
            compare.append(list1[start])
        start = start + 1    
    return compare    


print(only_evens([2, 3, 4]))


def concat(list_2: list[int], list_3: list[int]) -> list[int]:
    """Result will consist of first word followed by second word."""
    start_1: int = 0
    list_4: list[int] = []

    while start_1 < len(list_2):
        list_4.append(list_2[start_1])
        start_1 = start_1 + 1
        
    start_2: int = 0    
    while start_2 < len(list_3):
        list_4.append(list_3[start_2])
        start_2 = start_2 + 1
    return list_4  
    
        
print(concat([1, 2, 3], [4, 5, 6]))   


def sub(list_5: list[int], first: int, last: int) -> list[int]:
    """Function of lists is supposed to be returned."""
    list_6: list[int] = []
    if first < 0:
        first = 0

    if last > len(list_5):
        last = (len(list_5))

    if len(list_5) == 0:
        return list_6

    if last <= 0:
        return list_6  

    while first < last:
        list_6.append(list_5[first])
        first += 1
    return list_6