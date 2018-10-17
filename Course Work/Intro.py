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

    def read(self, directory):
        with open(directory, "rb") as file:
            self.__memory = list(file.read())

    def read_ptrn(self, filename):
        file = Image.open(filename)
        self.__memory = list(file.convert("L").getdata())

    def __get_save_path(self, dir, fix):
        return (dir + "/" if dir[-1:] in "/\\" else "") + self.__name + fix

    def save_ptrn(self, directory):
        file = Image.new("L", (30, 30))
        file.putdata(self.__memory)
        print(self.__get_save_path(directory))
        file.save(self.__get_save_path(directory))


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


if __name__ == "__main__":
    # neurons = []
    # for i in range(33):
    #    neurons.append(Neuron("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"[i]))
    # print(neurons)

    # file = open("K_letter", "rb")
    # letter = file.read()
    # print(letter)

    # interface = GUI()
    # a = {1 : "A", 2: 1, 3: None}
    #
    # b = str(a)
    # print(b)
    s = 'автомат'
    s = s.strip("а")
    print(s)
    help(str)
    def help():
        print("На помощь!")
    help(str)
    t = {[1, 2, 3]: "Привет"}
    print(t)
    s = 'автомат'

    s.strip("а")
    print(s)
    a = 10

    b = 5

    a = a ^ b
    print(a)
    a = 10
    b = "ghbd"
    c = a + b
    print(c)
    var = 50 / 25
    print(var)
    a = b = [10, 20, 30, 40, 50]
    a[2] = 100
    print(b)
    var = input("Введите три числа (через пробел):")
    print(var)
    a = 10; b = 0; c = a - b
    neuron = Neuron("Example")
    neuron.read_ptrn("D:\Desktop\Python\Lessons Python\Course Work\K_letter.bmp")
    neuron.save_ptrn("")

    neuron = BIP.BmpImageFile()

    neuron = Neuron("Example")
    print(neuron)
    neuron.save_png("D:/Desktop/Python/Lessons-Python/Course Work/")
    neuron.save("D:/Desktop/Python/Lessons Python/Course Work/")
