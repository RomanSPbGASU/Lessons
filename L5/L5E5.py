def get_exchange(money: int):
    for i in range(0, money + 1, 1):
        for j in range(i, money + 1, 2):
            for k in range(j, money + 1, 5):
                if k == money:
                    yield [1] * i + [2] * ((j - i) // 2) + [5] * (
                                (k - j) // 5)


if __name__ == "__main__":
    print("Возможные варианты размена монеты 10 руб.")
    for ex in get_exchange(10):
        print(ex)
