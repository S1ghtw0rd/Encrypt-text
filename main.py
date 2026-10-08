import time
from caesar import encrypt_caesar_english, encrypt_caesar_russian
from atbash import decrypt_and_encrypt_atbash_english, decrypt_and_encrypt_atbash_russian

def russian_menu():
    text = input("Напишите текст (Без цифр и знаков препинания): ")
    time.sleep(3)

    print()
    print("Выберите как дешифровать текст (Если ответ получился неверным попробуйте другую кодировку)")
    print("1. Шифр Цезаря")
    print("2. Шифр Атбаш")
    time.sleep(2)
    choice_cipher = int(input("Действие: "))

    if choice_cipher == 1:
        shift = int(input("Сдвиг (Укажите цифру): "))
        result = encrypt_caesar_russian(text, shift)
        print(f"Шифр Цезаря - {result}")


print("Choice language")
print("1. Русский")
print("2. English")
print()
choice_language = int(input("Choice (Выберите): "))
time.sleep(2)

if choice_language == 1:
    russian_menu()

