import os

if __name__ == "__main__":
    os.chdir("bank_contacts\\")
    banks_info = "banks_info.txt"
    open(banks_info, "w").close()
    file_names = os.listdir()
    file_names.remove(banks_info)
    data = []
    for file_name in file_names:
        with open(file_name, encoding="utf8") as file:
            data.append(file.readlines())
        print("Информация из файла", file_name, "считана")

    print("\nСправочная информация по банкам:\n")

    for bank in data:
        with open(banks_info, "a") as file:
            file.writelines(bank)
            file.write("\n")
        for line in bank:
            print(line, end="")
        print()
