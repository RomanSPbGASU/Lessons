indict = {"initial": None, "final": None, "term": None}
func_in_list = [lambda: float(input("Введите начальную сумму, ₽ = ")),
                lambda: float(input("Введите конечную сумму, ₽ = ")),
                lambda: int(input("Введите срок инвестирования, лет = "))]
i = 0
for key in indict:  # добьёмся от пользователя ввода корректных данных
    while 1:
        try:
            indict[key] = func_in_list[i]()
            i += 1
            break
        except ValueError:
            print("\tОшибка. Некорректный ввод")
print("\t" * 11, "Простой процент   Сложный процент")
print("Размер необходимой процентной ставки, % год.\t", end=" ")
percent = (indict["final"] / indict["initial"] - 1) * 100 / indict["term"]
print(round(percent, 2), "\t\t  ", end=" ")
prop = ((indict["final"] / indict["initial"]) ** (1 / indict["term"]) - 1)
percent = prop * 100
print(round(percent, 2))
