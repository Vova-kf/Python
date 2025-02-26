number = int(input("Введіть число секунд (від 0 до 8640000): "))

if number < 0 or number>= 8640000:
    print("Error")
else:
    days, remainder = divmod(number, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)


    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif days % 10 in (2, 3, 4) and days % 100 not in (12, 13, 14):
        day_word = "дні"
    else:
        day_word = "днів"


    number_time = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    print(f"{days} {day_word}, {number_time}")
