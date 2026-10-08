ENGLISH = "abcdefghijklmnopqrstuvwxyz"
ENGLISH_REVERSED = "zyxwvutsrqponmlkjihgfedcba"

RUSSIAN = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
RUSSIAN_REVERSED = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

def decrypt_and_encrypt_atbash_english(text):
    result = ""
    for letter in text:
        lower = letter.lower()
        if lower in ENGLISH:
            index = ENGLISH.index(lower)
            new_letter = ENGLISH_REVERSED[index]
            if letter.isupper():
                new_letter = new_letter.upper()
            result += new_letter
        else:
            result += letter
    return result

def decrypt_and_encrypt_atbash_russian(text):
    result = ""
    for letter in text:
        lower = letter.lower()
        if lower in RUSSIAN:
            index = RUSSIAN.index(lower)
            new_letter = RUSSIAN_REVERSED[index]
            if letter.isupper():
                new_letter = new_letter.upper()
            result += new_letter
        else:
            result += letter
    return result