##TODO: связи Хэбба - попробовать реализовать алгоритм
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

import sys


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
        return str("Нейрон")

    def save(self, directory):
        file = open(self.__name, "wb")
        for byte in self.__memory:
            file.write(byte)

    def read_data(self, filename):
        file = open(filename)
        for byte in file:
            self.__memory += byte

    def to_png(self):
        signature = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
        ihdr = b"\x00\x00\x00\x0D\x49\x48\x44\x52\x00\x00\x00\x1E\x00\x00\x00\x1E\x08\x02\x00\x00\x00\xFC\x18\xED\xA3"
        idat = b""
        iend = b"\x00\x00\x00\x00\x49\x45\x4E\x44\xAE\x42\x60\x82"


if __name__ == "__main__":

    #neurons = []
    #for i in range(33):
    #    neurons.append(Neuron("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"[i]))
    #print(neurons)

    #file = open("K_letter.png", "rb")
    #letter = file.read()
    #print(letter)

    neuron = Neuron("Example")
    neuron.save("D:/Desktop/Python/Lessons Python/Course Work/")

