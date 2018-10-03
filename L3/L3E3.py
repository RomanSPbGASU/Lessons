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
init, rate, term = 10000, 15, 5
print("\nНачальная сумма = %.2f рублей" % init)
print("Процентная ставка = %.2f %% год" % rate)
print("Срок инвестирования = %d лет" % term)
print(("{:<{}}" + "{:^{}}" * 2).format("", 9, "Простой процент", 36, "Сложный процент", 36), end = "")
def fm_print(*tuple):
    fm_print.col_w = 18 # ширина основных столбцов
    col_width = [fm_print.col_w/2, *[fm_print.col_w] * 4]
    z = [zip(col_width, tuple)]
    print(z)
    print(("{:>{}}" + "{:<{}}" * 4).format(zip(col_width, tuple)))
fm_print("", *(("Сумма, руб.", "Доход за год, руб.") * 2))
simple = complex = init
for i in range(term):
    in_sim = simple
    in_com = complex
    simple += init * rate / 100
    complex *= (1 + rate / 100)
    in_sim = simple - in_sim
    in_com = complex - in_com
    print("%d-й год \t" % (i + 1), round(simple, 2), "\t", round(in_sim, 2), "\t", round(complex, 2), "\t", round(in_com, 2))

