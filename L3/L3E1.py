from L1.L1E1 import get_yield


def tb_print(*values):
    """Печатает строку посередине окна консоли, обрамляя ее символами '|'

    Для задания ширины обрамления можно использовать поле .width
    """
    try:
        tb_print.width
    except AttributeError:
        tb_print.width = 40
    print(" " * 18, "|{0:{width}}|".format(*values, width=tb_print.width),
          sep="")


def fm_print(*values):
    form = "%-20s %-18s %-18s"
    print(form % values)


if __name__ == '__main__':
    variables = init, rate, term = [10000, 10, 5]
    in_text = ("Введите начальную сумму, ₽: ", "Введите размер ставки, %: ",
               "Введите срок инвестирования, лет: ")
    p_vars = [" Сумма вклада = %.f ₽ ", " Процентная ставка = %.f%% ",
              " Срок инвестирования = %d лет "]
    t = (float, float, int)
    for i in range(3):
        try:
            variables[i] = t[i](input(in_text[i]))
        except ValueError:
            p_vars[i] += "(default) "
        finally:
            p_vars[i] = p_vars[i] % variables[i]
    tb_print.width = 39
    tb_print(chr(0x2ed) * tb_print.width)
    for line in p_vars:
        tb_print(line)
    tb_print("_" * tb_print.width)
    print()
    init, rate, term = variables
    finSimple = init * (1 + rate / 100 * term)
    finCom = init * (1 + rate / 100) ** term
    fm_print("", "Простой процент", "Сложный процент")
    fm_print("Начальная сумма, ₽:", round(init, 1), round(init, 1))
    fm_print("Конечная сумма, ₽:", round(finSimple, 1), round(finCom, 1))
    incSimple = finSimple - init
    incCom = finCom - init
    fm_print("Доход, руб:", round(incSimple, 1), round(incCom, 1))
    fm_print("Доходность, % год.:", round(get_yield(incSimple, init, term), 1),
             round(get_yield(incCom, init, term), 1))
