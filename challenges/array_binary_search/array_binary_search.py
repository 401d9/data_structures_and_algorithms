from bisect import bisect_left


def binary_search(a, x, lo=0, hi=None):
    """
       Binary search for an item in a sorted list.

        Takes in only a and x and provides lo and hi arguments
       Args:
           a:     A sorted list
           x:  The item to search for
       Returns:
           True or False
        Bisect:
            lo=0 declares where to start in the array
            hi=gets set to the length of the array
       """
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1


"""
Credits:
   Docstring example: https://codereview.stackexchange.com/questions/147136/binary-search-a-sorted-list-of-integers
   Bisection example: https://stackoverflow.com/questions/212358/binary-search-bisection-in-python
"""
numb_array=[1, 2, 3, 5, 6, 7, 8, 9]
print(binary_search(numb_array, 1))
print(binary_search(numb_array, 4))
print(binary_search(numb_array, 9))

