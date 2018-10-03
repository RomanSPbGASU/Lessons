from re import compile, search
ptrn = re.compile(r".*[\./]\d{4}$")
while 1:
    date = input("Введите дату в одном из двух форматов: 10.09.1995 или 10/09/1995")
    print("Дата введена %sправильно" % "" if ptrn.search(date) else "не")