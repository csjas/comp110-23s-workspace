"""EX07 - Dictionary Functions."""

__author__ = "730617864"

def invert(func_first: dict[str, str]) -> dict[str, str]:
    """"""
    inversion: dict[str, str] = dict()
    for values in func_first:
        if func_first[values] in inversion:
            raise KeyError("There is a a request of one of the values.")
        else:
            inversion[func_first[values]] = values
    return inversion

def favorite_color(colour: dict[str, str]) -> str:
    """"""
    dict_colour: dict[str, int] = dict()
    highest_freq: str = ""
    freq: int = 0
    for colouring in colour:
        if colour[colouring] in dict_colour:
            dict_colour[colour[colouring]] += 1
        else:
            dict_colour[colour[colouring]] = 1
    for counting in dict_colour:
        if dict_colour[counting] > freq:
            freq = dict_colour[counting]
            highest_freq = counting
    return highest_freq        

def count(freq: list[str]) -> dict[str, int]:
    """"""
    each_item: dict[str, int] = dict()
    for words in freq:
        if words in each_item:
            each_item[words] =+ 1
        else: 
            each_item[words] = 1
    return each_item