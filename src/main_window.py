"""
File with class for main window of application.
"""

import os
import re
import tkinter as tk


class DialogWindow:
    """
    Class for dialog window.
    """

    def __init__(self, parent: "MainWindow"):
        """
        :param parent: parent window.
        """

        self._parent = parent
        self._dialog_window = tk.Toplevel(parent.window)
        self._dialog_window.title("Параметры игры")
        self._dialog_window.geometry("300x150")
        self._dialog_window.resizable(False, False)
        self._dialog_window.grab_set()
        self.label_x_cell_number = tk.Label(self._dialog_window, text="Ширина поля")
        self.label_x_cell_number.place(x=30, y=20)
        self.label_x_cell_number.configure(visible="no")
        self.entry_x_cell_number = tk.Entry(self._dialog_window)
        self.entry_x_cell_number.place(x=120, y=20)
        self.label_y_cell_number = tk.Label(self._dialog_window, text="Высота поля")
        self.label_y_cell_number.place(x=30, y=50)
        self.entry_y_cell_number = tk.Entry(self._dialog_window)
        self.entry_y_cell_number.place(x=120, y=50)
        self.button_ok = tk.Button(self._dialog_window, text="Ок", width=10, height=1,
                                   command=self.set_parameters)
        self.button_ok.place(x=30, y=80)
        self.button_cancel = tk.Button(self._dialog_window, text="Отмена", width=10, height=1,
                                       command=self.close_window)
        self.button_cancel.place(x=120, y=80)

    def close_window(self):
        """
        Method closes dialog window.
        """

        self._dialog_window.destroy()

    def set_parameters(self):
        """
        Method sets parameters.
        """

        x_cell_number = self.entry_x_cell_number.get()
        if not re.match(r"^\d+$", x_cell_number):
            self.entry


class MainWindow:
    """
    Class for main window.
    """

    def __init__(self):
        self.window = tk.Tk()
        self._init_ui()

    def _init_ui(self):
        """
        Method initializes widgets on main window.
        """

        self.window.title("Тренировка памяти")
        self.window.geometry("400x400")
        dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(dir_name, "gui", "icon.ico")
        self.window.iconbitmap(icon_path)
        self._button_start = tk.Button(self.window, text="Старт", width=10, height=1,
                                       command=self.set_game_parameters)
        self._button_start.pack()

    def set_game_parameters(self):
        """
        Method sets game parameters.
        """

        dialog_window = DialogWindow(self)

    def show(self):
        self.window.mainloop()
