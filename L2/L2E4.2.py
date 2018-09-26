from random import *
while 1:
    try:
        letterCount = int(input("Введите количество символов в пароле: "))
    except ValueError:
        print("Ошибка. Необходимо ввести число")
    pw = ''
    for i in range(letterCount):
        pw += (choice([chr(randint(0x41, 0x5A)), chr(randint(0x61, 0x7A)), chr(randint(0x30, 0x39))]))
    print("Ваш пароль: ", pw)
    if input("Попробуем снова? (д/н)") == "н":
        break