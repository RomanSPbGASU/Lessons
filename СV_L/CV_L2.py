from tkinter import *
from tkinter import ttk
import os
from L7.L7E5 import *


class FileManagerWindow(Tk):
    def __init__(self):
        super().__init__(className=" File Manager")
        self.iconbitmap("Manager.ico")
        self.minsize(400, 320)
        self.config(background="#eee")
        self.rowconfigure(0, weight=0, minsize=32)
        self.rowconfigure(1, weight=0, minsize=38)
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
        self.home = "D:/Desktop/Python/Lessons Python/СV_L/test_hierarchy"

        self.path = StringVar(self, self.home)

        self.path_entry = Entry(self, textvariable=self.path,
                                font=("Arial", 10, "bold"), state=DISABLED)
        self.path_entry.grid(row=0, column=0, padx=3, pady=3, sticky=NSEW)

        self.dir_up_image = PhotoImage(file="Dir_up.png")
        self.dir_up_btn = Button(self, name="dir_up", image=self.dir_up_image,
                                 command=self.up_directory,
                                 **self.btn_style)
        self.dir_up_btn.grid(row=0, column=1, sticky=NSEW, **self.btn_margin)

        self.home_image = PhotoImage(file="Home.png")
        self.home_btn = Button(self, name="home",
                               image=self.home_image,
                               command=self.proceed_home_path,
                               **self.btn_style)
        self.home_btn.grid(row=0, column=2, sticky=NSEW, **self.btn_margin)

        self.btn_style["anchor"] = W
        self.btn_style["padx"] = 10

        self.fm_treeview = ttk.Treeview(self, show="tree")
        self.fm_treeview.grid(row=1, column=0, rowspan=8, padx=3, pady=3,
                              sticky=NSEW)
        self.fm_treeview.bind("<Double-1>", self.set_path)

        self.duplicate_text = StringVar(self, "Дублировать")
        self.duplicate_image = PhotoImage(file="Duplicate.png")
        self.duplicate_btn = Button(self, textvariable=self.duplicate_text,
                                    image=self.duplicate_image,
                                    **self.btn_style)
        self.duplicate_btn.grid(row=2, column=1, columnspan=4, sticky=NSEW,
                                **self.btn_margin)

        self.duplicate_all_text = StringVar(self, "Дублировать всё")
        self.duplicate_all_image = PhotoImage(file="Duplicate_all.png")
        self.duplicate_all_btn = Button(self, image=self.duplicate_all_image,
                                        textvariable=self.duplicate_all_text,
                                        **self.btn_style)
        self.duplicate_all_btn.grid(row=3, column=1, columnspan=4, sticky=NSEW,
                                    **self.btn_margin)

        self.del_duplicates_text = StringVar(self, "Удалить дубликаты")
        self.del_duplicates_image = PhotoImage(file="Delete_duplicates.png")
        self.del_duplicates_btn = Button(self, image=self.del_duplicates_image,
                                         textvariable=self.del_duplicates_text,
                                         **self.btn_style)
        self.del_duplicates_btn.grid(row=4, column=1, columnspan=4,
                                     sticky=NSEW, **self.btn_margin)

        self.rename_text = StringVar(self, "Переименовать")
        self.rename_image = PhotoImage(file="Rename.png")
        self.rename_btn = Button(self, textvariable=self.rename_text,
                                 image=self.rename_image, **self.btn_style)
        self.rename_btn.grid(row=5, column=1, columnspan=4, sticky=NSEW,
                             **self.btn_margin)

        self.move_file_text = StringVar(self, "Переместить")
        self.move_file_image = PhotoImage(file="Move.png")
        self.move_file_btn = Button(self, textvariable=self.move_file_text,
                                    image=self.move_file_image,
                                    **self.btn_style)
        self.move_file_btn.grid(row=6, column=1, columnspan=4, sticky=NSEW,
                                **self.btn_margin)

        self.minimized = False
        self.minimize_sidebar_image = PhotoImage(file="Minimize.png")
        self.maximize_sidebar_image = PhotoImage(file="Maximize.png")
        self.minimize_sidebar_btn = Button(self, width=15, height=20,
                                           image=self.minimize_sidebar_image,
                                           command=self.change_sidebar_state,
                                           **self.btn_style)
        self.minimize_sidebar_btn.grid(row=8, column=1, sticky=W,
                                       **self.btn_margin)

    def update_fm_treeview(self):
        self.fm_treeview.delete(*self.fm_treeview.get_children())
        self.init_fm_treeview(self.path.get())

    def up_directory(self):
        if self.path.get() == self.home:
            return
        self.path.set(os.path.dirname(self.path.get()))
        self.update_fm_treeview()

    def proceed_home_path(self):
        self.path.set(self.home)
        self.update_fm_treeview()

    def set_path(self, event):
        item_id = self.fm_treeview.selection()[0]
        item = self.fm_treeview.item(item_id)
        path = item["text"]
        parent = self.fm_treeview.parent(item_id)
        while parent:
            path = self.fm_treeview.item(parent)["text"] + "/" + path
            parent = self.fm_treeview.parent(parent)
        path = self.path.get() + (
            "/" if self.path.get()[-1] is not "/" else "") + path
        if os.path.isdir(path):
            self.path.set(path)
            self.update_fm_treeview()

    def duplicate(self):
        ...

    def init_fm_treeview(self, path, parent=""):
        for i, item in enumerate(os.listdir(path)):
            abs_path = os.path.join(path, item)
            parent_element = self.fm_treeview.insert(parent, "end",
                                                     text=item,
                                                     open=True)
            if os.path.isdir(abs_path):
                self.init_fm_treeview(abs_path, parent_element)

    def change_sidebar_state(self):
        if not self.minimized:
            self.home_btn.grid(row=1, column=1, sticky=NSEW, **self.btn_margin)
            self.duplicate_text.set("")
            self.duplicate_all_text.set("")
            self.del_duplicates_text.set("")
            self.rename_text.set("")
            self.move_file_text.set("")
            self.minimize_sidebar_btn.config(image=self.maximize_sidebar_image)
            self.minimized = True
        else:
            self.home_btn.grid(row=0, column=2, sticky=NSEW, **self.btn_margin)
            self.duplicate_text.set("Дублировать")
            self.duplicate_all_text.set("Дублировать всё")
            self.del_duplicates_text.set("Удалить дубликаты")
            self.rename_text.set("Переименовать")
            self.move_file_text.set("Переместить")
            self.minimize_sidebar_btn.config(image=self.minimize_sidebar_image)
            self.minimized = False

    def show(self):
        self.init_fm_treeview(self.path.get())
        self.mainloop()


if __name__ == "__main__":
    fm = FileManagerWindow()
    fm.show()
