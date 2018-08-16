from .array_binary_search import binary_search
import test


def test_NaN():
    expected = 'unexpected entry'
    actual = binary_search([1, 2, 4, 6, 8, 10, 34], 'a')
    assert expected == actual


def test_out_array():
    """
    Test for inputs that are not with in the array for correct return
    """
    expected = -1
    actual = binary_search([1, 2, 4, 6, 8, 10, 34], 11)
    assert expected == actual


def test_large_array():
    """
    This takes in a large array(relatively) as a third check until I think of better tests!
    """
    expected = 13
    actual = binary_search([1, 2, 4, 6, 8, 10, 34, 53, 64, 99, 234, 275, 767, 4675, 6975, 68958], 4675)
    assert expected == actual
