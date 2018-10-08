from re import compile, search


init = ["    Газпром     ", "   Роснефть!", "ЛУКойл#", "Сургутнефтегаз", "      Сбербанк ?  ", "транснефть", "$МосЭнерго@"]
print("Начальный список:")
for name in init:
    print(name)

ptrn = compile(r"\s*([а-яА-Я]+).*")
print("\nОчищенный список:")
form = [ptrn.search(name).group(1).capitalize() for name in init if ptrn.search(name) != None]
for name in form:
    print(name)