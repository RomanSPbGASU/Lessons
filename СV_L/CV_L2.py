from tkinter import *
from tkinter import ttk
from L7.L7E5 import *


class FileManagerWindow(Tk):
    def __init__(self):
        super().__init__(className=" File Manager")
        self.minsize(400, 300)
        self.rowconfigure(0, weight=0, minsize=40)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=0)

        self.path_entry = Entry(self)
        self.path_entry.grid(sticky=NSEW)

        self.dir_up_btn = Button(self, name="dir_up", relief=FLAT,
                                 borderwidth=1, activebackground="#f00",
                                 background="#0f0",
                                 highlightbackground="#00f",
                                 highlightcolor="#0ff",
                                 overrelief=RIDGE, highlightthickness=15)
        self.dir_up_btn.grid(row=0, column=1, sticky=NSEW)

        self.home_btn = Button(self, name="home",
                               overrelief=FLAT, default=ACTIVE)
        self.home_btn.grid(row=0, column=2, sticky=NSEW)

        self.fm_treeview = ttk.Treeview(self)
        self.fm_treeview.grid(row=1, column=0, rowspan=7, sticky=NSEW)

        self.duplicate_btn = Button(self, text="Дублировать", highlightthickness=15, highlightcolor="#0ff")
        self.duplicate_btn.grid(row=1, column=1, columnspan=4, sticky=NSEW)

        self.duplicate_all_btn = Button(self, text="Дублировать всё")
        self.duplicate_all_btn.grid(row=2, column=1, columnspan=4, sticky=NSEW)

        self.del_duplicates_btn = Button(self, text="Удалить дубликаты")
        self.del_duplicates_btn.grid(row=3, column=1, columnspan=4,
                                     sticky=NSEW)

        self.rename_btn = Button(self, text="Переименовать")
        self.rename_btn.grid(row=4, column=1, columnspan=4, sticky=NSEW)

        self.move_file_btn = Button(self, text="Переместить")
        self.move_file_btn.grid(row=5, column=1, columnspan=4, sticky=NSEW)

        self.minimize_sidebar_btn = Button(self, width=1, height=1)
        self.minimize_sidebar_btn.grid(row=7, column=1, sticky=W)

    def open(self):
        self.mainloop()


if __name__ == "__main__":
    fm = FileManagerWindow()
    fm.open()
