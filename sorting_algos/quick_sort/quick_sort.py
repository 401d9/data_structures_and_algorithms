

def quick_sort(arg_list):
    """ Function for implementing quick sort. """

    len_check = len(arg_list)

    if len_check <= 1:
        return arg_list
    else:
        pivot = arg_list[0]
        right = [i for i in arg_list[1:] if i > pivot]
        left = [i for i in arg_list[1:] if i <= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


sample_test_list = [5, 4, 2, 1, 0]

print(quick_sort(sample_test_list))
