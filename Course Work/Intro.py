from PIL import Image, ImageDraw, BmpImagePlugin as BIP
import tkinter as tk
import tkinter.filedialog as fd


class Neuron:
    def __init__(self, name, in_arr=tuple([0] * 900)):
        if len(in_arr) != 900:
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

    def __get_save_path(self, path, fix):
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
        file = Image.new("L", (30, 30))
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
        self.l_count = 1
        self.binary = None

    def _binarize(self) -> Image.Image:
        """ Преобразует исходное изображение в бинарное (с инверсией)"""
        sb = self.image.convert(mode="1")
        for i in range(30):
            for j in range(30):
                point = (i, j)
                sb.putpixel(point, int(not sb.getpixel(point)))
        self.binary = sb
        return sb

    def cut(self) -> []:
        """ Возвращает связные области бинарного изображения"""
        sb = self._binarize()
        width = sb.size[0]
        height = sb.size[1]
        # TODO: разобрать метод point()
        # TODO: разобрать что такое "lookup table"
        for i in range(height):
            for j in range(width):
                point = (i, j)
                print(self.image.getpixel(point))


if __name__ == "__main__":
    c = Cutter("Example.bmp")
    c.cut()
    nn = NeuroNet()
    inter = GUI()
    nn.input(...)

    neuron = BIP.BmpImageFile()

    neuron = Neuron("Example")
    print(neuron)
    neuron.save_png("D:/Desktop/Python/Lessons-Python/Course Work/")
    neuron.save("D:/Desktop/Python/Lessons Python/Course Work/")
