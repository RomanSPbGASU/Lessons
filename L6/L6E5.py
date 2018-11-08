class Queue(list):
    def __init__(self):
        super().__init__()
        self.pop_count = 0

    def push(self, obj):
        super().append(obj)
        print(len(self), ": ", obj)

    def pop(self, index=-1):
        self.pop_count += 1
        try:
            print(self.pop_count, ": ", super().pop(0))
        except IndexError:
            print("Ошибка. Очередь пуста")


if __name__ == "__main__":
    print("Помещяем в очередь...")
    queue = Queue()
    queue.push(11)
    queue.push(22)
    queue.push(33)
    print("Извлекаем из очереди...")
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()
