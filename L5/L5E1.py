from re import compile


def delete_spaces(strings: list):
    for i, string in enumerate(strings):
        string = list(string)
        for space in range(string.count(" ")):
            string.remove(" ")
        strings[i] = "".join(string)


def delete_punctuation(strings: list):
    ptrn = compile(r"[а-яА-Я]+")
    for i, string in enumerate(strings):
        res = ""
        res += ptrn.search(string).group(0)
        strings[i] = res


def capitalize(strings: list):
    for i, string in enumerate(strings):
        strings[i] = string.capitalize()


def print_strings(strings: list):
    for string in strings:
        print(string)


if __name__ == "__main__":
    titles = ["    Газпром     ", "   Роснефть!", "ЛУКойл#", "Сургутнефтегаз",
              "      Сбербанк ?  ", "транснефть", "$МосЭнерго@"]
    print("Начальный список:")
    print_strings(titles)
    delete_spaces(titles)
    delete_punctuation(titles)
    capitalize(titles)
    print("\nОчищенный список:")
    print_strings(titles)
