def calculator():
    while True:
        number_one = float(input('Перше число: '))
        arithmetic_sign = input('Яка операція (+, -, *, /): ')
        number_two = float(input('Друге число: '))

        if arithmetic_sign == '+':
            result = number_one + number_two
        elif arithmetic_sign == '-':
            result = number_one - number_two
        elif arithmetic_sign == '*':
            result = number_one * number_two
        elif arithmetic_sign == '/':
            if number_two == 0:
                print('Error!!! На нуль ділити не можна!!!')
                return
            result = number_one / number_two
        else:
            print('Error!!!')
            return

        print('Дорівнює: ' + str(result))
        action = input("Продовжити? (y/n): ").lower()
        if action != "y":
            break
calculator()

