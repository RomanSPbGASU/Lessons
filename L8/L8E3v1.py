from tkinter import *
from tkinter import ttk
import random as rnd


class SortingWidget(Frame):
    def __init__(self, master, sort_func, button_name="", *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.paned_area = PanedWindow(self, orient=HORIZONTAL)
        self.paned_area.grid(sticky="nsew")
        self.entry_pane = Entry(self.paned_area)
        self.paned_area.add(self.entry_pane)

        self.unsorted_entry = Entry(self, width=50)
        self.unsorted_entry.pack(side=LEFT)
        self.sort_button = Button(self, width=20)
        self.sort_button.pack(side=LEFT)
        self.sort_button["text"] = button_name
        self.sorted_label = Label(self, background="#fff", width=50)
        self.sorted_label.pack(side=LEFT)

        self.sort = sort_func

    def sort_up(self):
        numbers = str.split(self.unsorted_entry.cget("text"), " ")
        numbers.sort()
        self.sorted_label = " ".join(numbers)

    def sort_down(self):
        ...

    def randomize(self):
        ...


class SortingWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Сортировка чисел")
        self.minsize(200, 100)
        self.resizable(1, 1)
        self.info_label = Label(self, text="Введите числа через пробел "
                                           "в необходимое окно ввода")
        self.info_label.pack(side=TOP)
        widget_names = ("По возрастанию", "По убыванию", "Случайным образом")
        sort_functions = (SortingWidget.sort_up,
                          SortingWidget.sort_down,
                          SortingWidget.randomize)
        self.sorting_widgets = dict()
        for i, name in enumerate(widget_names):
            this = SortingWidget(self, sort_functions[i], button_name=name)
            this.grid(row=i + 1, column=1)
            self.sorting_widgets[name] = this

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    sorting_window = SortingWindow()
    sorting_window.show()
