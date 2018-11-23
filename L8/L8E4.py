from re import compile
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Adder(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Суммирование чисел"
        # self.minsize(400, 250)
        self.resizable(0, 0)
        self.sum = 0

        # input
        Label(self, text="Введите число: ").grid()
        self.input_var = DoubleVar()
        self.input_entry = Entry(self, textvariable=self.input_var)
        self.input_entry.grid(row=0, column=1)
        self.input_btn = Button(self, text="Ввод").grid(row=0, column=2)

        # output
        self.output_treeview = ttk.Treeview(selectmode=NONE, show="tree",
                                            columns=(1, 2, 3))
        self.output_treeview.heading("#0")
        self.output_treeview.column("#0", width=0)
        self.output_treeview.heading("#1")
        self.output_treeview.column("#1")
        self.output_treeview.heading("#2")
        self.output_treeview.column("#2")
        self.output_treeview.insert("", "end",
                                    values=("Второе", "Третье"), )
        self.output_treeview.insert("", "end",
                                    values=("Второе", "Третье"), )
        self.output_treeview.insert("", 0,
                                    values=(3, "Второе", "Третье"), )
        self.output_treeview.grid(row=2, columnspan=3)
        self.output_treeview.config(columns=(1, 2, 3, 4, "five"))
        self.output_treeview.heading("#3")
        self.output_treeview.column("#3")

        # bottom buttons
        self.clear_btn = Button(self, text="Отчистить").grid(row=3)
        self.result_btn = Button(self, text="Результат").grid(row=3, column=2)

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    adder = Adder()
    adder.show()

    # print("Введите слово 'stop' для получения результата")
    # res = 0
    # while 1:
    #     ptrn = compile(r"[+-]*[0-9]+")  # шаблон для ввода числа в C++ стиле
    #     stop = compile(r"stop")
    #     try:
    #         inp = input("Введите целое число: ")
    #         if stop.search(inp):
    #             break
    #         if inp == '':
    #             raise IOError()
    #         num = int(ptrn.match(inp).string)
    #         res += num
    #     except (ValueError, AttributeError):
    #         print("Необходимо ввести число, а не строку!!!")
    #     except IOError:
    #         print("Вы не ввели значение!")
    # print("Сумма введённых чисел равна: ", res)
