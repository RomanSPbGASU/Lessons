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
col_w = 18  # ширина основных столбцов
print(("{:<{}}" + "{:^{}}" * 2).format("", col_w/2, "Простой процент", col_w*2, "Сложный процент", col_w*2), end = "")
def fm_print(*tuple):
    col_width = [col_w/2, *[col_w] * 4]
    print(col_width)
    print(("{:>{}}" + "{:^{}}" * 4).format(*tuple))
fm_print("", col_w/2, *(("Сумма, руб.", col_w, "Доход за год, руб.", col_w) * 2))
simple = complex = init
for i in range(term):
    in_sim = simple
    in_com = complex
    simple += init * rate / 100
    complex *= (1 + rate / 100)
    in_sim = simple - in_sim
    in_com = complex - in_com
    print("%d-й год \t" % (i + 1), round(simple, 2), "\t", round(in_sim, 2), "\t", round(complex, 2), "\t", round(in_com, 2))

