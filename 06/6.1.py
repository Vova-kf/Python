import string

a = input('Ведіть дві букви через - :' ).split("-")

letter = string.ascii_letters

one_letter = letter.index(a[0])
two_letter = letter.index(a[1])

new_lst = letter[one_letter:two_letter +1]

print(new_lst)

