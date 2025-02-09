# first_list = [1, 3, 4, 0, 5, 0, 7, 0, 0, 2]
#
# first_list.sort(reverse=False)
#
# print(first_list)


first_list = [[1, 2, 3], [4, 5, 6]]
tmp = first_list.copy()
print(id(first_list) == id(tmp))  #  False