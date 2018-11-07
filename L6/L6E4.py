class Stack(list):
    def __init__(self):
        super().__init__()
        self.pop_count = 0

    def append(self, obj):
        super().append(obj)
        print(len(self), ": ", obj)

    def pop(self, index=-1):
        self.pop_count += 1
        try:
            print(self.pop_count, ": ", super().pop(index))
        except IndexError:
            print("Ошибка. Стек пуст")


if __name__ == "__main__":
    print("Помещяем в стек...")
    stack = Stack()
    stack.append(11)
    stack.append(22)
    stack.append(33)
    print("Извлекаем из стека...")
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
