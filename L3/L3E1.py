vars = init, rate, term = [10000, 10, 5]
itext = ("Введите начальную сумму, ₽: ", "Введите размер ставки, %: ", "Введите срок инвестирования, лет: ")
pvars = [" Сумма вклада = %.f ₽ ", " Процентная ставка = %.f%% ", " Срок инвестирования = %d лет "]
t = (float, float, int)
for i in range(3):
    try:
        vars[i] = t[i](input(itext[i]))
    except:
        pvars[i] += "(default) "
    finally:
        pvars[i] = pvars[i] % vars[i]
def tb_print(*list):
    try:
        tb_print.width
    except AttributeError:
        tb_print.width = 40
    print(" " * 18, "|{0:{width}}|".format(*list, width = tb_print.width), sep = "")
tb_print.width = 39
tb_print(chr(0x305) * tb_print.width)
for line in pvars:
    tb_print(line)
tb_print("_" * tb_print.width)
print()
init, rate, term = vars
finSimple = init * (1 + rate / 100 * term)
finCom = init * (1 + rate / 100) ** term
def fm_print(*tuple):
    form = "%-20s%-18s%-18s"
    print(form % tuple)
fm_print("", "Простой процент", "Сложный процент")
fm_print("Начальная сумма, ₽:", round(init, 1), round(init, 1))
fm_print("Конечная сумма, ₽:", round(finSimple, 1), round(finCom, 1))
incSimple = finSimple - init
incCom = finCom - init
fm_print("Доход, руб:", round(incSimple, 1), round(incCom, 1))
def getYield(income):
    return income / init * 1 / term * 100
fm_print("Доходность, % год.:", round(getYield(incSimple), 1), round(getYield(incCom), 1))

