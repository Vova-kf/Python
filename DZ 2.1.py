number = int(input("Ведіть число: "))

# Робимо математичні дії ділимо наше число і заокруглюємо до цілого.
number_one= number // 1000            # ведене число ділимо на 1000 і беремо перше число від результату
number_two = (number % 1000) // 100   # ведене число ділимо на 100 і беремо перше число від результату
number_three = (number % 100) // 10   # ведене число ділимо на 10 і беремо перше число від результату
number_four = number % 10             # беремо залишок від числа і заокруглюємо його до цілого



print(number_one)
print(number_two)
print(number_three)
print(number_four)


