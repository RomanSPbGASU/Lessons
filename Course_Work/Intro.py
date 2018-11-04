from PIL import Image, ImageDraw, BmpImagePlugin as BIP
import tkinter as tk
import tkinter.filedialog as fd


# TODO: разработать класс для проверки эффективности работы нейросети, создающий растровое изображение из случайного фрагмента текстового файла и проверки количества ошибок после распознавания текста нейросетью.
class Neuron:
    def __init__(self, name, in_arr=tuple([0] * 1024)):
        if len(in_arr) != 1024:
            raise ValueError("входной массив должен содержать 30x30 элементов")
        self.__name = str(name)
        self.__in_arr = in_arr
        self.__memory = []

    def __repr__(self):
        return str(self.__name)

    def __str__(self):
        return str("Нейрон: " + self.__name)

    def save(self, directory=""):
        with open(self.__get_save_path(directory, ".mem"), "wb") as file:
            file.write(bytearray(self.__memory))
            print(bytearray(self.__memory))

    def read(self, directory):
        with open(directory, "rb") as file:
            self.__memory = list(file.read())
            print(self.__memory)

    def read_ptrn(self, filename):
        """ Считывает шаблон (коэффициенты нейронов), представленный в виде
        .bmp файла

        Рекомендуется использовать этот метод, если шаблон в .bmp формате
        был сформирован с помощью сторонних программ. В случае,
        если необходимо промежуточное сохранение/считывание нейрона (Neuron)
        используйте методы save() и read() """
        file = Image.open(filename)
        self.__memory = list(file.convert("L").getdata())

    def __get_save_path(self, path, fix) -> str:
        """ Возвращает путь для сохранения Нейрона, включая его имя

        path: директория для сохранения
        fix: обозначение формата файла, например: .jpg, .txt
        """
        return (path + "/" if path[-1:] in "/\\" else "") + self.__name + fix

    def save_ptrn(self, directory):
        """ Сохраняет шаблон (коэффициенты нейронов) в .bmp файле

        Рекомендуется использовать этот метод только для визуализации
        результатов обучения. Для сохранения с целью последующего
        использования в программе рекомендуется использовать метод save().
        """
        file = Image.new("L", (32, 32))
        file.putdata(self.__memory)
        print(self.__get_save_path(directory, ".bmp"))
        file.save(self.__get_save_path(directory, ".bmp"))


