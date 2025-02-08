first_list = [1, 2, 3, 4, 5, 6, 7]

list_length = len(first_list)

split_list = (list_length + 1) // 2

new_list_one = first_list[:split_list]
new_list_two = first_list[split_list:]

print([new_list_one, new_list_two])


