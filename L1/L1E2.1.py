indict = {"initial": None, "rate": None, "term": None}
funcinlist = [lambda : float(input("Введите начальную сумму, ₽ = ")),\
              lambda : float(input("Введите размер ставки, % = ")),\
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
for i in range(90): print(end="_")
print(None)
print("\t\t\t\t\tСхема начисления процентов")
print("\t\t\t Ежемесячно\tЕжеквартально\tРаз в полгода\tЕжегодно")
lines = []
out = list(range(4))
# данные
lines.append(["Начальная сумма, ₽:\t ", lambda garb : indict["initial"], None, out])
lines.append(["Конечная сумма, ₽:\t ", lambda period : indict["initial"] * (1 + indict["rate"] / 100 * period / 12) ** (indict["term"] * 12 / period), (1,3,6,9), out])
lines.append(["Доход, руб:\t\t ", lambda final : final - indict["initial"], lines[1][2], out])
lines.append(["Доходность, % год.:\t ", lambda period: lines[2][2] / indict["initial"] / (indict["term"] * 12 / period) * 100, lines[1][2], out])
# движок
for title, func, input, output in lines:
    print(title, end = "\t")    # поток выводится не сразу а только после символа конца строки
    for i in range(4):
        output[i] = func(input[i])
        print(result[i], end = "\t")
    print()





