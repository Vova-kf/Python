import string
text = 'Привіт,,,, я вивчаю Python!!!'
# text =input('Ведіть свій текст, для перетворення на хештег: ')

new_text = " "
for a in text:
    if a not in string.punctuation:
        new_text += a.capitalize()

new2_text = new_text.title().split()
hashtags = '#'+ "".join(new2_text)




print(hashtags[:140])