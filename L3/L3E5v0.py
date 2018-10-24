print("Введите слово 'stop' для получения результата")
res = 0
while 1:
    try:
        inp = input("Введите целое число: ")
        if inp == '':
            raise IOError()
        if inp == "stop":
            break
        num = int(inp)
        res += num
    except ValueError:
        print("Необходимо ввести число, а не строку!!!")
    except IOError:
        print("Вы не ввели значение!")
print("Сумма введённых чисел равна: ", res)
