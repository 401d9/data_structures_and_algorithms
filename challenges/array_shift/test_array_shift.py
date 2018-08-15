
from .array_shift import insert_shift_array
import pytest


def test_reverse_array_module_exists():
    assert insert_shift_array


def test_array_for_odd():
    expected = [1, 2, 3, 4, 5]
    actual = insert_shift_array([1, 2, 4, 5], 3)
    assert expected == actual


def test_array_for_even():
    expected = [1, 2, 3, 4]
    actual = insert_shift_array([1, 2, 4], 3)
    assert expected == actual


def test_array_character_even():
    expected = ['a', 'b', 'c', 'd']
    actual = insert_shift_array(['a', 'b', 'd'], 'c')
    assert expected == actual


def test_array_character_odd():
    expected = ['a', 'b', 'c', 'd', 'e']
    actual = insert_shift_array(['a', 'b', 'd', 'e'], 'c')
    assert expected == actual
