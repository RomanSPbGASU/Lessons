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
import math
print("Размер необходимой процентной ставки, % год.\t", round((indict["final"] / indict["initial"] - 1) * 100 / indict["term"], 2), "\t\t  ", round((math.pow(indict["final"] / indict["initial"], 1 / indict["term"]) - 1) * 100, 2))
