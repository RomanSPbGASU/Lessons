from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class ReSaverWindow(Tk):
    def __init__(self, master=None, *args, **kwargs):
        # window
        super().__init__(master, *args, **kwargs)
        self.title("Просмотр файлов")
        self.config(background="#eee")
        self.resizable(False, True)
        self.minsize(width=500, height=80)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.file_name = None
        self._placeholder = "Укажите файл..."

        # header (filename)
        self.file_path_var = StringVar(self, self.placeholder)
        self.file_entry = Entry(self, textvariable=self.file_path_var,
                                borderwidth=8, relief="flat", width=20,
                                foreground="#aaa", font=("Arial", 10, "bold"))
        self.file_entry.bind("<Return>", self.read_file)
        self.file_entry.grid(row=0, column=0, columnspan=3, sticky=NSEW,
                             padx=(20, 0), pady=3)
        self.fe_focus_id = self.file_entry.bind("<FocusIn>",
                                                self.delete_placeholder)
        self.fe_out_id = self.file_entry.bind("<FocusOut>",
                                              self.past_placeholder)
        self.browse_btn = Button(self, text="Выбрать",
                                 font=("Arial", 10, "bold"),
                                 command=self.browse_file, foreground="#444",
                                 activebackground="#999",
                                 activeforeground="#fff")
        self.browse_btn.grid(row=0, column=3, sticky="we", padx=(5, 20),
                             pady=3)

        # main (content)
        self.file_content_frame = Frame()
        self.file_content_frame.grid(columnspan=4, sticky=NSEW, padx=2)
        self.file_content_frame.grid_rowconfigure(0, weight=1)
        self.file_content_text = Text(self.file_content_frame, takefocus=0)
        self.file_content_text.grid(sticky="nsw")
        self.file_content_scroll = Scrollbar(self.file_content_frame)
        self.file_content_text["yscrollcommand"] = self.file_content_scroll.set
        self.file_content_scroll["command"] = self.file_content_text.yview
        self.file_content_scroll.grid(row=0, column=1, sticky="nes")

        # footer (buttons)
        self.clear_btn = Button(self, text="Очистить", command=self.clear_all,
                                font=("Arial", 10, "bold"), foreground="#333")
        self.clear_btn.grid(sticky="e", padx=(20, 0), pady=(20, 10), ipadx=40)
        self.save_btn = Button(self, text="Сохранить", command=self.write_file,
                               background="#f55", highlightbackground="#eee",
                               foreground="#fff", font=("Arial", 10, "bold"),
                               activebackground="#e33",
                               activeforeground="#eee", highlightcolor="#000")
        self.save_btn.grid(row=2, column=2, columnspan=2, sticky="w",
                           padx=(0, 20),
                           pady=(20, 10), ipadx=30)

    @property
    def placeholder(self):
        return "\0" + str(self._placeholder)

    @placeholder.setter
    def placeholder(self, value):
        if value[0] == "\0":
            self._placeholder = value[1:]
        else:
            self._placeholder = value

    @placeholder.deleter
    def placeholder(self):
        del self._placeholder

    def past_placeholder(self, *args):
        if not self.file_entry.get():
            self.file_entry.delete(0, END)
            self.file_entry.insert(0, self.placeholder)
            self.file_entry.config(foreground="#aaa")

    def delete_placeholder(self, *args):
        if self.file_entry.get() == self.placeholder:
            self.file_entry.delete(0, END)
            self.file_entry.config(foreground="#000")

    def browse_file(self):
        self.delete_placeholder()
        self.file_path_var.set(filedialog.askopenfilename(
            filetypes=(("All files", "*.*"),
                       ("TXT files", "*.txt"),
                       ("HTML files", "*.html|*.htm"),
                       ("Python files", "*.py"))))
        self.read_file("<Button-1>")

    def read_file(self, event):
        file_path = self.file_path_var.get()
        try:
            with open(file_path, encoding="utf-8") as file:
                self.file_content_text.insert(0.0, file.read())
        except FileNotFoundError:
            messagebox.showerror("Ошибка",
                                 message="Файл " + file_path + " не найден")
            self.past_placeholder()
        except UnicodeDecodeError:
            try:
                with open(file_path, encoding="1251") as file:
                    self.file_content_text.insert(0.0, file.read())
            except FileNotFoundError:
                messagebox.showerror("Ошибка",
                                     message=
                                     "Файл " + file_path + " не найден")
                self.past_placeholder()

    def clear_all(self):
        self.file_content_text.delete(0.0, END)
        if self.file_entry.focus_get() != self.file_entry:
            self.file_entry.delete(0, END)
            self.past_placeholder()
        else:
            self.file_entry.delete(0, END)

    def write_file(self, event=None):
        file_path = self.file_path_var.get()
        try:
            if file_path == "":
                raise ValueError()
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.file_content_text.get(0.0, END))
        except FileNotFoundError:
            messagebox.showerror("Ошибка",
                                 message="Файл " + file_path + " не найден")
        except ValueError:
            messagebox.showerror("Ошибка", message="Файл не выбран")
        else:
            messagebox.showinfo("Сохранение файла",
                                message="Файл " + file_path + " сохранён")

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    re_saver = ReSaverWindow()
    re_saver.show()
