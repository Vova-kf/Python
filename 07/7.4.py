def common_elements():

    one_lst = [x for x in range(100) if x % 3 == 0]
    two_lst = [x for x in range(100) if x % 5 == 0]

    list_three = set(one_lst) & set(two_lst)


    return list_three


common_elements()
print(common_elements())