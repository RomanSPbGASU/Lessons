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
    print("_", end = "")
print()
print("\t\t\t\t\tСхема начисления процентов")
print("\t\t\t Ежемесячно\tЕжеквартально\tРаз в полгода\tЕжегодно")
print("Начальная сумма, ₽:\t " , end = "")
for i in range(4):
    print(float(round(initialAmount, 1)), end = "\t")
print()
def getFinalAmount(monthInPeriod):
    return initialAmount * (1 + rateAmount / 100 * monthInPeriod / 12) ** (investmentTerm * 12 / monthInPeriod)
MONTHLY, QUARTERLY, HALFYEARLY, YEARLY = 1, 3, 6, 12
finalAmountMonthly = getFinalAmount(MONTHLY)
finalAmountQuarterly = getFinalAmount(QUARTERLY)
finalAmountHalfyearly = getFinalAmount(HALFYEARLY)
finalAmountYearly = getFinalAmount(YEARLY)
print("Конечная сумма, ₽:\t ", round(finalAmountMonthly, 2), "\t", round(finalAmountQuarterly, 2), "\t", round(finalAmountHalfyearly, 2), "\t", round(finalAmountYearly, 2), sep = "")
incomeMonthly, incomeQuarterly, incomeHalfyearly, incomeYearly = finalAmountMonthly - initialAmount, finalAmountQuarterly - initialAmount, finalAmountHalfyearly - initialAmount, finalAmountYearly - initialAmount
print("Доход, руб:\t\t ", round(incomeMonthly, 2), "\t", round(incomeQuarterly, 2), "\t", round(incomeHalfyearly, 2), "\t", round(incomeYearly, 2), sep = "")
def getYield(income):
    return income / initialAmount * 1 / investmentTerm * 100
yieldMonthly, yieldQuarterly, yieldHalfyearly, yieldYearly = getYield(incomeMonthly), getYield(incomeQuarterly), getYield(incomeHalfyearly), getYield(incomeYearly)
print("Доходность, % год.:\t ", round(yieldMonthly, 2), "\t\t", round(yieldQuarterly, 2), "\t\t", round(yieldHalfyearly, 2), "\t\t", round(yieldYearly, 2), sep = "")
