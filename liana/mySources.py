from random import randint

def get_token(length):
    string_chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    text = ""
    for i in range(length):
        new_number = randint(61)
        text += string_chars[new_number]

    return text
