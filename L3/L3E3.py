from L3E1 import tb_print
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
tb_print.width = 40
tb_print(chr(0x305) * tb_print.width)
tb_print(" Начальная сумма = %.2f рублей" % init)
tb_print(" Процентная ставка = %.2f %% год" % rate)
tb_print(" Срок инвестирования = %d лет" % term)
tb_print("_" * tb_print.width)
print(("{:<{}}" + "{:^{}}" * 2).format("", 9, "Простой процент", 20, "Сложный процент", 41))
def fm_print(*tuple):
    fm_print.col_w = 19 # ширина основных столбцов
    col_width = [fm_print.col_w//2, *[fm_print.col_w//4*3, fm_print.col_w] * 2]
    fm_args = []
    for i in range(len(col_width if len(col_width) < len(tuple) else tuple)):
        l = [tuple[i]] + [col_width[i]]
        for j in l:
            fm_args.append(j)
    print(("{:<{}}" + "{:<{}}" * 4).format(*fm_args))
fm_print("", *(("Сумма, руб.", "Доход за год, руб.") * 2))
simple = complex = init
for i in range(term):
    in_sim = simple
    in_com = complex
    simple += init * rate / 100
    complex *= (1 + rate / 100)
    in_sim = simple - in_sim
    in_com = complex - in_com
    fm_print("%d-й год" % (i + 1), str(round(simple, 2)), str(round(in_sim, 2)), str(round(complex, 2)), str(round(in_com, 2)))

