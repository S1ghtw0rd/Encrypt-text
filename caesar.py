ENGLISH = "abcdefghijklmnopqrstuvwxyz"
RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def _encrypt_caesar(text, shift, alphabet):
    result = ""
    for letter in text:
        lower = letter.lower()
        if lower in alphabet:
            new_letter = (ord(letter) + shift) % len(alphabet)

        if letter.isupper():
            result += chr(new_letter)
        else:
            result += letter
    return result

def encrypt_caesar_russian(text, shift):
    return _encrypt_caesar(text, shift, RUSSIAN)

def encrypt_caesar_english(text, shift):
    return _encrypt_caesar(text, shift, ENGLISH)
