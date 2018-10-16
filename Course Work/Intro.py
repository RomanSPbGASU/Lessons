from PIL import Image, ImageDraw, BmpImagePlugin as BIP
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb


class Neuron:
    def __init__(self, name, *in_arr):
        # if len(in_arr) != 900:
        #    raise valueerror("входной массив должен содержать 30x30 элементов")
        self.__name = str(name)
        self.__in_arr = bytearray(in_arr)
        self.__memory = bytearray()
        self.__out_arr = bytearray()

    def __repr__(self):
        return str(self.__name)

    def __str__(self):
        return str("Нейрон: " + self.__name)

    def save(self, directory=""):
        """ Сохранение нейрона на диск """
        save_dir = directory + "/" if directory[-1:] in "/\\" else ""
        save_dir += self.__name
        with open(self.__name, "wb") as file:
            for b in self.__memory:
                file.write(b)

    def read_data(self, filename):
        file = open(filename)
        for byte in file:
            self.__memory += byte

    def save_png(self, directory):
        image = Image.open("temp.jpg")
        draw = ImageDraw.Draw(image)
        width = image.size[0]
        height = image.size[1]
        pix = image.load()


class GUI(tk.Tk):
    def __init__(self):
        self = tk.Tk()
        self.title("Распознование символов на Python")
        self.geometry("500x250+200+300")

    def show_file_dialog(self):
        path = fd.askopenfilename(initialdir="",
                                  title="Выберите файл для распознавания",
                                  filetypes=(("BMP image files (*.bmp)", "*.bmp"),
                                             ("", "")))
        self.filename = path.split(sep="/")[-1]


if __name__ == "__main__":
    # neurons = []
    # for i in range(33):
    #    neurons.append(Neuron("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"[i]))
    # print(neurons)

    # file = open("K_letter", "rb")
    # letter = file.read()
    # print(letter)

    root = tk.Tk()
    root.title("Распознование символов на Python")
    root.geometry("500x250+200+300")
    root.show_file_dialog = show_file_dialog
    root.choose_file = tk.Button(root,
                                 text="Выбрать",
                                 background="#555",
                                 foreground="#ccc",
                                 padx="10",
                                 pady="4",
                                 font="14",
                                 command=root.show_file_dialog)
    root.choose_file.pack()
    filename = tk.StringVar()
    file_entry = tk.Entry(textvariable=file_name)
    file_entry.place()
    root.mainloop()

    neuron = BIP.BmpImageFile()

    neuron = Neuron("Example")
    print(neuron)
    neuron.save_png("D:/Desktop/Python/Lessons-Python/Course Work/")
    neuron.save("D:/Desktop/Python/Lessons Python/Course Work/")
