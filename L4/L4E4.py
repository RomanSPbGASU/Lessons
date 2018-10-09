class Set(set):
    def __init__(self, name, *elems):
        self.name = name
        set.__init__(self, elems)

    def print(self):
        """ Выводит элементы множества на экран """
        print(self.name, ": ", end = "")
        for elem in self:
            print(elem, end = " ")
    def sort(self):
        """ Сортирует элементы множества и помещает их в список """
        return [self].sort()
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
        insects = self.insection(set)
        for insect in insects:
            self.disgard(insect)

engineers = Set("Инженеры", "Иванов", "Петров", "Сидоров", "Zuse")
programmers = Set("Программисты", "Torvalds", "Knuth", "Stroustrup", "Zuse")

if __name__ == "__main__":
    print("Доступные операции над множествами:\n")
    print("1. Вывести списки на экран")
    print("2. Сортировать данные списков")
    print("3. Поиск записи в каждом списке")
    print("4. Добавление записи в списки")
    print("5. Удаление записи из списков")
    print("6. Поиск записи, в обоих списках")
    print("7. Удаление из второго списка записей, содержащихся в обоих списках")
    print("8. Нахождение записей, имеющихся только в одном списке")
    functions = { 
        1: (engineers.print(), programmers.print),
        2: print("Отсортированные множества\n", *[engineers.sort()], *[programmers.sort()]),
        3: (print("элемент %s найден в списке '%s'" % ("не" if not engineers.find(input("Введите искомое значение: ")) else "", engineers.name)), 
            print("элемент %s найден в списке '%s'" % ("не" if not programmers.find(input("Введите искомое значение: ")) else "", programmers.name))),
        4: (lambda x = input("Введите значение для добавления: "): (engineers.add(x), programmers.add(x)))(),
        5: (lambda x = input("Введите значение для удаления: "): (engineers.discard(x), programmers.discard(x)))(),
        6: engineers.find_insect(input("Введите значение для поиска: "), programmers),
        7: engineers.del_duplicate(programmers),
        8: engineers.difference(programmers)
        }
    while 1:
        functions[int(input("\nВыберите операцию над множествами: "))]

#выводить содержимое обоих списков на экран;
# сортировать данные обоих списков;
# осуществлять поиск нужных записей в каждом из списков;
# добавлять записи в оба списка;
# удалять записи из обоих списков;
# находить записи, которые содержатся в обоих списках;
# удалять из второго списка те записи, которые содержатся в обоих списках;
# находить записи в одном списке, которые отсутствуют в другом списке 