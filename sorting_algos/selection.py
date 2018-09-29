# Insertion sort
# Go through a list comparing values to find the lowest value, take that value and place it at the corresponding index.
# Continue till all values are sorted accordingly.
import random


def really_big_list(numb):
    big_list = []
    counter = numb
    while counter:
        ran_num = random.randint(0, numb)
        big_list.append(ran_num)
        counter -= 1

    return big_list


# print(unsorted_list)

# for i in unsorted_list:
#     temp_val = unsorted_list[0]
#     position = 0
#
#     while position <= len(unsorted_list) - 1:
#         # if temp_val == unsorted_list[0]:
#         #     position += 1
#         if temp_val > unsorted_list[position + 1]:
#             temp_val = unsorted_list[position]
#             position += 1
#     print(unsorted_list)

# really_big_list(5)
#
unsorted_list = [2, 3, 10, 1, 4]
# print(unsorted_list)
# # Take a list and get the value of the first index
# for index in range(len(unsorted_list)):
#     for smallest in range(unsorted_list + 1, len(unsorted_list)):
#         if unsorted_list[index] > unsorted_list[smallest]:
#             unsorted_list[index], unsorted_list[smallest] = unsorted_list[smallest], unsorted_list[index]
# print(unsorted_list)
    # i = 0  # Index
    # p = index  # Position
    # v = None  # Value
# Find the smallest value in the list and remember the index

# Swap the first index value for the smallest index value
# increment to the next index and repeat


def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""

    if len(array) <= 1:  # base case
        return array

    # divide array in half and merge sort recursively
    half = len(array) // 2
    left = merge_sort(array[:half])
    right = merge_sort(array[half:])

    return merge(left, right)


print(merge_sort(really_big_list(10000)))
