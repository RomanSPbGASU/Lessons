from tkinter import *
from tkinter import ttk


class Deposit(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Схема начисления процентов"

        # initial
        self.initial_label = Label(self, text="Начальная сумма, ₽:")
        self.initial_label.grid()
        self.initial_var = StringVar()
        self.initial_entry = Entry(self, textvariable=self.initial_var)
        self.initial_entry.grid(row=0, column=1)

        # rate
        self.rate_label = Label(self, text="Размер ставки, %:")
        self.rate_label.grid()
        self.rate_var = StringVar()
        self.rate_entry = Entry(self, textvariable=self.rate_var)
        self.rate_entry.grid(row=1, column=1)

        # term
        self.term_label = Label(self, text="Срок инвестирования, лет:")
        self.term_label.grid()
        self.term_var = StringVar()
        self.term_entry = Entry(self, textvariable=self.term_var)
        self.term_entry.grid(row=2, column=1)

        # scheme
        self.scheme_label = Label(self, text="Схема начисления процентов")
        self.scheme_label.grid(columnspan=3)
        self.scheme_table = ttk.Treeview(self, columns=(1, 2, 3, 4), height=2)
        self.scheme_table.grid(columnspan=3, ipady=20)
        self.scheme_table.heading(1, text="Ежемесячно")
        self.scheme_table.heading(2, text="Ежеквартально")
        self.scheme_table.heading(3, text="Раз в полгода")
        self.scheme_table.heading(4, text="Ежегодно")
        self.scheme_table.column(1, width=90)
        self.scheme_table.column(2, width=90)
        self.scheme_table.column(3, width=90)
        self.scheme_table.column(4, width=90)
        self.scheme_table.insert("", index=END, text="Начальная сумма, ₽")
        self.scheme_table.insert("", index=END, text="Конечная сумма, ₽")
        self.scheme_table.insert("", index=END, text="Доход, руб")
        self.scheme_table.insert("", index=END, text="Доходность, % год.")

        # buttons
        self.button_frame = Frame(self)
        self.button_frame.grid(row=0, rowspan=3, column=2)
        self.clear_button = Button(self.button_frame, text="Отчистить")
        self.clear_button.grid()
        self.calculate_button = Button(self.button_frame, text="Рассчитать")
        self.calculate_button.grid()

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    deposit = Deposit()
    deposit.show()
    indict = {"initial": None, "rate": None, "term": None}
    func_in_list = [lambda: float(input("Введите начальную сумму, ₽ = ")),
                    lambda: float(input("Введите размер ставки, % = ")),
                    lambda: int(input("Введите срок инвестирования, лет = "))]
    i = 0
    for key in indict:  # добьёмся от пользователя ввода корректных данных
        while 1:
            try:
                indict[key] = func_in_list[i]()
                i += 1
                break
            except ValueError:
                print("\tОшибка. Некорректный ввод")
    print("\t\t\t\t\tСхема начисления процентов")
    print("\t\t\t\t\t\tЕжемесячно     Ежеквартально  Раз в полгода  Ежегодно")
    per_len = [1, 3, 6, 12]
    lines = [["Начальная сумма, ₽:", lambda: indict["initial"], [None] * 4],
             ["Конечная сумма, ₽:", lambda: indict["initial"] * (
                     1 + indict["rate"] / 100 * per_len[i] / 12) ** (
                                                    indict["term"] * 12 /
                                                    per_len[i]),
              [None] * 4],
             ["Доход, руб:", lambda: lines[1][2][i] - indict["initial"],
              [None] * 4],
             ["Доходность, % год.:",
              lambda: lines[2][2][i] / indict["initial"] / indict[
                  "term"] * 100, [None] * 4]]  # данные
    for title, func, output in lines:  # движок
        print(format(title, "22"), end="\t")
        for i in range(4):
            output[i] = func()
            print(format(output[i], "<15.2f"), end="")
        print()
