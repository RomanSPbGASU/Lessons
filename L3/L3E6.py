from re import compile, search
#ptrn = compile(r".*[\./]((?:0[1-9]){2}|(?:1[0-2]){2})[\./]\d{4}$")
#ptrn = compile(r"[\./](?:0[1-9]|1[0-2])[\./](?!0{4})\d{4}$")
# TODO: написать тесты для регулярных выражений
ptrn = compile(r"^(3[01](?=0[13578]|1[02])|")
while 1:
    date = input("Введите дату в одном из двух форматов: 10.09.1995 или 10/09/1995: ")
    print("Дата введена %sправильно" % ("" if ptrn.search(date) else "не"))

