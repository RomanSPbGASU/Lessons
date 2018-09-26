while 1:
    try:
        letterCount = int(input("Введите количество символов в пароле: "))
    except ValueError:
        print("Ошибка. Необходимо ввести число")
    import random
    password = (random.sample("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", letterCount)) # выбор не полностью случаен, так как выбранные элементы не могут повторяться
    print("Ваш пароль: ", ''.join(password))
    if input("Попробуем снова? (д/н)") == "н":
        break