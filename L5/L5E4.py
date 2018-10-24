def fibonacci(upper: int):
    i = 1
    yield 1
    j = 0
    while i + j < upper:
        yield i + j
        j, i = i, i + j


if __name__ == "__main__":
    try:
        upper_limit = int(input("Введите верхнюю границу: "))
    except ValueError:
        print("Введённое значение не является числом")
        upper_limit = 1
    print("Числа Фибоначчи в диапазоне от %s до %s" % (1, upper_limit))
    for num in fibonacci(upper_limit):
        print(num, end=" ")


