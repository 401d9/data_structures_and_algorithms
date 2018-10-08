from merge import merge_split
import random
import pytest


@pytest.fixture
def one_list():
    return [10, 1, 53, 200, 12983981, 313, 7820]


@pytest.fixture
def two_random_large_list():
    """Creates a list with 12345 indices with random values to test sorts! """
    two_list = []
    count = 12345

    while count:
        random_numbers = random.randint(0, 12345)
        count -= 1
    return two_list


def test_merge_split():
    """Check to make sure there is an actual function to call"""
    assert merge_split


def test_repeated_numbers():
    """ Test to see how a sorting algo deals with the same number repeatedly """

    repeat_number_list = merge_split([2, 2, 2, 2, 2, 2, 2, 4])

    assert all(repeat_number_list[i] <= repeat_number_list[i+1] for i in range(len(repeat_number_list) - 1))


def test_huge_list():
    """Calls another function to test sorting algo against a really large randomly generated list"""

    huge_list = merge_split([two_random_large_list()])

    assert all(huge_list[i] <= huge_list[i+1] for i in range(len(huge_list) - 1))


def test_fixed_list():
    """ Uses a small static list for easy verification of a working sort algo"""

    fixed = merge_split([one_list()])

    assert all(fixed[i] <= fixed[i+1] for i in range(len(fixed)-1))
