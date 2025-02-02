def calculator():
    number_one = float(input('Перше число: '))
    variant = input('Яка операція (+, -, *, /): ')
    number_two = float(input('Друге число: '))

    if variant == '+':
        resultat = number_one + number_two
    elif variant == '-':
        resultat = number_one - number_two
    elif variant == '*':
        resultat = number_one * number_two
    elif variant == '/':
        if number_two == 0:
            print('Помилка! На нуль ділити не можна!!!')
            return
        resultat = number_one / number_two
    else:
        print('Помилка! Невідома операція.')
        return

    print('Дорівнює: ' + str(resultat))

calculator()

