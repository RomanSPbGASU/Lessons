while 1:
    try:
        monthNum = int(input("Введите номер месяца: "))
        break
    except ValueError:
        print("Ошибка. Введите число")
while 1:
    try:
        firstWeekday = int(input("Введите номер первого дня месяца: "))
        break
    except ValueError:
        print("Ошибка. Введите число")
