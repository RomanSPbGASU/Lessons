import random


class guess_the_word():
    """Класс консольной игры по типу "Поля чудес" """

    def __init__(self, word = "example", dif_level = 5):
        print("{:^80}".format("Игра: Угадайте слово"))
        try:
            file = open('word_rus.txt', 'r')
        except Exception as ex:
            print("Ошибка: %s" % ex.args[0])
            raise SystemExit
        rus_list = []
        for word in file:
            rus_list.append(word)
        self.dif_level = 5
        self.cage = ""
        self.letters = ""
        self.mistakes = 0

    def put_dif_level(self):
        """Метод выводит диалог выбора уровня сложности (от 0 до 10). """
        try:
            dif_level = int(input("Выберите уровень сложности (0-10): "))
            if dif_level < 0 or dif_level > 10:
                raise Exception("Уровень сложности должен быть в диапазоне от 0 до 10. ")
        except Exception as ex:
            print(ex.args[0], "Значение по умолчанию: 5")
        except ValueError:
            raise Exception("Ошибка. Необходимо ввести число. ")
        mis_max = (33 - len({word})) * (10 - dif_level) / 10

    def choose_word(self, word):
        if not word:
            raise Exception("Слово для игры не выбрано")
        else:
            cage = ""
            for letter in word:
                cage += "*"

    def choose_rnd_word(self):
        """Метод выбирает случайное слово из словаря."""
        word = random.choice(rus_list)
        choose_word(word)

    def show_cage(self):
        print("{:^80}".format(cage))

    def update_cage(letter):
        for i, lt in enumerate(word):
            if lt == letters[-1]:
                cage = cage[0:i] + lt + cage[i:-1]

    def put_letter(self):
        """Метод выводит диалог о вводе предполагаемой буквы. """
        letters += str(input("Введите букву: ").lower())
        if letters[-1] in word:
            update_cage(letters[-1])
        else:
            mistakes += 1
            print("Буквы '%s' в этом слове нет. Количество ошибок: %d / %d" % (letter, mistakes, mis_max))

    def again(self):
        return input("Сыграем ещё раз? (д/н): ").lower() != "н"

    def play_game(self):
        while 1:
            print("Угадайте слово")
            choose_rnd_word()
            show_cage()
            put_dif_level()
            while mistakes <= mis_max:
                put_letter()
                show_cage()
                if word == cage:
                    print("Вы выиграли!")
                    break
            else:
                print("Вы проиграли")
            if not again():
                break


if __name__ == "__main__":
    game = guess_the_word()
    game.play_game()