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
        self.__name = name
        self.__in_arr = in_arr
        self.__memory = []
        self.__out_arr = []

    def __format__(self):
        return self.__name


if __name__ == "__main__":

    neurons = []
    for i in range(33):
        neurons.append(Neuron(chr(0x410 + i)))
    print(neurons)

    file = open("K_letter.png", "r")
    letter = file.re
