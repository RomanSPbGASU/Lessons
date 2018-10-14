from PIL import Image, ImageDraw, BmpImagePlugin as BIP


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


if __name__ == "__main__":
    # neurons = []
    # for i in range(33):
    #    neurons.append(Neuron("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"[i]))
    # print(neurons)

    # file = open("K_letter", "rb")
    # letter = file.read()
    # print(letter)


    neuron = BIP.BmpImageFile()

    neuron = Neuron("Example")
    print(neuron)
    neuron.save_png("D:/Desktop/Python/Lessons-Python/Course Work/")
    neuron.save("D:/Desktop/Python/Lessons Python/Course Work/")
