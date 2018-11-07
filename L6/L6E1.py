from L6.Dist import Dist


def format_print(name, res, lead):
    for_print = "{:<20} {:<15} {:<15}".format(name, res, lead)
    print(for_print)


def get_max_leading(*rises):
    max_leading = rises[0]
    for leading in rises:
        if leading > max_leading:
            max_leading = leading
    return max_leading


if __name__ == "__main__":
    print("{:^80}".format("Метание молота"))

    first = Dist(86, 74)
    second = Dist(84, 14)
    third = Dist(80, 46)

    format_print("Имя", "Результат", "Улучшение")
    format_print("Юрий Седых", first, first - second)
    format_print("Сергей Литвинов", second, second - third)
    format_print("Юрий Тамм", third, third - Dist(80, 32))
    print("_" * 80)
    format_print("Среднее: ", (first + second + third) / 3, "")
    format_print("Среднее улучшение: ", "", (first - Dist(80, 32)) / 3)
    ml = get_max_leading(first - second, second - third, third - Dist(80, 32))
    format_print("Макс. улучшение: ", "", ml)
