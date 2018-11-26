from tkinter import *
from tkinter import messagebox


class Adder(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Суммирование чисел"
        self.minsize(420, 110)
        self.rowconfigure(1, weight=1, minsize=20)
        self.columnconfigure(0, weight=0, minsize=100)
        self.columnconfigure(1, weight=1, minsize=100)
        self.columnconfigure(2, weight=0, minsize=100)

        # input
        Label(self, text="Введите число: ").grid(sticky="e")
        self.input_var = DoubleVar()
        self.input_entry = Entry(self, textvariable=self.input_var)
        self.input_entry.grid(row=0, column=1, sticky="we")
        self.input_entry.bind("<Return>", self.add_to_numbers)
        self.input_btn = Button(self, text="Ввод", command=self.add_to_numbers)
        self.input_btn.grid(row=0, column=2, ipadx=30, padx=15, pady=10)
        self.input_btn.bind("<Return>", self.add_to_numbers)

        # output
        self.folding_numbers_listbox = Listbox(self, justify=CENTER)
        self.folding_numbers_listbox.grid(columnspan=3, sticky=NSEW)
        self.folding_numbers_listbox.bind("<Delete>", self.del_number)
        self.folding_numbers_listbox.bind("<Return>", self.show_sum)

        # bottom buttons
        self.delete_btn = Button(self, text="Удалить", command=self.del_number)
        self.delete_btn.grid(ipadx=30, padx=(15, 5), pady=10)
        self.delete_btn.bind("<Return>", self.del_number)
        self.clear_btn = Button(self, text="Отчистить", command=self.clear)
        self.clear_btn.grid(row=2, column=1, ipadx=30, padx=5, pady=10)
        self.clear_btn.bind("<Return>", self.clear)
        self.result_btn = Button(self, text="Результат", command=self.show_sum,
                                 background="#f55", foreground="#fff",
                                 activebackground="#e33",
                                 activeforeground="#eee")
        self.result_btn.grid(row=2, column=2, ipadx=30, padx=(5, 15), pady=10)
        self.result_btn.bind("<Return>", self.show_sum)

    def add_to_numbers(self, event=None):
        try:
            print("Введено в Entry:      ", self.input_entry.get())
            print("Сохранено в DoubleVar:", self.input_var.get())
            self.folding_numbers_listbox.insert(END, self.input_var.get())
            print("Добавлено в Listbox:  ", self.folding_numbers_listbox.get(END))
            print("_" * 40)
            self.input_var.set("")
        except TclError:
            pass

    def show_sum(self, event=None):
        messagebox.showinfo("Результат", "Сумма введённых чисел: " + str(sum(
            self.folding_numbers_listbox.get(0, END))))

    def clear(self, event=None):
        self.input_var.set("")
        self.folding_numbers_listbox.delete(0, END)

    def del_number(self, event=None):
        listbox = self.folding_numbers_listbox
        if listbox.curselection():
            listbox.delete(listbox.curselection())

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    adder = Adder()
    adder.show()

