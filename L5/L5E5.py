def get_exchange(money: int):
    if money < 1:
        yield None
    base_exchange = [1] * money
    yield base_exchange
    coins_equal = {2: [(1, 1)],
                   5: [(2, 2, 1), (1, 1, 1, 1, 1)]}
    coins = tuple(coins_equal)
    for coin in coins:
        exchange = base_exchange.copy()
        while 1:
            for coin_equal in coins_equal[coin]:
                included = True
                for c in coin_equal:
                    included = included and c in exchange
                if included:
                    for c in coin_equal:
                        exchange.remove(c)
                    exchange.append(coin)
                else:
                    break
            exchange.sort(reverse=True)
            yield exchange


if __name__ == "__main__":
    print("Возможные варианты размена монеты 10 руб.")
    for ex in get_exchange(10):
        print(ex)
