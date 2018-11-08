class LinkList:
    first = None
    last = None
    length = 0

    def __init__(self, *items):
        self.first = Node()
        self.last = self.first
        # self.length = 0
        for item in items:
            self.push(item)

    def push(self, data):
        self.last.next = Node(data)
        self.length += 1
        return data

    def pop(self, index=-1):
        if index < 0:
            offset = self.length + index
        else:
            offset = index
        current = self.first
        try:
            for i in range(offset - 1):
                current = current.next
                if current is None:
                    raise IndexError()
        except IndexError as ie:
            print(ie)
        current.next = current.next.next
        return current.next


class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None


if __name__ == "__main__":
    print("Помещяем в список...")
    link_list = LinkList()
    for i in range(1, 4):
        print(i, ": ", link_list.push(i * 11))
    print("Извлекаем из списка...")
    for i in range(4):
        print(i + 1, ": ", link_list.pop())
