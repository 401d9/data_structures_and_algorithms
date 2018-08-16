
from .array_shift import insert_shift_array
import pytest


def test_reverse_array_module_exists():
    """
    This is testing to make sure that the function exists
    """
    assert insert_shift_array


def test_array_for_odd():
    """
    This is checking the function against an odd number list length which tests how it deals with finding the middle of
     the list
     """

    expected = [1, 2, 3, 4, 5]
    actual = insert_shift_array([1, 2, 4, 5], 3)
    assert expected == actual


def test_array_for_even():
    """
    This will test an even numbered array to check where it starts its checks.
    """
    expected = [1, 2, 3, 4]
    actual = insert_shift_array([1, 2, 4], 3)
    assert expected == actual


def test_array_character_even():
    """This adds values to the check other than numbers, as the function should be able to take in many different
    types
    """
    expected = ['a', 'b', 'c', 'd']
    actual = insert_shift_array(['a', 'b', 'd'], 'c')
    assert expected == actual


def test_array_character_odd():
    """
       This will test an odd numbered array to check where it starts its checks.
       """
    expected = ['a', 'b', 'c', 'd', 'e']
    actual = insert_shift_array(['a', 'b', 'd', 'e'], 'c')
    assert expected == actual
