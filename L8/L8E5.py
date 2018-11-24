from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


class ReSaverWindow(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Просмотр файлов")
        self.file_name = None

        # header (filename)
        Label(self, text="Путь к файлу: ").grid()
        self.file_path_var = StringVar(self, "Укажите файл...")
        self.file_entry = Entry(self, textvariable=self.file_path_var)
        self.file_entry.bind("<Return>", self.read_file)
        self.__focus_id = self.file_entry.bind("<FocusIn>", self.clear_hint)
        self.file_entry.grid(row=0, column=1)
        self.browse_btn = Button(self, text="Выбрать",
                                 command=self.browse_file)
        self.browse_btn.grid(row=0, column=2)

        # main (content)
        self.file_content_text = Text(self)
        self.file_content_text.grid(columnspan=3)

        # footer (buttons)
        self.clear_btn = Button(self, text="Очистить")
        self.clear_btn.grid()
        self.save_btn = Button(self, text="Сохранить")
        self.save_btn.grid(row=2, column=2)

    def browse_file(self):
        self.file_path_var.set(filedialog.askopenfilename(
            filetypes=(("TXT files", "*.txt"), ("All files", "*.*"))))
        self.read_file("<Button-1>")

    def read_file(self, event):
        file_path = self.file_path_var.get()
        try:
            with open(file_path, encoding="utf-8") as file:
                self.file_content_text.insert(0.0, file.read())
        except FileNotFoundError:
            messagebox.showerror("Ошибка",
                                 message="Файл " + file_path + "не найден")

    def clear_hint(self, event):
        self.file_entry.delete(0, END)
        self.file_entry.unbind("<FocusIn>", self.__focus_id)

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    re_saver = ReSaverWindow()
    re_saver.show()
