# TODO: связи Хэбба - попробовать реализовать алгоритм
#import random



## 1. создать массив случайных чисел 5x5
#strenghts = [random.randint(0, 999)/1000 for i in range(25)]

#ETA = 0.01
#LTP = 1
#POST_NOT_PRE = 2
#PRE_NOT_POST = 3

#ipt = []
#for i in range(5):
#    for j in range(5):
#        strenghts[i * 5 + j] += ETA * ipt[i * 5 + j] * opt
from PIL import Image, ImageDraw


class Neuron:
    def __init__(self, name, *in_arr):
        #if len(in_arr) != 900:
        #    raise valueerror("входной массив должен содержать 30x30 элементов")
        self.__name = str(name)
        self.__in_arr = bytearray(in_arr)
        self.__memory = bytearray()
        self.__out_arr = bytearray()

    def __repr__(self):
        return str(self.__name)

    def __str__(self):
        return str("Нейрон: " + self.__name)

    def save(self, directory = ""):
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

    #neurons = []
    #for i in range(33):
    #    neurons.append(Neuron("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"[i]))
    #print(neurons)

    #file = open("K_letter", "rb")
    #letter = file.read()
    #print(letter)

    with open("K_letter.bmp", "rb") as file:
        data = bytearray(file.read())
    for b in data:
        print(((("{0:0<2s} " * 8) + "\t") * 2 + "\n").format(hex(b)[2:]), sep="")



    neuron = Neuron("Example")
    print(neuron)
    neuron.save_png("D:/Desktop/Python/Lessons-Python/Course Work/")
    neuron.save("D:/Desktop/Python/Lessons Python/Course Work/")

