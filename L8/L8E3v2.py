from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random as rnd


class SortingTabWidget(Frame):
    def __init__(self, master, tab_name="", sort_func=None, *args,
                 **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        # main frame
        self.name = tab_name
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.sort = sort_func

        # input widget
        self.in_text = Text(self, height=3)
        self.in_text.grid(row=0, column=0, sticky=NSEW)
        self.in_text_scroll = Scrollbar(self, command=self.in_text.yview)
        self.in_text_scroll.grid(row=0, column=1, sticky=NSEW)
        self.in_text.config(yscrollcommand=self.in_text_scroll.set)
        self.generate_on_change(self.in_text)
        self.in_text.bind("<<Change>>", self.in_text_on_change, add="+")

        # output widget
        self.out_text = Text(self, state=NORMAL, height=3)
        self.out_text.config(state=DISABLED)
        self.out_text.grid(row=1, column=0, sticky=NSEW)
        self.out_text_scroll = Scrollbar(self, command=self.out_text.yview)
        self.out_text_scroll.grid(row=1, column=1, sticky="nse")
        self.out_text.config(yscrollcommand=self.out_text_scroll.set)

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
        # main part
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
        self.input = "fff"

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky=NSEW)

        # tabs
        tab_names = ("По возрастанию", "По убыванию", "Случайным образом")
        sort_functions = (SortingTabWidget.sort_up,
                          SortingTabWidget.sort_down,
                          SortingTabWidget.randomize)
        self.sorting_widgets = dict()
        for i, name in enumerate(tab_names):
            tab = SortingTabWidget(self.notebook, name, sort_functions[i])
            self.notebook.add(tab, text=tab.name)
            self.sorting_widgets[name] = tab

            def __in_text_on_change(event):
                current_tab = self.notebook.tab(self.notebook.select(), "text")
                s_widget = self.sorting_widgets[current_tab]
                self.input = s_widget.in_text.get(0.0, END)[:-1]

            def __in_text_on_focus_in(event):
                if self.is_combined.get():
                    current_tab = self.notebook.tab(self.notebook.select(),
                                                    "text")
                    s_widget = self.sorting_widgets[current_tab]
                    s_widget.in_text.delete(0.0, END)
                    s_widget.in_text.insert(0.0, self.input)

            tab.in_text.bind("<<Change>>", __in_text_on_change, "+")
            tab.in_text.bind("<FocusIn>", __in_text_on_focus_in, "+")

        # faq
        initial_tab_name = self.notebook.tab(self.notebook.select(), "text")
        initial_tab = self.sorting_widgets[initial_tab_name]
        initial_tab.in_text.insert(0.0,
                                   "Вводите данные. Например: аб я 10 30.2 15")
        initial_tab.out_text.config(state=NORMAL)
        initial_tab.out_text.insert(0.0, "Результат: 10 15 30.2 аб я")
        initial_tab.out_text.config(state=DISABLED)

        def __clear_and_unbind_focus(event):
            # next line working not correctly: it unbind all events
            initial_tab.in_text.unbind("<FocusIn>", focus_in_id)
            initial_tab.in_text.bind("<FocusIn>", __in_text_on_focus_in)
            initial_tab.unbind("<FocusOut>", tab_focus_out_id)
            initial_tab.in_text.delete(0.0, END)
            initial_tab.out_text.delete(0.0, END)

        focus_in_id = initial_tab.in_text.bind("<FocusIn>",
                                               __clear_and_unbind_focus, "+")
        tab_focus_out_id = initial_tab.bind("<FocusOut>",
                                            __clear_and_unbind_focus, "+")

        # options
        self.checkbutton_frame = Frame(self, background="#e00")
        self.checkbutton_frame.grid(row=0, column=0, sticky="ne")

        #   synchronize scrolling
        self.scroll_synchronized = Checkbutton(self.checkbutton_frame,
                                               text="Синхр. прокрутку",
                                               state=DISABLED)
        self.scroll_synchronized.grid(row=0, column=0)

        #   combine input
        self.is_combined = BooleanVar()
        self.combined_input = Checkbutton(self.checkbutton_frame,
                                          text="Объединить ввод",
                                          variable=self.is_combined,
                                          onvalue=True, offvalue=False,
                                          command=self.__change_combined,
                                          state=NORMAL)
        self.combined_input.grid(row=0, column=1)

    def show(self):
        self.mainloop()

    def __change_combined(self):
        if self.is_combined.get():
            ans = False
            not_empty = False
            for w in self.sorting_widgets.values():
                if self.notebook.tab(self.notebook.select(), "text") != w.name:
                    not_empty |= bool(w.in_text.get(0.0, END) != "\n")
            if not_empty:
                ans = messagebox.showinfo("Возможна потеря данных",
                                          "При объединении полей ввода, "
                                          "информация из полей ввода на "
                                          "неактивных вкладках будет потеряна",
                                          type="okcancel")
            if ans == "cancel":
                self.is_combined.set(False)


if __name__ == "__main__":
    sorting_window = SortingBookWindow()
    sorting_window.show()
