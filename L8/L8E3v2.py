from tkinter import *
from tkinter import ttk
import random as rnd


class SortingTabWidget(Frame):
    def __init__(self, master, tab_name="", sort_func=None, *args,
                 **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.name = tab_name
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.sort = sort_func

        self.in_text = Text(self, height=3)
        self.in_text.insert(0.0, "Вводите данные. Например: аб я 10 30.2 15")
        self.in_text.grid(row=0, column=0, sticky=NSEW)
        self.in_text_scroll = Scrollbar(self, command=self.in_text.yview)
        self.in_text_scroll.grid(row=0, column=1, sticky=NSEW)
        self.in_text.config(yscrollcommand=self.in_text_scroll.set)
        self.__del_info_id = self.in_text.bind("<FocusIn>",
                                               self.__in_text_del_info)
        self.generate_on_change(self.in_text)
        self.in_text.bind("<<Change>>", self.in_text_on_change)

        self.out_text = Text(self, state=NORMAL, height=3)
        self.out_text.insert(0.0, "Результат: 10 15 30.2 аб я")
        self.out_text.config(state=DISABLED)
        self.out_text.grid(row=1, column=0, sticky=NSEW)
        self.out_text_scroll = Scrollbar(self, command=self.out_text.yview)
        self.out_text_scroll.grid(row=1, column=1, sticky="nse")
        self.out_text.config(yscrollcommand=self.out_text_scroll.set)

    def __in_text_del_info(self, event):
        """
        Удаляет текст из поля ввода.

        Отрабатывает только один раз в течении жизни окна
        """
        self.in_text.delete(0.0, END)
        self.in_text.unbind("<FocusIn>", self.__del_info_id)

    @staticmethod
    def generate_on_change(obj):
        """
        Генерация события <<Change>> для obj
        """
        obj.tk.eval('''
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete})} {

                    event generate  $widget <<Change>> -when tail
                }

                # return the result from the real widget command
                return $result
            }
            ''')
        obj.tk.eval('''
            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}
        '''.format(widget=str(obj)))

    def in_text_on_change(self, event):
        values = self.in_text.get(0.0, END).split()
        values = self.sort(values)
        self.out_text.config(state=NORMAL)
        self.out_text.delete(0.0, END)
        self.out_text.insert(0.0, " ".join(values))
        self.out_text.config(state=DISABLED)

    @staticmethod
    def segregated_sort(iterable, reverse=False):
        numbers = []
        strings = []
        for value in iterable:
            try:
                numbers.append(int(value))
            except ValueError:
                try:
                    numbers.append(float(value))
                except ValueError:
                    strings.append(value)
        sorted_as_nums = [str(val) for val in sorted(numbers, reverse=reverse)]
        return sorted_as_nums + sorted(strings, reverse=reverse)

    @staticmethod
    def sort_up(iterable):
        return SortingTabWidget.segregated_sort(iterable, False)

    @staticmethod
    def sort_down(iterable):
        return SortingTabWidget.segregated_sort(iterable, True)

    @staticmethod
    def randomize(iterable):
        values = list(iterable)
        rnd.shuffle(values)
        return values


class SortingBookWindow(Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.title("Сортировка чисел")
        self.minsize(560, 100)
        self.resizable(1, 1)
        self["background"] = "#0e0"
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        style = ttk.Style()
        current_theme = style.theme_use()
        style.theme_settings(current_theme, {
            "TNotebook.Tab": {"configure": {"padding": [0, 1.5]}}})

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky=NSEW)

        tab_names = ("По возрастанию", "По убыванию", "Случайным образом")
        sort_functions = (SortingTabWidget.sort_up,
                          SortingTabWidget.sort_down,
                          SortingTabWidget.randomize)
        self.sorting_widgets = dict()
        for i, name in enumerate(tab_names):
            tab = SortingTabWidget(self.notebook, name, sort_functions[i])
            self.notebook.add(tab, text=tab.name)
            self.sorting_widgets[name] = tab

        self.checkbutton_frame = Frame(self, background="#e00")
        self.checkbutton_frame.grid(row=0, column=0, sticky="ne")

        self.scroll_synchronized = Checkbutton(self.checkbutton_frame,
                                               text="Синхр. прокрутку",
                                               state=DISABLED)
        self.scroll_synchronized.grid(row=0, column=0)

        self.combined_input = Checkbutton(self.checkbutton_frame,
                                          text="Объединить ввод")
        self.combined_input.grid(row=0, column=1)

    def show(self):
        self.mainloop()


if __name__ == "__main__":
    sorting_window = SortingBookWindow()
    sorting_window.show()