class GUI(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Распознование символов на Python")
        self.geometry("500x250+200+300")
        self.choose_file_btn = tk.Button(self,
                                         text="Выбрать",
                                         background="#555",
                                         foreground="#ccc",
                                         padx="10",
                                         pady="4",
                                         font="14",
                                         command=self._show_file_dialog)
        self.choose_file_btn.pack()
        self.recognition_btn = tk.Button(self,
                                         text="Распознать",
                                         background="#c55",
                                         foreground="#ccc")
        self.recognition_btn.pack()
        self.filename = tk.StringVar(master=self, value="F_letter.bmp")
        file_entry = tk.Entry(master=self, textvariable=self.filename)
        file_entry.place(relx=.2, rely=.1, anchor="c")
        self.count = tk.IntVar(master=self, value=1)
        count_entry = tk.Entry(master=self, textvariable=self.count)
        count_entry.place(relx=.2, rely=.3, anchor="c")
        self.recognized_text = tk.StringVar()
        self.recognized_entry = tk.Entry(master=self,
                                         textvariable=self.recognized_text)
        self.recognized_entry.pack()
        self.mainloop()

    def _show_file_dialog(self):
        ask_file = fd.askopenfilename
        self.path = ask_file(initialdir="",
                             title="Выберите файл для распознавания",
                             filetypes=(
                                 ("BMP image files (*.bmp)", "*.bmp"),
                                 ("", "")))
        self.filename.set(self.path.split(sep="/")[-1])

    def recognise_text(self):
        ...


class NeuroNet:
    def __init__(self, name="NeuroNet"):
        self.name = name
        self.big = []
        for letter in range(0x41, 0x5A):
            self.big.append(Neuron(chr(letter)))
        self.small = []
        for letter in range(0x61, 0x7A):
            self.small.append(Neuron(chr(letter)))

    def input(self, in_arr):
        """ Принимает список из 30x30 значений цветов пикселей (0..255)

        in_arr: входной список (должен быть одномерным)
        """
        # TODO: подумать на чём лучше обучать на контурных изображениях или
        # на залитых или на скелетированных
        for neuron in self.big:
            ...
        for neuron in self.small:
            ...


class Cutter:
    """ Класс, предназначенный для разделения графического фрагмента текста
    на отдельные буквы """

    # TODO: Придумать алгоритм определения принадлежности нескольоких
    # областей к одной букве. Возможно по среднему размеру символов (
    # подойдёт только для букв) или по направлению строки. Как, например
    # распознать букву Ы? Возможно, если достоверно известно что она
    # является частью слова (последовательности букв, без цифр) - это можно
    # будет сделать, в связи с тем что "палочка" от буквы "Ы" не похожа ни
    # на одну букву.

    def __init__(self, filename):
        self.image = Image.open(filename)
        self.obj_count = 1
        self.binary = None
        self.marked = None

    def _binarize(self) -> Image.Image:
        """ Преобразует исходное изображение в бинарное (с инверсией)"""
        sb = self.image.convert(mode="1")
        for i in range(32):
            for j in range(32):
                point = (i, j)
                sb.putpixel(point, int(not sb.getpixel(point)))
        self.binary = sb
        return sb

    def cut(self) -> []:
        """ Возвращает связные области бинарного изображения"""

        # Как я понимаю алгоритм разметки изображений:
        # Идём по изображению по строкам слева направо сверху вниз. Если текущая точка принадлежит
        # class Contour:
        #     def __init__(self, img: Image.Image, map: Image.Image, start: ImageDraw.ImageDraw.point):
        #         self.SourceImage = None
        #         self.CurrentImageMap = None
        #     def __passDownLeft(self, p, InvertedAxis):
        #         while self.SourceImage.isInside(p):
        #             self.__commitPoint(p)
        #             p = self.__movePoint(p, 0, 1, InvertedAxis)
        #             left = self.__movePoint(p, -1, 0, InvertedAxis)
        #             if self.SourceImage.isFilled(left):
        #                 p = self.__commitPoint(left)
        #                 while self.SourceImage.isInside(p):
        #                     left = self.__movePoint(p, -1, 0, InvertedAxis)
        #                     if not self.SourceImage.isFilled(left):
        #                         break
        #                     p = self.__commitPoint(left)
        #                     up = self.__movePoint(p, 0, -1, InvertedAxis)
        #                     if self.SourceImage.isFilled(up):
        #                         return
        #             else:
        #                 while self.SourceImage.isInside(p) and not self.SourceImage.isFilled(p):
        #                     right = self.__movePoint(p, 1, 0, InvertedAxis)
        #                     rightUp = self.__movePoint(right, 0, -1, InvertedAxis)
        #                     if not self.SourceImage.isFilled(rightUp):
        #                         return
        #                     self.__commitPoint(rightUp)
        #                     p = self.__commitPoint(right)
        #
        #
        #     def __movePoint(self, src, x, y, InvertedAxis):
        #         p = src
        #         if InvertedAxis:
        #             x = -x
        #             y = -y
        #         p.X += x
        #         p.Y += y
        #         return p
        #
        #     def __commitPoint(self, p):
        #         if (not self.CurrentImageMap.isAssigned(p)) and self.SourceImage.isFilled(p):
        #             self.CurrentImageMap.assignSegment(self, p)
        #             Points.push_back(p)
        #         return p

        class Region:
            """ Класс для хранения заполненной области изображения """

            def __init__(self):
                super().__init__()
                self.top_y = 0
                self.left_x = 0
                self.len = 0
                """ Количество элементов в контуре"""
                self.contour = []
                """ Точки контура. Y-координата = top_y + index:
                [[x1, x2, x3], [x1], [x4, x5, x6], ...]"""
                self.closed = True
                """ Замкнутость контура"""

            def __len__(self):
                return self.len

            def __iter__(self):
                for row in self.contour:
                    yield from row

            def __reversed__(self):
                ...
                raise AttributeError

            def __contains__(self, item):
                x, y = item
                try:
                    return Region.inhere(self.contour[y - self.top_y], x)
                except IndexError:
                    return False

            def __add__(self, other) -> __name__.Region:
                """
                Объединение объектов
                """
                ...

            def add_to_contour(self, point: tuple) -> None:
                """
                Добавление точки контура в объект

                :param point: итерируемый объект содержащий координаты X и Y
                :return: None
                """
                x, y = point[0]
                len_y = len(self.contour)
                bottom_y = self.top_y + len_y - 1
                if y < self.top_y:
                    self.contour = [x] + [[]] * (self.top_y - y)
                    self.len += self.top_y - y + 1
                    return
                if y > bottom_y:
                    self.contour.extend([[]] * (y - bottom_y) + [x])
                    self.len += self.top_y - y + 1
                    return
                current_y = y - self.top_y
                row = self.contour[current_y]
                Region.insort(row, x)
                self.len += 1

            def is_inside_simple(self, point: tuple) -> bool:
                """
                Нахождение точки внутри контра без учёта особых точек

                Осуществляется проведением луча вдоль оси Х и подсчёта
                пересечений. Работает быстрее, чем is_inside для выпуклых
                фигур. Однако для невыпуклых фигур дает сбой, если на своём
                пути луч проходит по касательной к фигуре

                :param point: итерируемый объект содержащий координаты X и Y
                :return: True, если точка внутри контура (принадлежит ему)
                """
                x, y = point
                current_y = y - self.top_y
                index = Region.get_pos(self.contour[current_y], x)
                try:
                    if x == self.contour[index]:
                        return True
                    else:
                        return bool(index % 2)
                except IndexError:
                    return False

            def is_inside(self, point: tuple) -> bool:
                """
                Проверка, находится ли точка внутри контура

                :param point: итерируемый объект содержащий координаты X и Y
                :return: True, если точка внутри контура (принадлежит ему)
                """
                x, y = point
                current_y = y - self.top_y
                index = Region.get_pos(self.contour[current_y], x)
                if x == self.contour[index]:
                    return True

                def is_c_point(x, x_offset, y) -> bool:
                    """
                    Проверяет принадлежность точки контуру

                    :param x: координата
                    :param x_offset: смещение координаты x
                    :param y: координата
                    :return: True, если принадлежит
                    """
                    res = x + x_offset == self.contour[y][
                        Region.get_pos(self.contour[y], x) + x_offset]
                    return res

                crossings = 0
                for x_coord in self.contour[current_y][:index]:
                    upper_l = is_c_point(x_coord, -1, current_y - 1)
                    upper = is_c_point(x_coord, 0, current_y - 1)
                    upper_r = is_c_point(x_coord, 1, current_y - 1)
                    lower_l = is_c_point(x_coord, -1, current_y + 1)
                    lower = is_c_point(x_coord, 0, current_y + 1)
                    lower_r = is_c_point(x_coord, 1, current_y + 1)

                    if upper_l ^ upper ^ upper_r & lower_l ^ lower ^ lower_r:
                        crossings += 1
                return bool(crossings % 2)

            def walk_around_simple(self, start: tuple, clockwise=True):
                """
                Обходит контур выпуклой фигуры от заданной точки.

                 Если заданная точка не принадлежит контуру, обход
                 начинается с ближайшей точки

                :param start: точка от которой начинается обход
                :param clockwise: направление по часовой стрелке
                :return:
                """

            def walk_around(self, start: tuple, clockwise=True):
                """
                 Обходит контур от заданной точки

                 Если заданная точка не принадлежит контуру, обход
                 начинается с ближайшей точки

                :param start: точка от которой начинается обход
                :param clockwise: направление по часовой стрелке
                :return:
                """
                if start not in self.contour:
                    ...
                    return
                else:
                    ...
                # TODO: реализовать метод, так как он понадобится при
                # разбиении изображения
                ...

            @staticmethod
            def get_pos(row: list, val: int) -> int:
                """
                Возвращает предполагаемую позицию элемента в ряду

                :param row: итерируемый объект
                :param val: значение для поиска
                :return: позиция элемента
                """
                start = 0
                end = len(row)
                medium = (end - start) // 2
                while (end - start) >= 1:
                    if val == row[medium]:
                        break
                    if val > row[medium]:
                        start = medium
                    else:
                        end = medium
                return medium  # +1

            @staticmethod
            def insort(row: list, val: int) -> int:
                """
                Вставляет значение в отсортированный ряд

                :param row: список для вставки
                :param val: Добавляемое значение
                :return: индекс добавленного значения в ряду
                """
                index = Region.get_pos(row, val)
                if val != row[index]:
                    row.insert(index, val)
                return index

            @staticmethod
            def inhere(row: list, val: int) -> bool:
                """
                Ищет значение в ряду

                :param row: список для поиска
                :param val: значение для поиска
                :return: True, если элемент найден, иначе False
                """
                if val == row[Region.get_pos(row, val)]:
                    return True

            def get_bitmap(self):
                """ Получение объекта в виде битового массива"""
                ...

            def get_points(self):
                ...

        sb = self._binarize()
        width = sb.size[0]
        height = sb.size[1]

        regions = []
        for i in range(height):
            for j in range(width):
                point = (j, i)
                if sb.getpixel(point):
                    regions.append(point)
                    while sb:
                        ...


if __name__ == "__main__":
    c = Cutter("Example.bmp")
    c.cut()
    nn = NeuroNet()
    inter = GUI()
    nn.input(...)

    neuron = BIP.BmpImageFile()

    neuron = Neuron("Example")
    print(neuron)
    neuron.save_png("D:/Desktop/Python/Lessons-Python/Course_Work/")
    neuron.save("D:/Desktop/Python/Lessons Python/Course_Work/")
