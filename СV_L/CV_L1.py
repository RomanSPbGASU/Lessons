from tkinter import *


class TrainsTimeTableWindow(Tk):
    def __init__(self):
        super().__init__()
        self.stations = {"Новая деревня", "Старая деревня", "Лисий Нос",
                         "Горская", "Сестрорецк"}
        self.times = {{5, 1, 10, 2, 15, 3, 20, 4, 35, 5, 45},
                      {3, 1, 10, 3, 25, 5, 45},
                      {4, 2, 15, 3, 30, 4, 35, 5, 45},
                      {3, 3, 30, 4, 35, 5, 40}}

# Вариант №9