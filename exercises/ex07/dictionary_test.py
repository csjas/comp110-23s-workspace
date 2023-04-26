"""EX07 - Dictionary Functions."""

__author__ = "730617864"


from dictionary import invert, favorite_color, count


def test_invert_the_empty() -> None:
    """"""
    one: dict[str, str] = {}
    assert invert(one) == {}


def test_invert_the_different() -> None:
    """"""
    one: dict[str, str] = {'a': 'z'}
    assert invert(one) == {'z': 'a'}


def test_invert_the_same() -> None:
    """"""
    one: dict[str,str] = {'a': 'a'}
    assert invert(one) =={'a': 'a'}


def test_favorite_color_empty() -> None:
    """"""
    color: dict[str, str] = {}
    assert favorite_color(color) == {}


def test_favorite_color_mostpopular() -> None:
    """"""
    color: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color() == "blue"


def test_favorite_color_allsame() -> None:
    """"""
    color: dict[str, str] = {"Marc": "yellow", "Danny": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(color) == "yellow"


def test_count_empty() -> None:
    """"""
    freq: list[str] = []
    assert count(freq) == {}


def test_count_threestring() -> None:
    """"""
    freq: list[str] = ["apple", "apple", "banana"]
    assert count(freq) == {"apple": 2, "banana": 1}
    

def test_count_twostrings() -> None:
    """"""
    freq: list[str] = ["apple", "apple"]
    assert count(freq) == {"apple": 2}