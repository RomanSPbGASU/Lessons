indict = {"initial": None, "rate": None, "term": None}
funcinlist = [lambda : float(input("Введите начальную сумму, ₽ = ")),
              lambda : float(input("Введите размер ставки, % год = ")),
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
print("\nНачальная сумма = %.2f рублей" % indict["initial"])
print("Процентная ставка = %.2f %% год" % indict["rate"])
print("Срок инвестирования = %d лет" % indict["term"])
print("\t" * 2, "Простой процент\t\t Сложный процент")
print("\t" * 2, "Сумма, руб. Доход за год, руб.  Сумма, руб. Доход за год, руб.")
simple = complex = indict["initial"]
for i in range(indict["term"]):
    in_sim = simple
    in_com = complex
    simple += indict["initial"] * indict["rate"] / 100
    complex *= (1 + indict["rate"] / 100)
    in_sim = simple - in_sim
    in_com = complex - in_com
    print("%d-й год \t" % i, round(simple, 2), "\t", round(in_sim, 2), "\t", round(complex, 2), "\t", round(in_com, 2))

