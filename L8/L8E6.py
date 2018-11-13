from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


def insert_text(text_data: Text):
    try:
        file_name = fd.askopenfilename()
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Не выбран файл для чтения")
    else:
        with open(file_name) as file:
            info = file.read()
            text_data.insert(1.0, info)


def extract_text(text_data: Text):
    # как добавлять расширение к введённому пользователем имени файла?
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", ".html; *.htm"),
                       ("All files", "*.*")))
    except FileNotFoundError:
        messagebox.showinfo("Информация", "Файл не сохранён")
    else:
        with open(file_name, "w") as file:
            info = text_data.get(1.0, END)
            file.write(info)


if __name__ == "__main__":
    window = Tk()
    text = Text(width=50, height=25)
    text.grid(columnspan=2)
    open_btn = Button(text="Открыть", command=lambda t=text: insert_text(t))
    open_btn.grid(row=1, sticky=E)
    save_btn = Button(text="Сохранить", command=lambda t=text: extract_text(t))
    save_btn.grid(row=1, column=1, sticky=W)

    window.mainloop()
