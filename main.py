
import sqlite3 as sql

import sys
import time

from PyQt5 import QtWidgets

from start import Ui_StartWindow
from add import Ui_AddWindow


def open_start_window():
    global StartWindow
    StartWindow = QtWidgets.QMainWindow()
    start_window = Ui_StartWindow()
    start_window.setupUi(StartWindow)

    StartWindow.show()

    def open_add_window():
        global AddWindow
        AddWindow = QtWidgets.QMainWindow()
        class_add = Ui_AddWindow()
        class_add.setupUi(AddWindow)

        AddWindow.show()
        StartWindow.close()

        def save_():

            date = class_add.lineEdit_date.text()
            plus_or_minus = class_add.comboBox_plus_or_minus.currentText()
            spend_type = class_add.comboBox_spend_type.currentText()
            cost = class_add.lineEdit_cost.text()
            note = class_add.lineEdit_note.text()

            print(f"Дата: {date}\nТраты/Доходы: {plus_or_minus}\nТип траты: {spend_type}\n"
                  f"Сумма: {cost}\nПримечание: {note}\n")

            print("Successful save")

            open_add_window()

        def back_():
            AddWindow.close()
            open_start_window()

        class_add.btn_save.clicked.connect(save_)
        class_add.btn_back.clicked.connect(back_)

    def close_app():
        exit()

    start_window.btn_add_new.clicked.connect(open_add_window)
    start_window.btn_exit.clicked.connect(close_app)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    open_start_window()

    sys.exit(app.exec_())
