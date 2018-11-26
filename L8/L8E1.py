from tkinter import *
from tkinter import ttk


class Deposit(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Схема начисления процентов"
        self.results = []
        self.period_lengths = (1, 3, 6, 12)

        # initial
        self.initial_label = Label(self, text="Начальная сумма, ₽:")
        self.initial_label.grid()
        self.initial_var = DoubleVar()
        self.initial_entry = Entry(self, textvariable=self.initial_var)
        self.initial_entry.grid(row=0, column=1)

        # rate
        self.rate_label = Label(self, text="Размер ставки, %:")
        self.rate_label.grid()
        self.rate_var = DoubleVar()
        self.rate_entry = Entry(self, textvariable=self.rate_var)
        self.rate_entry.grid(row=1, column=1)

        # term
        self.term_label = Label(self, text="Срок инвестирования, лет:")
        self.term_label.grid()
        self.term_var = DoubleVar()
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
        self.scheme_table.column(1, width=95)
        self.scheme_table.column(2, width=95)
        self.scheme_table.column(3, width=95)
        self.scheme_table.column(4, width=95)
        self.initial_item = self.scheme_table.insert("", index=END,
                                                     text="Начальная сумма, ₽")
        self.final_item = self.scheme_table.insert("", index=END,
                                                   text="Конечная сумма, ₽")
        self.income_item = self.scheme_table.insert("", index=END,
                                                    text="Доход, руб")
        self.yield_item = self.scheme_table.insert("", index=END,
                                                   text="Доходность, % год.")

        # buttons
        self.button_frame = Frame(self)
        self.button_frame.grid(row=0, rowspan=3, column=2)
        self.clear_button = Button(self.button_frame, text="Отчистить")
        self.clear_button.grid()
        self.calculate_button = Button(self.button_frame, text="Рассчитать",
                                       command=self.calculate)
        self.calculate_button.grid()

    def clear(self):
        self.initial_var.set("")
        self.rate_var.set("")
        self.term_var.set("")
        self.scheme_table.delete(self.initial_item,
                                 self.final_item,
                                 self.income_item,
                                 self.yield_item)

    def calc_final(self, period):
        init = self.initial_var.get()
        rate = self.rate_var.get()
        term = self.term_var.get()
        return init * (1 + rate / 100 * period / 12) ** (term * 12 / period)

    def calc_income(self, final):
        return float(final) - self.initial_var.get()

    def calc_yield(self, income):
        income = float(income)
        if not income:
            return 0.
        else:
            return income / self.initial_var.get() / self.term_var.get() * 100

    def calculate(self):
        set_item = self.scheme_table.item
        set_item(self.initial_item, values=[self.initial_var.get()] * 4)
        set_item(self.final_item,
                 values=list(map(self.calc_final, self.period_lengths)))
        final_values = self.scheme_table.item(self.final_item)["values"]
        set_item(self.income_item,
                 values=list(map(self.calc_income, final_values)))
        income_values = self.scheme_table.item(self.income_item)["values"]
        set_item(self.yield_item,
                 values=list(map(self.calc_yield, income_values)))

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    deposit = Deposit()
    deposit.show()
