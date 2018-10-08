from re import compile, search


# проверка e-mail (упрощённая)
ptrn = compile(r"(?P<box>[a-z0-9]+[a-z0-9_.-]*[a-z0-9])@(?P<host>[a-z]+-?[a-z]*\.[a-z]+)")
string = input("Введите адрес электронной почты: ")
email = ptrn.search(string)
print("e-mail '%s' соответствует шаблону" % email.group())
print("логин: %s домен: %s" % (email.group("box"), email.group("host")))