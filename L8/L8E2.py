from tkinter import *


class RainbowWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Rainbow colors")
        self.color_label = Label(self, text="Tap any button ↓",
                                 font=("Arial", 16, "bold"), height=3)
        self.color_label.grid(row=1, columnspan=7)
        self.color_buttons = {}
        colors = ["red", "orange", "yellow", "green",
                  "blue", "indigo", "violet"]
        for i in range(7):
            active_bg = self.get_hex(self.winfo_rgb(colors[i]))
            button = Button(self, width=5, height=2, bg=colors[i],
                            activebackground=active_bg,
                            command=
                            lambda c=colors[i]: self.show_color_name(c))
            button.grid(row=2, column=i)
            self.color_buttons[colors[i]] = button

    @staticmethod
    def get_hex(rgb: tuple):
        return "#%02x%02x%02x" % tuple(map(lambda c: int(c * 0.9 / 256), rgb))

    def show_color_name(self, color):
        self.color_label["fg"] = color
        color_hex = self.get_hex(self.winfo_rgb(color))
        self.color_label["text"] = color + " - " + color_hex

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    rainbow = RainbowWindow()
    rainbow.show()
