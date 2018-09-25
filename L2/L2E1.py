indict = {"initial": 50000, "rate": 7.5, "term": 15}
#funcinlist = [lambda : float(input("Введите начальную сумму, ₽ = ")),
#              lambda : float(input("Введите размер ставки, % год = ")),
#              lambda : int(input("Введите срок инвестирования, лет = "))]
#i = 0
#for key in indict:   # добьёмся от пользователя ввода корректных данных
#    while 1:
#        try:
#            indict[key] = funcinlist[i]()
#            i += 1
#            break
#        except:
#            print("\tОшибка. Некорректный ввод")
print("\nНачальная сумма = %.2f рублей" % indict["initial"])
print("Процентная ставка = %.2f %% год" % indict["rate"])
print("Срок инвестирования = %d лет" % indict["term"])
print("\t\t\t\t\t\t Простой процент\t   Сложный процент")
print("Сумма, руб.   Доход за год, руб.   Сумма, руб.   Доход за год, руб.")
simple = complex = indict["initial"]
for i in range(indict["term"]):
    in_sim = simple
    in_com = complex
    simple *=  (1 + indict["rate"] / 100 * indict["term"])
    complex *= (1 + indict["rate"] / 100) ** indict["term"]
    in_sim -= -simple
    print("%d-й год" % i, simple, in_sim, complex, in_com)