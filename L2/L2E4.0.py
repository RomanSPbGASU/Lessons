try:
    letterCount = int(input("Введите количество символов в пароле: "))
except ValueError:
    print("Ошибка. Необходимо ввести число")
import random
password = ""
for i in range(letterCount):
    password += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
print("Ваш пароль: ", password)