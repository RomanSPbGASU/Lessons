class LinkList:
    first = None
    last = None
    length = 0

    def __init__(self, *items):
        for item in items:
            self.append(item)

    def __str__(self):
        res = "/"
        for value in self:
            res += value + "/"
        # if len(res) == 1:
        #     res += "/"
        return res

    # TODO: написать итератор, чтобы использовать его в методе __getitem__
    # который использовать в методах pop и append

    def __next__(self):
        raise NotImplementedError("Необходимо переопределить метод")

    def __iter__(self):
        raise NotImplementedError("Необходимо переопределить метод")

    def __getitem__(self, index):
        if index < 0:
            offset = self.length + index
        else:
            offset = index
        current = self.first
        try:
            for i in range(offset):
                if current is None:
                    raise IndexError()
                current = current.next
        except IndexError as ie:
            print(ie)
        current.next = current.next.next
        return current.next

    def __len__(self):
        return self.length

    def append(self, data):
        if self.first is None:
            self.first = Node(data)
            self.last = self.first
            self.length += 1
            return
        self.last.next = Node(data)
        self.length += 1

    def pop(self, index=-1):
        prev = self[index - 1]
        prev.next = self[index].next


class Node:
    def __init__(self, data=None, next_node=None):
        self.value = data
        self.next = next_node


if __name__ == "__main__":
    print("Помещяем в список...")
    link_list = LinkList()
    for i in range(1, 4):
        link_list.append(i * 11)
        print(i, ": ", link_list[-1])
    print("Извлекаем из списка...")
    for i in range(1, 5):
        print(i + 1, ": ", link_list.pop())
