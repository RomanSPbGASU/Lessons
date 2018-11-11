import csv

dialect = csv.excel
dialect.delimiter = ";"
dialect.quotechar = "'"


def csv_write(file_name, data):
    with open(file_name, "w") as file:
        csv_writer = csv.writer(file, dialect)
        csv_writer.writerows(data)


if __name__ == "__main__":
    names = "NAMES.txt"
    names_sort_numb = "NAMES_sort_numb.txt"
    names_sort_name = "NAMES_sort_name.txt"

    with open(names) as file:
        csv_reader = csv.reader(file, dialect)
        data = list(csv_reader)
    print("Файл", names, "считан")

    for line in data:
        line[0] = int(float(line[0]))
    print("Данные преобразованы")

    data.sort()
    print("Данные отсортированы по номеру банка")

    csv_write(names_sort_numb, data)
    print("Данные записаны в файл", names_sort_numb)

    for line in data:
        line[0], line[1] = line[1], line[0]
    print("Данные переставлены местами")

    data.sort()
    print("Данные отсортированы по наименованию банка")

    csv_write(names_sort_name, data)
    print("Данные записаны в файл", names_sort_name)
