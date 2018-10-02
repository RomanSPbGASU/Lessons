#itext = ("Введите начальную сумму, ₽ = ", "Введите размер ставки, % = ", "Введите срок инвестирования, лет = ")
#t = (float, float, int)
#var = []; i = 0
#while i <= 2:
#    try:
#      var.append(t[i](input(itext[i])))
#    except (ValueError):
#        print("Ошибка. Некорректный ввод")
#        continue
#    else:
#        i += 1
init, rate, term = 10000, 10, 5
print("{0:^81}".format("Схема начисления процентов"), end = "")
def fm_print(*tuple):
    print(("{:<20}" + "{:<15}" * 4).format(*tuple))
fm_print("", "Ежемесячно", "Ежеквартально", "Раз в полгода", "Ежегодно")
fm_print("Начальная сумма, ₽:", *([round(init, 1)] * 4))
fm_print("Конечная сумма, ₽:", )

lines = [["Конечная сумма, ₽:", lambda : init * (1 + rate / 100 * [1,3,6,12][i] / 12) ** (term * 12 / [1,3,6,12][i]), [None] * 4],
["Доход, руб:", lambda : lines[1][2][i] - init, [None] * 4],
["Доходность, % год.:", lambda : lines[2][2][i] / init / term * 100, [None] * 4]]
for title, func, output in lines:
    print(format(title, "22"), end = "\t")
    for i in range(4):
        output[i] = func()
        print(format(output[i], "<15.2f"), end = "")
    print()
