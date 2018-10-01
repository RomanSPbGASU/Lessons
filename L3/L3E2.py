itext = ("Введите начальную сумму, ₽ = ", "Введите размер ставки, % = ", "Введите срок инвестирования, лет = ")
t = (float, float, int)
var = []
i = 0
while i <= 2:
    try:
      var.append(t[i](input(itext[i])))
    except (ValueError):
        print('\x083', end= '')
        print("\x08\x08Ошибка. Некорректный ввод")
        continue
    else:
        i += 1
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
