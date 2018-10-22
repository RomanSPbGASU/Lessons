def get_final_amount(month_in_period):
    period_count = (investmentTerm * 12 / month_in_period)
    fa = initialAmount
    fa *= (1 + rateAmount / 100 * month_in_period / 12) ** period_count
    return fa


def get_yield(income):
    return income / initialAmount * 1 / investmentTerm * 100


if __name__ == "__main__":
    try:
        initialAmount = float(input("Введите начальную сумму, ₽ = "))
        rateAmount = float(input("Введите размер ставки, % = "))
        investmentTerm = int(input("Введите срок инвестирования, лет = "))
    except ValueError:
        print("Ошибка ввода. Будут использованы значения по умолчанию:")
        print("Начальная сумма = 100000 ₽")
        print("Размер ставки = 10%")
        print("Срок инвестирования = 5 лет")
        initialAmount, rateAmount, investmentTerm = 100000, 10, 5
    for i in range(90):
        print("_", end="")
    print()
    print("\t\t\t\t\tСхема начисления процентов")
    print("\t\t\t\t Ежемесячно Ежеквартально Раз в полгода Ежегодно")
    print("Начальная сумма, ₽:\t ", end="")
    for i in range(4):
        print(float(round(initialAmount, 1)), end=" \t")
    print()

    MONTHLY, QUARTERLY, HALF_YEARLY, YEARLY = 1, 3, 6, 12
    finalAmountMonthly = get_final_amount(MONTHLY)
    finalAmountQuarterly = get_final_amount(QUARTERLY)
    finalAmountHalfYearly = get_final_amount(HALF_YEARLY)
    finalAmountYearly = get_final_amount(YEARLY)
    print("Конечная сумма, ₽:\t ", round(finalAmountMonthly, 2), "\t",
          round(finalAmountQuarterly, 2), "\t",
          round(finalAmountHalfYearly, 2),
          "\t", round(finalAmountYearly, 2), sep="")
    incomeMonthly = finalAmountMonthly - initialAmount
    incomeQuarterly = finalAmountQuarterly - initialAmount
    income_half_yearly = finalAmountHalfYearly - initialAmount
    incomeYearly = finalAmountYearly - initialAmount
    print("Доход, руб: \t\t ", round(incomeMonthly, 2), "\t",
          round(incomeQuarterly, 2), "\t", round(income_half_yearly, 2), "\t",
          round(incomeYearly, 2), sep="")

    yieldMonthly, yieldQuarterly, yieldHalfYearly, yieldYearly = get_yield(
        incomeMonthly), get_yield(incomeQuarterly), get_yield(
        income_half_yearly), get_yield(incomeYearly)
    print("Доходность, % год.:\t ", round(yieldMonthly, 2), "\t\t",
          round(yieldQuarterly, 2), "\t\t", round(yieldHalfYearly, 2), "\t\t",
          round(yieldYearly, 2), sep="")
