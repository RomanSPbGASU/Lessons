class Set(set):
    def __init__(self, name, *elems):
        self.name = name
        set.__init__(self, elems)

    def print(self):
        """ Выводит элементы множества на экран """
        print(self.name, ": ", end = "")
        for elem in self:
            print(elem, end = " ")
        print()
    def sort(self):
        """ Сортирует элементы множества и помещает их в список """
        c = self.copy()
        c = list(c)
        c.sort()
        return c
    def find(self, elem):
        """ Ищет элемент во множестве """
        return elem in self
    def find_insect(self, elem, *sets):
        """ Проверяет принадлежит ли элемент ко всем множествам """
        insect = self.copy()
        for set in sets:
            insect = insect.intersection(set)
        return elem in insect
    def del_duplicate(self, set):
        """ Удаляет содержащиеся в set элементы из множества """
        insects = self.intersection(set)
        for insect in insects:
            set.discard(insect)

engineers = Set("Инженеры", "Иванов", "Петров", "Сидоров", "Zuse")
programmers = Set("Программисты", "Torvalds", "Knuth", "Stroustrup", "Zuse")

if __name__ == "__main__":
    print("Доступные операции над множествами:\n")
    print("1. Вывести списки на экран")
    print("2. Показать сортированные данные списков")
    print("3. Поиск записи в каждом списке")
    print("4. Добавление записи в списки")
    print("5. Удаление записи из списков")
    print("6. Поиск записи, в обоих списках")
    print("7. Удаление из второго списка записей, содержащихся в обоих списках")
    print("8. Нахождение записей, имеющихся только в одном списке")
    functions = { 
        1: lambda : (engineers.print(), programmers.print()),
        2: lambda : print("Отсортированные множества: \n", *engineers.sort(), "\n", *programmers.sort()),
        3: lambda x : (print("элемент %s найден в списке '%s'" % ("не" if not engineers.find(x) else "", engineers.name)), 
            print("элемент %s найден в списке '%s'" % ("не" if not programmers.find(x) else "", programmers.name))),
        4: lambda x : (engineers.add(x), programmers.add(x)),
        5: lambda x : (engineers.discard(x), programmers.discard(x)),
        6: lambda x : print("элемент %s найден в обоих списках" % ("не" if not engineers.find_insect(x, programmers) else "")),
        7: lambda : engineers.del_duplicate(programmers),
        8: lambda : print(*engineers.difference(programmers))
        }
    while 1:
        try:
            f_num = int(input("\nВыберите операцию над множествами: "))
        except:
            break
        if functions[f_num].__code__.co_argcount == 1:
            functions[f_num](input("Введите значение: "))
        else:
            functions[f_num]()

#выводить содержимое обоих списков на экран;
# сортировать данные обоих списков;
# осуществлять поиск нужных записей в каждом из списков;
# добавлять записи в оба списка;
# удалять записи из обоих списков;
# находить записи, которые содержатся в обоих списках;
# удалять из второго списка те записи, которые содержатся в обоих списках;
# находить записи в одном списке, которые отсутствуют в другом списке 