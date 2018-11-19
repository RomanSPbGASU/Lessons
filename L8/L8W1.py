# import tkinter as tk
#
# example = tk.Tk()
# example.minsize(300, 100)
# example.resizable(1, 1)
# example.title("Пробный интерфейс")
# example.configure(background='#b3dc65', height='200')
# example.configure(width='200')
# # header widget
# header = tk.Frame(example)
# header.configure(height='20', width='200')
# # file_menu widget
# file_menu = tk.Menubutton(header)
# file_menu.configure(text='Файл')
# # Menu_14 widget
# Menu_14 = tk.Menu(file_menu)
# Menu_14.configure(tearoff='false')
# Menu_14.add_command()
# # Command_13 widget
# Command_13 = tk.OptionMenu
# Command_13 = tk.Menuitem.Command(Menu_14)
# Command_13.configure(command_id_arg='false', label='Открыть')
# # Command_14 widget
# Command_14 = tk.Menuitem.Command(Menu_14)
# Command_14.configure(command_id_arg='false', label='Сохранить')
# # Command_15 widget
# Command_15 = tk.Menuitem.Command(Menu_14)
# Command_15.configure(command_id_arg='false', label='Сохранить как...')
# file_menu.grid(column='0', row='0')
# # edit_menu widget
# edit_menu = tk.Menubutton(header)
# edit_menu.configure(text='Правка')
# # Menu_15 widget
# Menu_15 = tk.Menu(edit_menu)
# Menu_15.configure(tearoff='false')
# # Command_16 widget
# Command_16 = tk.Menuitem.Command(Menu_15)
# Command_16.configure(command_id_arg='false', label='Отменить')
# # Command_17 widget
# Command_17 = tk.Menuitem.Command(Menu_15)
# Command_17.configure(command_id_arg='false', label='Повторить')
# # Separator_5 widget
# Separator_5 = tk.Menuitem.Separator(Menu_15)
# # Command_18 widget
# Command_18 = tk.Menuitem.Command(Menu_15)
# Command_18.configure(command_id_arg='false', label='Отчистить')
# edit_menu.grid(column='1', row='0')
# # help_menu widget
# help_menu = tk.Menubutton(header)
# help_menu.configure(text='Помощь')
# # Menu_16 widget
# Menu_16 = tk.Menu(help_menu)
# Menu_16.configure(tearoff='false')
# # Command_19 widget
# Command_19 = tk.Menuitem.Command(Menu_16)
# Command_19.configure(command_id_arg='false', label='Справка...')
# help_menu.grid(column='2', row='0')
# header.grid(column='0', ipady='0', row='0', sticky='new')
# header.rowconfigure(0, minsize='0', pad='0', weight='1')
# header.rowconfigure(1, minsize='0', pad='0', weight='1')
# header.rowconfigure(2, pad='0', weight='1')
# header.columnconfigure(0, weight='0')
# # main widget
# main = tk.Frame(example)
# main.configure(background='#fdede1', height='200', width='200')
# # PanedWindow_12 widget
# PanedWindow_12 = tk.PanedWindow(main)
# PanedWindow_12.configure(background='#f1fccd', height='200',
#                          orient='horizontal', width='200')
# # Pane_13 widget
# Pane_13 = tk.PanedWindow.Pane(PanedWindow_12)
# Pane_13.configure(minsize='100', padx='5', pady='5', sticky='nsew')
# Pane_13.configure(stretch='always')
# # Entry_4 widget
# Entry_4 = tk.Entry(Pane_13)
# Entry_4.configure(text='Entry_4')
# Entry_4.grid(column='0', row='0', sticky='nsew')
# # Pane_14 widget
# Pane_14 = tk.PanedWindow.Pane(PanedWindow_12)
# Pane_14.configure(minsize='100', sticky='ns', stretch='never')
# # button_area widget
# button_area = tk.Frame(Pane_14)
# button_area.configure(background='#fce0fe', height='200', width='200')
# # Button_14 widget
# Button_14 = tk.Button(button_area)
# Button_14.configure(padx='10', pady='10', text='Button_14')
# Button_14.grid(column='0', padx='10', pady='10', row='0', sticky='ew')
# button_area.grid(column='0', row='0', sticky='nsew')
# button_area.rowconfigure(0, weight='1')
# button_area.columnconfigure(0, weight='1')
# # Pane_15 widget
# Pane_15 = tk.PanedWindow.Pane(PanedWindow_12)
# Pane_15.configure(minsize='100', padx='5', pady='5', sticky='nsew')
# Pane_15.configure(stretch='always')
# # Text_6 widget
# Text_6 = tk.Text(Pane_15)
# Text_6.configure(height='10', text='Text_6', width='50')
# Text_6.grid(column='0', row='0', sticky='nsew')
# PanedWindow_12.grid(column='0', padx='5', pady='5', row='0', sticky='nsew')
# main.grid(column='0', pady='25', row='0', sticky='nsew')
# main.propagate(False)
# main.rowconfigure(0, weight='1')
# main.columnconfigure(0, weight='1')
# # footer widget
# footer = tk.Frame(example)
# footer.configure(background='#e1fdfc', height='25', width='200')
# footer.grid(column='0', row='0', sticky='sew')

# values = ["aaa.jpg", "bbb.png", "cccccccccccccccc.gif"]
# separated = []
# first_column_max = 0
# second_column_max = 0
# for value in values:
#     separated.append(value.split("."))
#     if len(separated[-1][0]) > first_column_max:
#         first_column_max = len(separated[-1][0])
#     if len(separated[-1][1]) > second_column_max:
#         second_column_max = len(separated[-1][1])
#
# listbox = Listbox(self, font="Consolas 12")
#
# for i, var in enumerate(separated):
#     string = "{0:{1}}  .{2:{3}}".format(var[0], first_column_max,
#                                         var[1], second_column_max)
#     listbox.insert(i, string)
# listbox.grid(sticky=NSEW)

import tkinter as tk
from tkinter import ttk


def generateOnChange(obj):
    obj.tk.eval('''
            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) || 
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

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


def onEntryChanged(event):
    print("Entry changed")


def onCheckChanged(event):
    print("Check button changed")


def onSpinboxChanged(event):
    print("Spinbox changed")


def onRadioChanged(event):
    print("Radio changed")


if __name__ == '__main__':
    root = tk.Tk()

    frame = tk.Frame(root, width=400, height=400)

    entry = tk.Entry(frame, width=30)
    entry.grid(row=0, column=0)
    generateOnChange(entry)
    entry.bind('<<Change>>', onEntryChanged)

    checkbutton = tk.Checkbutton(frame, command=onCheckChanged)
    checkbutton.grid(row=1, column=0)

    spinbox = tk.Spinbox(frame, width=100, from_=1.0, to=100.0,
                         command=onSpinboxChanged)
    spinbox.grid(row=2, column=0)

    phone = tk.StringVar()
    home = ttk.Radiobutton(frame, text='Home', variable=phone, value='home',
                           command=onRadioChanged)
    home.grid(row=3, column=0, sticky=tk.W)
    office = ttk.Radiobutton(frame, text='Office', variable=phone,
                             value='office', command=onRadioChanged)
    office.grid(row=3, column=0, sticky=tk.E)

    frame.pack()
    root.mainloop()
