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

def find_tel(name):
    """ Предоставляет номер телефона сотрудника """
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

func = {
    1: find_tel,
    2: get_info,
    3: get_unit_tels,
    4: get_pos_info
    }

while 1:
    try: 
        f_num = int(input("Выберите необходимое действие: "))
        if func < 1 or func > 4:
            raise ValueError
    except ValueError as ve:
        print("Выбрано недопустимое действие")
        print("Необходимо ввести число от 1 до 4")
        continue
    print(*func[f_num]())