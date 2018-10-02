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
print(("{:<{}}" + "{:<{}}" * 2).format("", 8, "Простой процент", 30, "Сложный процент", 30))
print("".format("Сумма, руб.", "Доход за год, руб.", "Сумма, руб.", "Доход за год, руб."))
simple = complex = init
for i in range(term):
    in_sim = simple
    in_com = complex
    simple += init * rate / 100
    complex *= (1 + rate / 100)
    in_sim = simple - in_sim
    in_com = complex - in_com
    print("%d-й год \t" % i, round(simple, 2), "\t", round(in_sim, 2), "\t", round(complex, 2), "\t", round(in_com, 2))

