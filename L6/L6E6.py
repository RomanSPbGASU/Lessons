class LinkList:
    first = last = None
    length = 0

    def __init__(self, *items):
        for item in items:
            self.append(item)

    def __str__(self):
        res = "/ "
        for value in self:
            res += str(value) + " / "
        return res

    def __next__(self):
        raise NotImplementedError("Необходимо переопределить метод")

    def __iter__(self):
        current = self.first
        for i in range(self.length):
            yield current.value
            current = current.next

    def __get_node(self, index):
        if index < 0:
            offset = self.length + index
        else:
            offset = index
        if not 0 <= offset <= self.length:
            raise IndexError()
        current = self.first
        for i in range(offset):
            current = current.next
        return current

    def __getitem__(self, index):
        if isinstance(index, slice):
            raise NotImplementedError()
        else:
            return self.__get_node(index).value

    def __setitem__(self, key, value):
        ...

    def __delitem__(self):
        ...

    def __len__(self):
        return self.length

    def append(self, data):
        if self.first:
            self.last.next = Node(data)
            self.last = self.last.next
        else:
            self.last = self.first = Node(data)
        self.length += 1

    def pop(self, index=-1):
        if self.length == 0:
            raise IndexError("Ошибка. Список пуст")
        else:
            res = self[index]
            if self.length == 1:
                self.first = self.last = None
            else:
                if index == -1:
                    self.last = self.__get_node(index - 1)
                    self.last.next = None
                else:
                    try:
                        prev = self.__get_node(index - 1)
                    except IndexError:
                        self.first = self.first.next
                    else:
                        prev.next = self.__get_node(index).next

            self.length -= 1
            return res


class Node:
    def __init__(self, data=None, next_node=None):
        self.value = data
        self.next = next_node

    def __repr__(self):
        return " /" + str(self.value) + "/ -->" + str(self.next)


if __name__ == "__main__":
    print("Помещяем в список...")
    link_list = LinkList()
    for i in range(1, 4):
        link_list.append(i * 11)
        print(i, ": ", link_list[-1])
    print("Извлекаем из списка...")
    for i in range(1, 5):
        try:
            print(i, ": ", link_list.pop())
        except IndexError as ie:
            print(ie)
