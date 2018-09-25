indict = {"initial": None, "final": None, "term": None}
funcinlist = [lambda : float(input("Введите начальную сумму, ₽ = ")),
              lambda : float(input("Введите конечную сумму, ₽ = ")),
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
print("\t\t\t\t\t\t Простой процент   Сложный процент")
import math
print("Размер необходимой процентной ставки, % год.\t", round((indict["final"] / indict["initial"] - 1) * 100 / indict["term"], 2), "\t\t  ", round((math.pow(indict["final"] / indict["initial"], 1 / indict["term"]) - 1) * 100, 2))