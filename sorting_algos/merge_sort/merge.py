sample_list = [6, 5 , 1, 9, 0, 2, 10]

def list_split(unsort_list):

    middle = (len(unsort_list)) // 2
    left =  unsort_list[:middle]
    right = unsort_list[middle:]
    return left, right 




def merge(list_1, list_2):

    print(list_1, list_2)
    # if len(list_1) < 2 or len(list_2) < 2:
    #     pass

    # else:
    #     inf_split = merge(*list_split(sample_list))
    #     print (inf_split)



merge(*list_split(sample_list))                                                                                                                    