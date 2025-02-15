number = int(input('Введіть число: '))

while number > 9:
    my_list = [int(d) for d in str(number)]  #
    result = my_list[0]
    for a in my_list[1:]:
        result *= a

    number = result

print(number)


