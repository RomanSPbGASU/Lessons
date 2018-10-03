from re import compile, search, match
print("Введите слово 'stop' для получения результата")
res = 0
while 1:
    ptrn = compile(r"[+-]*[0-9]+") # шаблон для ввода числа в C++ стиле
    stop = compile(r"stop")
    try:
        inp = input("Введите целое число: ")
        if stop.search(inp):
           break
        if inp == '':
            raise IOError()
        num = int(ptrn.match(inp).string)
        res += num
    except (ValueError, AttributeError):
        print("Необходимо ввести число, а не строку!!!")
    except IOError:
        print("Вы не ввели значение!")
print("Сумма введённых чисел равна: ", res)