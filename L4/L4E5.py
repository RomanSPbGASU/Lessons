from re import compile, search
def find_tel(name):
    """ Предоставляет номер телефона сотрудника """
    for employee, data in employees.items:
        if find_like(name):
            return data[2]
    pass
def get_info(name):
    """ Предоставляет информацию о сотруднике """
    pass
def get_unit_tels(unit_name):
    """ Предоставляет номера сотрудников конкретного отдела """
    pass
def get_pos_info(position_name):
    """ Предоставляет информацию о сотрудниках, занимающих определённую должность """
    pass
def find_like(exp, string):
    """ Ищет выражение в строке """
    ptrn = ".*" + str(exp) + ".*"
    return ptrn.search(string)

if __name__ == "__main__":
    positions = ("инженер", "начальник отдела", "менеджер", "программист")
    units = ("отдел автоматизации", "отдел маркетинга")
    employees = {"Иванов И. И.":(positions[0], units[1], 123), "Петров П. П.":(positions[2], units[0], 987), "Кузнецов К. К":(positions[3], units[0], 456), "Семёнов А. А":(positions[1], units[0], 789), "Волков А. Е":(positions[3], units[1], 321), "Путин В. В":(positions[1], units[1], 654)}

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
        f, text in func[f_num]
        print(f(input(text))
        #f(input(text) for f, text in func[f_num]

        # TODO: Изменить настройки, чтобы при нажатии F5 запускался активный файл