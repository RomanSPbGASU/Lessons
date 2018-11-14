while 1:
    try:
        x = int(input("Введите число X: "))
        y = int(input("Введите число Y: "))
    except:
        "Ошибка"
    print("До обмена:\tx = %d\ty = %d" % (x, y))
    x ^= y
    y ^= x
    x ^= y
    print("После обмена:\tx = %d\ty = %d" % (x, y))
    if input("Попробуем снова? (д/н)") == "н":
        break
