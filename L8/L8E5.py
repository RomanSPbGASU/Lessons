from tkinter import *


class ReSaverWindow(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Просмотр файлов")

        # header (filename)
        Label(self, text="Путь к файлу: ").grid()
        self.file_path_var = StringVar(self, "Укажите файл...")
        self.file_entry = Entry(self, textvariable=self.file_path_var)
        self.file_entry.grid(row=0, column=1)
        self.browse_btn = Button(self, text="Выбрать")
        self.browse_btn.grid(row=0, column=2)

        # main (content)
        self.file_content = Text(self)
        self.file_content.grid(columnspan=3)

        # footer (buttons)
        self.clear_btn = Button(self, text="Очистить")
        self.clear_btn.grid()
        self.save_btn = Button(self, text="Сохранить")
        self.save_btn.grid(row=2, column=2)

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    re_saver = ReSaverWindow()
    re_saver.show()
