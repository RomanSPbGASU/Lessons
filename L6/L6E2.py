import random


class Counter:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __str__(self):
        return self.name + ": " + str(self.count)

    def __iadd__(self, other):
        self.count += int(other)
        return self

    def __int__(self):
        return int(self.count)


if __name__ == "__main__":
    try:
        sample = int(input("Введите размер выборки: "))
    except ValueError:
        print("Размер выборки введён неверно")
    else:
        positive = Counter("Положительные числа", 0)
        negative = Counter("Отрицательные числа", 0)
        for i in range(sample):
            rnd = random.randint(-1, 1)
            if rnd > 0:
                positive += 1
            if rnd < 0:
                negative += 1
        print(positive, negative, sep="\n")
