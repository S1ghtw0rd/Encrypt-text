ENGLISH = "abcdefghijklmnopqrstuvwxyz"
RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def _encrypt_caesar(text, shift, alphabet):
    result = ""
    for letter in text:
        lower = letter.lower()
        if lower in alphabet:
            index = alphabet.index(lower)
            cipher = (index + shift) % len(alphabet)
            new_letter = alphabet[cipher]
            if letter.isupper():
                new_letter = new_letter.upper()
            result += new_letter
        else:
            result += letter
    return result

def encrypt_caesar_russian(text, shift):
    return _encrypt_caesar(text, shift, RUSSIAN)

def encrypt_caesar_english(text, shift):
    return _encrypt_caesar(text, shift, ENGLISH)
