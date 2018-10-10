from re import *


positions = ("инженер", "начальник отдела", "менеджер", "программист")
units = ("отдел автоматизации", "отдел маркетинга")
employees = {"Иванов И. И.":(positions[0], units[1], 123), "Петров П. П.":(positions[2], units[0], 987), "Кузнецов К. К":(positions[3], units[0], 456), "Семёнов А. А":(positions[1], units[0], 789), "Волков А. Е":(positions[3], units[1], 321), "Путин В. В":(positions[1], units[1], 654)}

def find_tel(name):
    """ Предоставляет номер телефона сотрудника """
    for employee, data in employees.items():
        if find_like(name, employee):
            return "Телефон: " + str(data[2])

def get_info(name):
    """ Предоставляет информацию о сотруднике """
    for employee, data in employees.items():
        if find_like(name, employee):
            return ["Должность: " + str(data[0]), "Подразделение: " + str(data[1]), "Телефон: " + str(data[2])]

def get_unit_tels(unit_name):
    """ Предоставляет номера сотрудников конкретного отдела """
    book = {}
    for employee, data in employees.items():
        if find_like(unit_name, data[1]):
            book.update({"Сотрудник: " + str(employee): "Телефон: " + str(data[2])})
    return book

def get_pos_info(position_name):
    """ Предоставляет информацию о сотрудниках, занимающих определённую должность """
    book = []
    for employee, data in employees.items():
        if find_like(position_name, data[0]):
            book.append(["Сотрудник: " + str(employee), "Подразделение: " + str(data[1]), "Телефон: " + str(data[2])])
    return book

def find_like(exp, string):
    """ Ищет выражение в строке """
    ptrn = compile(".*" + str(exp) + ".*", IGNORECASE)
    return ptrn.search(string)

if __name__ == "__main__":

    print("{:^80}".format("Поиск по базе сотрудников"))
    print()
    print("1. Найти номер телефона сотрудника")
    print("2. Получить информацию о сотруднике")
    print("3. Получить номера сотрудников конкретного отдела")
    print("4. Получить информацию о сотрудниках на конкретной должности")
    print()

    func = {
        1: (find_tel, "Введите имя сотрудника: "),
        2: (get_info, "Введите имя сотрудника: "),
        3: (get_unit_tels, "Введите название подразделения: "),
        4: (get_pos_info, "Введите название должности: ")
        }

    while 1:
        try: 
            f_num = int(input("Выберите необходимое действие: "))
            if f_num < 1 or f_num > 4:
                raise ValueError
        except ValueError as ve:
            print("Выбрано недопустимое действие")
            print("Необходимо ввести число от 1 до 4")
            continue
        f, text = func[f_num]
        ans = f(input(text))
        if ans:
            if type(ans) != str:
                for item in ans:
                    if type(item) != str:
                        for elem in item:
                            print(elem)
                    else:
                       print(item)
            else:
                print(ans)
        else:
            print("Ничего не найдено")