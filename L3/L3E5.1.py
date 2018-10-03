from re import compile, search
print("Введите слово 'stop' для получения результата")
res = 0
while 1:
    ptrn = re.compile(r"[+-]*[0-9]+") # шаблон для ввода числа в C++ стиле
    stop = re.compile(r"stop")
    try:
        inp = input("Введите целое число: ")
        num = ptrn.search(inp)
        if num != None:
            res += num
        if inp == '':
            raise IOError()
        if stop.search(inp):
           break
    except ValueError:
        print("Необходимо ввести число, а не строку!!!")
    except IOError:
        print("Вы не ввели значение!")
print("Сумма введённых чисел равна: ", res)