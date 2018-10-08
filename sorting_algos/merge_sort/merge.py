sample_list = [6, 5, 1, 9, 0, 2, 10]


def merge_split(unsort_list):

    if len(unsort_list) < 2:
        return unsort_list

    middle = len(unsort_list) // 2
    left = merge_split(unsort_list[:middle])
    right = merge_split(unsort_list[middle:])

    return merge(left, right)


def merge(list_1, list_2):

    merged = []

    ones, twos = 0, 0

    while ones < (len(list_1)) and twos < (len(list_2)):
        if list_1[ones] < list_2[twos]:
            merged.append(list_1[ones])
            ones += 1
        else:
            merged.append(list_2[twos])
            twos += 1

    if ones > (len(list_1) - 1):
        merged.extend(list_2[twos:])
        return merged
    else:
        merged.extend(list_1[ones:])
        return merged


print(merge_split(sample_list))
