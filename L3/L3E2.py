itext = ("Введите начальную сумму, ₽ = ", "Введите размер ставки, % = ", "Введите срок инвестирования, лет = ")
t = (float, float, int)
var = []; i = 0
while i <= 2:
    try:
      var.append(t[i](input(itext[i])))
    except (ValueError):
        print("Ошибка. Некорректный ввод")
        continue
    else:
        i += 1
init, rate, term = var
print("{0:^81}".format("Схема начисления процентов"), end = "")
def fm_print(*tuple):
    print(("{:<20}" + "{:<15}" * 4).format(*tuple))
fm_print("", "Ежемесячно", "Ежеквартально", "Раз в полгода", "Ежегодно")
fm_print("Начальная сумма, ₽:", *([round(init, 1)] * 4))
month = [1, 3, 6, 9]
fin = [round(init * (1 + rate / 100 * month[i] / 12) ** (term * 12 / month[i]), 1) for i in range(4)]
fm_print("Конечная сумма, ₽:", *fin)
inc = [round(fin[i] - init, 1) for i in range(4)]
fm_print("Доход, руб:", *inc)
fm_print("Доходность, % год.:", *[round(inc[i] / init / term * 100, 1) for i in range(4)])