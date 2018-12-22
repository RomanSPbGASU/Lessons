from tkinter import *
from tkinter import ttk
import PIL.Image
from L7.L7E5 import *


class FileManagerWindow(Tk):
    def __init__(self):
        super().__init__(className=" File Manager")
        self.iconbitmap("Manager.ico")
        self.minsize(400, 320)
        self.config(background="#eee")
        self.rowconfigure(0, weight=0, minsize=32)
        self.rowconfigure(1, weight=0, minsize=32)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=0)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=0)
        self.btn_style = {"relief": FLAT, "borderwidth": 1,
                          "activebackground": "#eee", "background": "#ccc",
                          "overrelief": RIDGE, "compound": LEFT,
                          "font": ("AvantGarde", 12), "foreground": "#333",
                          "activeforeground": "#111"}
        self.btn_margin = {"padx": 3, "pady": 3}

        self.path_entry = Entry(self)
        self.path_entry.grid(row=0, column=0, padx=3, pady=3, sticky=NSEW)

        self.dir_up_image = PhotoImage(file="Dir_up.png")
        self.dir_up_btn = Button(self, name="dir_up", image=self.dir_up_image,
                                 **self.btn_style)
        self.dir_up_btn.grid(row=0, column=1, sticky=NSEW, **self.btn_margin)

        self.home_image = PhotoImage(file="Home.png")
        self.home_btn = Button(self, name="home",
                               image=self.home_image,
                               **self.btn_style)
        self.home_btn.grid(row=0, column=2, sticky=NSEW, **self.btn_margin)

        self.btn_style["anchor"] = W
        self.btn_style["padx"] = 10

        self.fm_treeview = ttk.Treeview(self)
        self.fm_treeview.grid(row=1, column=0, rowspan=8, padx=3, pady=3,
                              sticky=NSEW)

        self.duplicate_image = PhotoImage(file="Duplicate.png")
        self.duplicate_btn = Button(self, text="Дублировать",
                                    image=self.duplicate_image,
                                    **self.btn_style)
        self.duplicate_btn.grid(row=2, column=1, columnspan=4, sticky=NSEW,
                                **self.btn_margin)

        self.duplicate_all_image = PhotoImage(file="Duplicate_all.png")
        self.duplicate_all_btn = Button(self, text="Дублировать всё",
                                        image=self.duplicate_all_image,
                                        **self.btn_style)
        self.duplicate_all_btn.grid(row=3, column=1, columnspan=4, sticky=NSEW,
                                    **self.btn_margin)

        self.del_duplicates_image = PhotoImage(file="Delete_duplicates.png")
        self.del_duplicates_btn = Button(self, text="Удалить дубликаты",
                                         image=self.del_duplicates_image,
                                         **self.btn_style)
        self.del_duplicates_btn.grid(row=4, column=1, columnspan=4,
                                     sticky=NSEW, **self.btn_margin)

        self.rename_image = PhotoImage(file="Rename.png")
        self.rename_btn = Button(self, text="Переименовать",
                                 image=self.rename_image, **self.btn_style)
        self.rename_btn.grid(row=5, column=1, columnspan=4, sticky=NSEW,
                             **self.btn_margin)

        self.move_file_image = PhotoImage(file="Move.png")
        self.move_file_btn = Button(self, text="Переместить",
                                    image=self.move_file_image,
                                    **self.btn_style)
        self.move_file_btn.grid(row=6, column=1, columnspan=4, sticky=NSEW,
                                **self.btn_margin)

        self.minimized = False
        self.minimize_sidebar_image = PhotoImage(file="Minimize.png")
        self.minimize_sidebar_btn = Button(self, width=15, height=20,
                                           image=self.minimize_sidebar_image,
                                           **self.btn_style)
        self.minimize_sidebar_btn.grid(row=8, column=1, sticky=W,
                                       **self.btn_margin)

    def open(self):
        self.mainloop()


if __name__ == "__main__":
    fm = FileManagerWindow()
    fm.open()
