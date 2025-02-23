import keyword
import string
variable = input("Введіть ім'я змінної: ")

if variable == "":
    print(False)
    exit()
if variable in keyword.kwlist:
    print(False)
    exit()
if variable[0].isdigit():
    print(False)
    exit()
for a in variable:
    if a.isupper():
        print(False)
        exit()
    if a.isspace():
        print(False)
        exit()
    if a in string.punctuation and a != "_":
        print(False)
        exit()
if variable.count("_") > 1:
    print(False)
    exit()


print(True)
