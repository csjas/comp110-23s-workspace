"""Challenge question - 04"""

author = "730617864"

def zip(List1: list[str], List2: list[int]) -> dict[str,int]:
    """Arguments stated as lists which returns dictionary which constitutes string and integer."""
    if len(List1) != len(List2) or len(List1) == 0:
        return{}
    
    empty = {}
    for start in range(len(List1)):
        empty[List1[start]] = List2[start]
    return empty