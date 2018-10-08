def selection_sort(unsorted):
    """
    Selection sort takes a list and sorts if from lowest to greatest value. For each index check the value at that
    index against all the unchecked indexes for the lowest value and swap the current index value for the lowest
    value found. Example: [2, 5, 3] will become [2, 3, 5] via [2, 5, 3] -> [2, 3, 5] -> [2, 3, 5] which goes through
    the whole list.

    ARG:
        An unsorted list
    OUTPUT:
        A value sorted list
    """

    for i in range(len(unsorted)):  # This gives you the Index of the list over the Value
        need_low_value = unsorted[i]
        index_at = i
        for v in range(i, len(unsorted)):
            if unsorted[v] < need_low_value: 
                need_low_value, index_at = unsorted[v], v  # swap in place
            
                temp_value = unsorted[i]
                unsorted[i] = need_low_value
                unsorted[index_at] = temp_value
            
    return unsorted


