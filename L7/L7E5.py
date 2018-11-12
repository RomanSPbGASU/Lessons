import os
import sys
import psutil
import shutil
import math


def get_procedure_number():
    def print_frames(content):
        print("‖{:<50}‖".format(content))

    print_frames("˭" * 50)
    print_frames("  Возможные процедуры:")
    print_frames(" 1 - вывести список файлов в текущей директории")
    print_frames(" 2 - вывести информацию о системе")
    print_frames(" 3 - вывести список процессов")
    print_frames(" 4 - продублировать все фйлы в директории")
    print_frames(" 5 - продубировать указанный файл")
    print_frames(" 6 - удалить все дубликаты файлов")
    print_frames("‗" * 50)
    return int(input("Выберите нужную процедуру: "))


def print_header(header):
    print("{:^80}".format(header))


def print_by_columns(collection):
    column_count = 80 // (max(len(name) for name in collection) + 2)
    column_width = 80 // column_count
    row_count = math.ceil(len(collection) / column_count)
    rows = [collection[i::row_count] for i in range(row_count)]
    for row in rows:
        for name in row:
            print("{:{}}".format(name, column_width), end="")
        print()


def show_file_names(*path):
    print_header("Файлы в текущей директории: ")
    file_names = os.listdir(*path)
    file_names = [name for name in file_names if os.path.isfile(name)]
    print_by_columns(file_names)


def show_system_info():
    def print_formatted(*content):
        print("{:<30}{}".format(*content))

    print_header("Информация о системе: ")
    print_formatted("Количество процессоров: ",
                    psutil.cpu_count())
    print_formatted("Платформа: ",
                    sys.platform)
    print_formatted("Кодировка файловой системы: ",
                    sys.getfilesystemencoding())
    print_formatted("Текущая директория: ",
                    os.getcwd())
    print_formatted("Текущий пользователь: ",
                    os.getlogin())


def show_process_list():
    print_header("Список запущенных процессов:")
    process_iter = psutil.process_iter(attrs=["name"])
    processes = []
    for p in process_iter:
        name = p.info["name"]
        try:
            processes.index(name)
        except ValueError:
            processes.append(name)
    print_by_columns(processes)


def duplicate_files():
    path = input("Директория: ")
    if path:
        print_header("=Дублирование файлов в директории " + path)
    else:
        print_header("=Дублирование файлов в текущей директории=")
    files = os.listdir(*path)
    for file in files:
        if os.path.isfile(file):
            file_root = os.path.splitext(file)[0]
            file_ext = os.path.splitext(file)[1]
            new_file = path + file_root + "_copy" + file_ext
            shutil.copy2(file, new_file)
            print("Файл", new_file, "был успешно создан")
        else:
            files.remove(file)


def duplicate_file():
    file = input("Файл: ")
    print_header("=Дублирование указанного файла=")
    if os.path.isfile(file):
        file_root = os.path.splitext(file)[0]
        file_ext = os.path.splitext(file)[1]
        new_file = file_root + "_copy" + file_ext
        shutil.copy2(file, new_file)
        print("Файл", new_file, "был успешно создан")


def del_duplicates():
    path = input("Директория: ")
    if path:
        print_header("=Удаление дубликатов в директории " + path)
    else:
        print_header("=Удаление дубликатов в текущей директории=")
    file_names = os.listdir(*path)
    deleted = 0
    for file_name in file_names:
        if not os.path.isfile(file_name):
            file_names.remove(file_name)
    for file_name in file_names:
        with open(file_name, "rb") as file:
            current = file.read()
        file_names.remove(file_name)
        for f_n in file_names:
            with open(f_n, "rb") as file:
                another = file.read()
            if current == another:
                os.remove(path + f_n)
                file_names.remove(f_n)
                deleted += 1
                print("Файл", f_n, "был успешно удален")

    str_deleted = "Удалено файлов: " + str(deleted)
    print("_" * len(str_deleted))
    print(str_deleted)


if __name__ == "__main__":
    ans = None
    procedures = [
        show_file_names,
        show_system_info,
        show_process_list,
        duplicate_files,
        duplicate_file,
        del_duplicates]
    while ans != "N":
        procedures[get_procedure_number() - 1]()
        ans = input("\nПродолжаем работу? (Y/N): ")
    print("До свидания!")
