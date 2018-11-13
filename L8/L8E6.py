from tkinter import *
from tkinter import filedialog as fd


def insert_text(text_data: Text):
    file_name = fd.askopenfilename()
    with open(file_name) as file:
        info = file.read()
        text_data.insert(1.0, info)


def extract_text(text_data: Text):
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", ".html; *.htm"),
                                                ("All files", "*.*")))
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
