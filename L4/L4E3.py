import random


class GuessTheWord(object):
    """Класс консольной игры по типу "Поля чудес" """

    try:
        file = open('word_rus.txt', 'r')
    except Exception as ex:
        print("Ошибка: %s" % ex.args[0])
        raise SystemExit
    rus_list = []
    for word in file:
        rus_list.append(word)


    def __init__(self, word = "example", dif_level = 5):
        print("{:^80}".format("Игра: Угадайте слово\n"))
        self.dif_level = 5
        self.cage = ""
        self.letters = ""
        self.mistakes = 0

    class DifLevelEx(Exception):
        def __init__(self, *args):
            self.args = args

    class LettersEx(Exception):
        def __init__(self, *args):
            self.args = args

    class DifLevelValueError(DifLevelEx, ValueError):
        pass

    def put_dif_level(self):
        """Метод выводит диалог выбора уровня сложности (от 0 до 10). """
        try:
            dif_level = int(input("Выберите уровень сложности (0-10): "))
            if dif_level < 0 or dif_level > 10:
                raise self.DifLevelEx("Уровень сложности должен быть в диапазоне от 0 до 10. ")
            else:
                self.dif_level = dif_level
        except (ValueError, self.DifLevelEx) as ex:
            print(ex.args[0] if type(ex) != ValueError else "Ошибка. Необходимо ввести число. ", 
                  "Значение по умолчанию: 5")
        self.mistakes = 0
        self.mis_max = int((32 - len(set(self.word))) * (10 - self.dif_level) / 10)

    def choose_word(self, word):
        try:
            if not word:
                raise Exception("Слово для игры не выбрано")
        except Exception as ex:
            print(ex)
        else:
            self.word = word
            self.cage = ""
            for letter in word:
                self.cage += "*"

    def choose_rnd_word(self):
        """Метод выбирает случайное слово из словаря."""
        word = random.choice(self.rus_list)[:-1]
        self.choose_word(word)

    def show_cage(self):
        print("{:^80}".format(self.cage))

    def update_cage(self, letter):
        for i, lt in enumerate(self.word):
            if lt == letter:
                self.cage = self.cage[:i] + lt + self.cage[i+1:]

    def put_letter(self):
        """Метод выводит диалог о вводе предполагаемой буквы. """
        try:
            ltr = str(input("Введите букву: ").lower())
            if ltr == "ё": ltr = "e"
            if ltr in self.letters:
                raise self.LettersEx("Эту букву вы уже выбирали")
            self.letters += ltr
            if ltr in self.word:
                self.update_cage(ltr)
            else:
                if ord(ltr) not in range(0x430, 0x44F):
                    raise self.LettersEx("Необходимо использовать только русские буквы.")
                self.mistakes += 1
                raise self.LettersEx("Буквы '%s' в этом слове нет. Количество ошибок: %d / %d" % (ltr, self.mistakes, self.mis_max))
        except self.LettersEx as le:
            print(le.args[0], "\nИспользованные буквы: ", *list(sorted(self.letters)))
        except Exception as ex:
            print(ex)

    def again(self):
        return input("Сыграем ещё раз? (д/н): ").lower() != "н"

    def play_game(self):
        while 1:
            self.choose_rnd_word()
            self.show_cage()
            self.put_dif_level()
            while self.mistakes <= self.mis_max:
                self.put_letter()
                self.show_cage()
                if self.word == self.cage:
                    print("Вы выиграли!")
                    break
            else:
                print("Вы проиграли")
                print("Загаданное слово: %s" % self.word)
            if not self.again():
                break


if __name__ == "__main__":
    game = GuessTheWord()
    game.play_game()