from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Deposit(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Схема начисления процентов"
        self.resizable(True, False)
        self.minsize(526, False)
        self.grid_columnconfigure(0, weight=0, pad=15)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.results = []
        self.period_lengths = (1, 3, 6, 12)
        self.bind_class("Entry", "<Return>", self.focus_next)

        # initial
        Label(self, text="Начальная сумма, ₽:").grid(sticky=E)
        self.initial_var = DoubleVar()
        self.initial_entry = Entry(self, textvariable=self.initial_var)
        self.initial_entry.grid(row=0, column=1, sticky="we")

        # rate
        Label(self, text="Размер ставки, %:").grid(sticky=E)
        self.rate_var = DoubleVar()
        self.rate_entry = Entry(self, textvariable=self.rate_var)
        self.rate_entry.grid(row=1, column=1, sticky="we")

        # term
        Label(self, text="Срок инвестирования, лет:").grid(sticky=E)
        self.term_var = DoubleVar()
        self.term_entry = Entry(self, textvariable=self.term_var)
        self.term_entry.grid(row=2, column=1, sticky="we")

        # scheme
        self.scheme_label = Label(self, text="Схема начисления процентов")
        self.scheme_label.grid(columnspan=3)
        self.scheme_table = ttk.Treeview(self, columns=(1, 2, 3, 4), height=2,
                                         takefocus=FALSE, selectmode="none")
        self.scheme_table.grid(columnspan=3, ipady=20, sticky="we", padx=5,
                               pady=5)
        self.scheme_table.bind("<Button1-Motion>", self.set_table_size)
        self.scheme_table.heading(1, text="Ежемесячно")
        self.scheme_table.heading(2, text="Ежеквартально")
        self.scheme_table.heading(3, text="Раз в полгода")
        self.scheme_table.heading(4, text="Ежегодно")
        self.scheme_table.column("#0", minwidth=135, width=135, stretch=False)
        self.scheme_table.column(1, minwidth=95, width=95, stretch=False)
        self.scheme_table.column(2, minwidth=95, width=95, stretch=False)
        self.scheme_table.column(3, minwidth=95, width=95, stretch=False)
        self.scheme_table.column(4, minwidth=95, width=95, stretch=False)
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
        self.button_frame.grid(row=0, rowspan=3, column=2, sticky="e")
        self.clear_button = Button(self.button_frame, text="Отчистить",
                                   command=self.clear, padx=5, pady=5,
                                   activebackground="#ccc")
        self.clear_button.grid(padx=15, pady=5, ipadx=30, sticky="we")
        self.clear_button.bind("<Return>", self.clear)
        self.calculate_button = Button(self.button_frame, text="Рассчитать",
                                       command=self.calculate,
                                       background="#f55", foreground="#fff",
                                       activebackground="#e33", padx=5, pady=5,
                                       activeforeground="#eee")
        self.calculate_button.grid(padx=15, pady=5, ipadx=30, sticky="we")
        self.calculate_button.bind("<Return>", self.calculate)

    def focus_next(self, event):
        event.widget.tk_focusNext().focus()

    def set_table_size(self, event):
        width = 0
        for i in range(5):
            width += self.scheme_table.column("#%i" % i, "width")
        self.minsize(width, False)
        self.geometry("%ix%i" % (width + 2, 225))

    def clear(self, event=None):
        self.initial_var.set(0.)
        self.rate_var.set(0.)
        self.term_var.set(0.)
        self.scheme_table.item(self.initial_item, values=())
        self.scheme_table.item(self.final_item, values=())
        self.scheme_table.item(self.income_item, values=())
        self.scheme_table.item(self.yield_item, values=())

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

    def calculate(self, event=None):
        set_item = self.scheme_table.item
        try:
            set_item(self.initial_item, values=[self.initial_var.get()] * 4)
            set_item(self.final_item,
                     values=list(map(self.calc_final, self.period_lengths)))
            final_values = self.scheme_table.item(self.final_item)["values"]
            set_item(self.income_item,
                     values=list(map(self.calc_income, final_values)))
            income_values = self.scheme_table.item(self.income_item)["values"]
            set_item(self.yield_item,
                     values=list(map(self.calc_yield, income_values)))
        except TclError as te:
            messagebox.showerror("Ошибка",
                                 "Неверное значение в одном из полей")

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    deposit = Deposit()
    deposit.show()
