import os
import re

if __name__ == "__main__":
    os.chdir("bank_contacts\\")
    banks_info = "banks_info.txt"
    open(banks_info, "w").close()
    file_names = os.listdir(".")
    file_names.remove(banks_info)
    data = []
    regexp = re.compile(
        r"Сокращенное фирменное наименование кредитной организации\n"
        "(?P<name>[^0-9]+)$/*^Почтовый адрес\n(?P<address>\d{6}[.,;\s][\s\t]?"
        "[А-Я]?[а-я]+[.,;\s][\s\t]?(ул[.]?|улица)[\s\t]?[А-Яа-я0-9_\-]"
        "[.,;\s][\s\t]?(д[.]?|дом)[\s\t]\d+[.,;\s]((кор[.]|к[.]|стр[.])"
        "[\s\t]\d+)?).*Телефон[:\s\t](?P<phone>[0-9+][0-9\-()]*[0-9])", re.S)
    for file_name in file_names:
        with open(file_name, encoding="1251") as file:
            match = regexp.search(file.read())
            print(match.group("name", "address", "phone"))





        print("Информация из файла", file_name, "считана")

    print("\nСправочная информация по банкам:\n")

    for bank in data:
        with open(banks_info, "a") as file:
            file.writelines(bank)
            file.write("\n")
        for line in bank:
            print(line, end="")
        print()
