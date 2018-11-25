from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image


class ReSaverWindow(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Просмотр файлов")
        self.resizable(False, True)
        self.minsize(width=500, height=70)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.file_name = None

        # header (filename)
        Label(self, text="Путь к файлу: ").grid(sticky="e")
        self.file_path_var = StringVar(self, "Укажите файл...")
        self.file_entry = Entry(self, textvariable=self.file_path_var,
                                borderwidth=8, relief="flat", width=20)
        self.file_entry.bind("<Return>", self.read_file)
        self.__focus_id = self.file_entry.bind("<FocusIn>", self.clear_hint)
        self.file_entry.grid(row=0, column=1, sticky=NSEW, pady=3)
        self.file_path_var.trace_add("read", self.clear_hint)
        self.browse_btn = Button(self, text="Выбрать",
                                 command=self.browse_file)
        self.browse_btn.grid(row=0, column=2, sticky="w", padx=5, pady=3,
                             ipadx=20)

        # main (content)
        self.file_content_frame = Frame()
        self.file_content_frame.grid(columnspan=3, sticky=NSEW, padx=2)
        self.file_content_frame.grid_rowconfigure(0, weight=1)
        self.file_content_text = Text(self.file_content_frame)
        self.file_content_text.grid(sticky="nsw")
        self.file_content_scroll = Scrollbar(self.file_content_frame)
        self.file_content_text["yscrollcommand"] = self.file_content_scroll.set
        self.file_content_scroll["command"] = self.file_content_text.yview
        self.file_content_scroll.grid(row=0, column=1, sticky="nes")

        # footer (buttons)
        self.clear_btn = Button(self, text="Очистить", command=self.clear_all)
        self.clear_btn.grid(sticky="e", padx=5, pady=5, ipadx=30)
        self.save_btn = Button(self, text="Сохранить", command=self.write_file,
                               background="#f55", highlightbackground="#222")
        self.save_btn.grid(row=2, column=2, sticky="w", padx=5, pady=5,
                           ipadx=30)

    def clear_hint(self, *args):
        self.file_path_var.trace_remove(self.file_path_var.trace_info()[0][0],
                                        self.file_path_var.trace_info()[0][1])

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
            if file_path == "":
                raise ValueError()
            with open(file_path, encoding="utf-8") as file:
                self.file_content_text.insert(0.0, file.read())
        except FileNotFoundError:
            messagebox.showerror("Ошибка",
                                 message="Файл " + file_path + " не найден")
        except ValueError:
            messagebox.showerror("Ошибка", message="Файл не выбран")

    def clear_all(self):
        self.file_entry.delete(0, END)
        self.file_content_text.delete(0.0, END)

    def write_file(self, event=None):
        file_path = self.file_path_var.get()
        with open(file_path, "w") as file:
            file.write(self.file_content_text.get(0.0, END))
        messagebox.showinfo("Сохранение файла",
                            message="Файл " + file_path + " сохранён")

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    re_saver = ReSaverWindow()
    re_saver.show()
