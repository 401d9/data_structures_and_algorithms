# from bisect import bisect_left
#
#
# def binary_search(a, x, lo=0, hi=None):
#     """
#        Binary search for an item in a sorted list.
#
#
#        Args:
#            a:  A sorted list
#            x:  The item to search for
#            lo: (Pre-set value) The lowest index to start in the passed in list
#            hi: (Pre-set value) This starts at None to check that list has a value. It then checks length for the end of
#             the list
#        Returns:
#            True or False
#         Bisect:
#             lo=0 declares where to start in the array
#             hi=gets set to the length of the array
#        """
#     hi = hi if hi is not None else len(a)
#     pos = bisect_left(a, x, lo, hi)
#     return pos if pos != hi and a[pos] == x else -1
#
#
# """
# Credits:
#    Docstring example: https://codereview.stackexchange.com/questions/147136/binary-search-a-sorted-list-of-integers
#    Bisection example: https://stackoverflow.com/questions/212358/binary-search-bisection-in-python
# """
numb_array = [1, 2, 3, 5, 6, 7, 8, 9]


# print(binary_search(numb_array, 1))
# print(binary_search(numb_array, 4))
# print(binary_search(numb_array, 9))


def binary_search(array_arg, search_numb):
    first = 0
    last = len(array_arg) - 1
    found = False

    while first <= last and not found:
        mid_point = (first + last) // 2
        if array_arg[mid_point] == search_numb:
            found = mid_point
        else:
            if search_numb < array_arg[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    if found == False:
        found = -1
    return found


x = int(input('input: '))
print(binary_search(numb_array, x))
