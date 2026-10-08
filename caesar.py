ENGLISH = "abcdefghijklmnopqrstuvwxyz"
RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def encrypt_caesar(text, shift, alphabet):
    for letter in text:
        lower = letter.lower()
        if lower in alphabet:
            new_letter = (chr(lower) + shift) % len(alphabet)
            