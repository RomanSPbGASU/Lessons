import random


class guess_the_word():
    """ Консольная игра по типу "Поля чудес" """


    def __init__:
        print("{:^80}".format("Игра: Угадайте слово"))
        try:
            file = open('word_rus.txt', 'r')
        except Exception as ex:
            print("Ошибка: %s" % ex.args[0])
            raise SystemExit
        self.dif_level = 5

    def put_dif_level(self):
    """ Диалог выбора уровня сложности (от 0 до 10) """
        try:
            dif_level = int(input("Выберите уровень сложности (0-10): "))
            if dif_level < 0 or dif_level > 10:
                raise Exception("Уровень сложности должен быть в диапазоне от 0 до 10. ")
        except Exception as ex:
            print(ex.args[0], "Значение по умолчанию: 5")
        except ValueError:
            raise Exception("Ошибка. Необходимо ввести число. ")
        mis_max = (33 - len({word})) * (10 - dif_level) / 10



    def show_cage(self):

    def put_letter(self):

        rus_list = []
        for word in file:
            rus_list.append(word)
        word = random.choice(rus_list)
        ans = ""
        for letter in word:
            ans += "*"
        letters = ""
        mistakes = 0
        #while mistakes < len(word) / 33 * 20
        mis_max = (33 - len({word}))*(10 - dif_level)/10
        while mistakes < mis_max:
            print(ans)
            letters += str(input("Введите букву: ").lower())
            if letters[-1] in word:
                for i, lt in enumerate(word):
                    if lt == letters[-1]:
                        ans = ans[0:i] + lt + ans[i:-1]
                print(ans)
            else:
                mistakes += 1
                print("Буквы '%s' в этом слове нет. Количество ошибок: %d" % (letter, mistakes))
        again = input("Сыграем ещё раз? (д/н): ").lower() != "н"
        if not again:
            break