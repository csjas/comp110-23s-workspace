"""Tests for Ex05."""

__author__ = "730617864"

from exercises.ex05.utils import only_evens, sub, concat


def test_even_number() -> None:
    """Check even number in empty list."""
    assert only_evens([]) == []


def test_even_from_even_odd() -> None:
    """Even number from even and odd numbers."""
    assert only_evens([5, 7, 9]) == []


def test_even_from_all() -> None:
    """Even from all even."""
    assert only_evens([2, 2, 2]) == [2, 2, 2]


def test_concat_empty_case() -> None:
    """Empty list case."""
    assert concat([], []) == []


def test_concat_single_digit() -> None:
    """Single digit list."""
    assert concat([5], [3]) == [5, 3]


def test_concat_num_order() -> None:
    """Numbers in order."""
    assert concat([7, 8, 9], [10, 11, 12]) == [7, 8, 9, 10, 11, 12]


def test_sub_empty_list() -> None:
    """Empty list case."""
    list_x: list[int] = []
    assert sub(list_x, 1, 2) == []


def test_sub_start_end() -> None:
    """According to start and end, value is returned."""
    list_y: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_y, 1, 3) == [2, 3]


def test_sub_end_greater_lenght() -> None:
    """End value is greater than lenght."""
    list_z: list[int] = [0, 1, 2]
    assert sub(list_z, 0, 4) == []