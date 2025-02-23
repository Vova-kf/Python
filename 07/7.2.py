def correct_sentence(text):

    text = text[0].upper() + text[1:]
    if text[-1] !='.':
        text += '.'
    return text

correct_sentence(text= 'Greetings, friends.')
print(correct_sentence(text= 'Greetings, friends.'))