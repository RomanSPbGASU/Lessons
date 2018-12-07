from tkinter import *
from tkinter import messagebox
from L8.L8E5v2 import EntryWithPlaceholder as EntryWP


class Adder(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title = "Запись в файл"
        self.minsize(420, 110)
        self.rowconfigure(1, weight=1, minsize=20)
        self.columnconfigure(0, weight=0, minsize=100)
        self.columnconfigure(1, weight=1, minsize=100)
        self.columnconfigure(2, weight=0, minsize=100)

        # input
        self.input_var = DoubleVar()
        self.input_entry = EntryWP(self, textvariable=self.input_var,
                                   placeholder="Введите данные...")
        self.input_entry.grid(row=0, column=1, sticky="we")
        self.input_entry.bind("<Return>", self.add_to_numbers)
        self.input_btn = Button(self, text="Ввод", command=self.add_to_numbers)
        self.input_btn.grid(row=0, column=2, ipadx=30, padx=15, pady=10)
        self.input_btn.bind("<Return>", self.add_to_numbers)

        # output
        self.folding_numbers_frame = Frame(self, background="#000")
        self.folding_numbers_frame.grid(columnspan=3, sticky=NSEW)
        self.folding_numbers_frame.grid_columnconfigure(0, weight=1)
        self.folding_numbers_frame.grid_rowconfigure(0, weight=1)
        self.folding_numbers_listbox = Listbox(self.folding_numbers_frame,
                                               justify=CENTER)
        self.folding_numbers_listbox.grid(sticky=NSEW)
        self.folding_numbers_listbox.bind("<Delete>", self.del_number)
        self.folding_numbers_listbox.bind("<Return>", self.show_sum)
        self.folding_numbers_scroll = Scrollbar(self.folding_numbers_frame)
        self.folding_numbers_scroll.grid(row=0, column=1, sticky="nes")
        self.folding_numbers_listbox.config(
            yscrollcommand=self.folding_numbers_scroll.set)
        self.folding_numbers_scroll.config(
            command=self.folding_numbers_listbox.yview)

        # bottom buttons
        self.delete_btn = Button(self, text="Удалить", command=self.del_number)
        self.delete_btn.grid(ipadx=30, padx=(15, 5), pady=10)
        self.delete_btn.bind("<Return>", self.del_number)
        self.clear_btn = Button(self, text="Отчистить", command=self.clear)
        self.clear_btn.grid(row=2, column=1, ipadx=30, padx=5, pady=10)
        self.clear_btn.bind("<Return>", self.clear)
        self.result_btn = Button(self, text="Записать", command=self.show_sum,
                                 background="#f55", foreground="#fff",
                                 activebackground="#e33",
                                 activeforeground="#eee")
        self.result_btn.grid(row=2, column=2, ipadx=30, padx=(5, 15), pady=10)
        self.result_btn.bind("<Return>", self.show_sum)

    def add_to_numbers(self, event=None):
        try:
            self.folding_numbers_listbox.insert(END, self.input_var.get())
            self.input_var.set("")
        except TclError:
            pass

    @staticmethod
    def show_sum(event=None):
        messagebox.showinfo("Запись", "Данные записаны в файл L9E1_result.txt")

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
