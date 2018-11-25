from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class ReSaverWindow(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Просмотр файлов")
        self.config(background="#eee")
        self.resizable(False, True)
        self.minsize(width=500, height=80)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.file_name = None

        # header (filename)
        self.file_path_var = StringVar(self, "Укажите файл...")
        self.file_entry = Entry(self, textvariable=self.file_path_var,
                                borderwidth=8, relief="flat", width=20,
                                foreground="#aaa", font=("Arial", 10, "bold"))
        self.file_entry.bind("<Return>", self.read_file)
        self.file_entry.grid(row=0, column=0, columnspan=3, sticky=NSEW,
                             padx=(20, 0), pady=3)
        self.fpv_trace_id = self.file_path_var.trace_add(("read", "write"),
                                                         self.clear_hint)
        self.fe_focus_id = self.file_entry.bind("<FocusIn>", self.clear_hint,
                                                "+")
        self.browse_btn = Button(self, text="Выбрать",
                                 font=("Arial", 10, "bold"),
                                 command=self.browse_file, foreground="#444")
        self.browse_btn.grid(row=0, column=3, sticky="we", padx=(5, 20), pady=3)

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
        self.save_btn.grid(row=2, column=2, columnspan=2, sticky="w", padx=(0, 20),
                           pady=(20, 10), ipadx=30)

    def clear_hint(self, *args):
        try:
            if args[2] == "read":
                self.file_entry.delete(0, END)
        except IndexError:
            pass
        self.file_entry.config(foreground="#000")
        if self.file_path_var.trace_info():
            self.file_path_var.trace_remove(("read", "write"),
                                            self.fpv_trace_id)
            self.file_entry.unbind("<FocusIn>", self.fe_focus_id)

    def browse_file(self):
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
            messagebox.showerror("Ошибка", message="Файл не выбран")
        except UnicodeDecodeError:
            with open(file_path, encoding="1251") as file:
                self.file_content_text.insert(0.0, file.read())

    def clear_all(self):
        self.file_entry.delete(0, END)
        self.file_content_text.delete(0.0, END)

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
