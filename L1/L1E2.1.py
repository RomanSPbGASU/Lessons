indict = {"initial": None, "rate": None, "term": None}
funcinlist = [lambda : float(input("Введите начальную сумму, ₽ = ")),
              lambda : float(input("Введите размер ставки, % = ")),
              lambda : int(input("Введите срок инвестирования, лет = "))]
i = 0
for key in indict:   # добьёмся от пользователя ввода корректных данных
    while 1:
        try:
            indict[key] = funcinlist[i]()
            i += 1
            break
        except:
            print("\tОшибка. Некорректный ввод")
print("\t\t\t\t\tСхема начисления процентов")
print("\t\t\tЕжемесячно     Ежеквартально  Раз в полгода  Ежегодно")
lines = [["Начальная сумма, ₽:", lambda : indict["initial"], [None] * 4],
["Конечная сумма, ₽:", lambda : indict["initial"] * (1 + indict["rate"] / 100 * [1,3,6,12][i] / 12) ** (indict["term"] * 12 / [1,3,6,12][i]), [None] * 4],
["Доход, руб:", lambda : lines[1][2][i] - indict["initial"], [None] * 4],
["Доходность, % год.:", lambda : lines[2][2][i] / indict["initial"] / indict["term"] * 100, [None] * 4]] # данные
for title, func, output in lines: # движок
    print(format(title, "22"), end = "\t")    # поток выводится не сразу а только после символа конца строки
    for i in range(4):
        output[i] = func()
        print(format(output[i], "<15.2f"), end = "")
    print()