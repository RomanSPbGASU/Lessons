try:
    initialAmount = float(input("Введите начальную сумму, ₽ = "))
    rateAmount = float(input("Введите размер ставки, % = "))
    investmentTerm = int(input("Введите срок инвестирования, лет = "))
except:
    print("Ошибка ввода")
    print("Начальная сумма = 100000 ₽")
    print("Размер ставки = 10%")
    print("Срок инвестирования = 5 лет")
    initialAmount, rateAmount, investmentTerm = 100000, 10, 5
finalAmountSimple = initialAmount * (1 + rateAmount / 100 * investmentTerm)
finalAmountComplicated = initialAmount * (1 + rateAmount / 100) ** investmentTerm
print("\t\t\t Простой процент Сложный процент")
print("Начальная сумма, ₽:\t", round(initialAmount, 1), "\t", initialAmount)
print("Конечная сумма, ₽:\t", round(finalAmountSimple, 1), "\t", round(finalAmountComplicated, 1))
incomeSimple = finalAmountSimple - initialAmount
incomeComplicated = finalAmountComplicated - initialAmount
print("Доход, руб:\t\t", round(incomeSimple, 1), "\t", round(incomeComplicated, 1))
def getYield(income, initial_amount, term):
    return income/initial_amount*1/term*100
yieldSimple = getYield(incomeSimple, initialAmount, investmentTerm)
yieldComplicated = getYield(incomeComplicated, initialAmount, investmentTerm)
print("Доходность, % год.:\t", round(yieldSimple, 1), "\t\t", round(yieldComplicated, 1))

