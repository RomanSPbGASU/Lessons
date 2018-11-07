class Stack(list):
    def append(self, obj):
        super().append(obj)
        print(len(self), ": ", obj)

    def pop(self, index=-1):
        try:
            print(len(self), ": ", super().pop(index))
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
