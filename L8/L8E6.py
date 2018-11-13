from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


def insert_text(text_obj: Text):
    file_name = fd.askopenfilename()
    try:
        with open(file_name) as file:
            info = file.read()
            text_obj.insert(1.0, info)
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Не выбран файл для чтения")


def extract_text(text_obj: Text):
    # как добавлять расширение к введённому пользователем имени файла?
    file_name = fd.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", ".html; *.htm"),
                   ("All files", "*.*")))
    try:
        with open(file_name, "w") as file:
            info = text_obj.get(1.0, END)
            file.write(info)
    except FileNotFoundError:
        messagebox.showwarning("Внимание!", "Файл не сохранён")
    else:
        messagebox.showinfo("Сохранение", "Файл сохранён")


def clear_text(text_obj: Text):
    text_obj.delete(1.0, END)


if __name__ == "__main__":
    window = Tk()
    text = Text(width=50, height=25)
    text.grid(columnspan=3)
    open_btn = Button(text="Открыть", command=lambda t=text: insert_text(t))
    open_btn.grid(row=1, column=0, sticky=S)
    save_btn = Button(text="Сохранить", command=lambda t=text: extract_text(t))
    save_btn.grid(row=1, column=1, sticky=S)
    clear_btn = Button(text="Очистить", command=lambda t=text: clear_text(t))
    clear_btn.grid(row=1, column=2, sticky=S)
    window.mainloop()
