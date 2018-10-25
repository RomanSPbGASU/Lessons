def get_exchange(money: int):
    if money < 1:
        raise ValueError
    coins = [1, 2, 5]
    i = 1
    j = -1
    while 1:
        exchange = []
        while sum(exchange) != money:
            exchange.append(coins[i + j])
        i += 1
        yield exchange


if __name__ == "__main__":
    print("Возможные варианты размена монеты 10 руб.")
    for ex in get_exchange(10):
        print(ex)
