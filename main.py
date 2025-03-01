import sqlite3 as sql

import sys
import os

from PyQt5 import QtWidgets

from start import Ui_StartWindow
from add import Ui_AddWindow
from balance import Ui_BalanceWindow
from result import Ui_ResultWindow


def init_db():
    db = sql.connect('spend_history.db')
    cursor = db.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS spend_history (
                date TEXT,
                plus_or_minus TEXT,
                spend_type TEXT,
                cost INTEGER,
                note TEXT,
                balance INTEGER)
                ''')

    cursor.execute(f"""INSERT INTO spend_history VALUES ('0', '0', '0', 0, '0', 0)""")

    db.commit()
    db.close()


def count_balance(db, cursor, plus_or_minus=None, cost=None):

    current_balance = cursor.execute("""SELECT * FROM spend_history""").fetchall()[-1][-1]
    db.commit()

    if plus_or_minus == 'Доходы':
        return current_balance + cost
    elif plus_or_minus == 'Траты':
        return current_balance - cost
    else:
        return current_balance


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
            db = sql.connect('spend_history.db')
            cursor = db.cursor()

            date = class_add.lineEdit_date.text()
            plus_or_minus = class_add.comboBox_plus_or_minus.currentText()
            spend_type = class_add.comboBox_spend_type.currentText()
            cost = class_add.lineEdit_cost.text()
            note = class_add.lineEdit_note.text()

            balance = count_balance(db, cursor, plus_or_minus, int(cost))
            print(balance)

            cursor.execute(f"""INSERT INTO spend_history VALUES
             ('{date}', '{plus_or_minus}', '{spend_type}', {cost}, '{note}', {balance})""")

            db.commit()
            db.close()

            print("Successful save")

            open_add_window()

        def back_():
            AddWindow.close()
            open_start_window()

        class_add.btn_save.clicked.connect(save_)
        class_add.btn_back.clicked.connect(back_)

    def show_result_table():
        global ResultWindow
        ResultWindow = QtWidgets.QMainWindow()
        class_result = Ui_ResultWindow()
        class_result.setupUi(ResultWindow)

        ResultWindow.show()
        StartWindow.close()

        def show():
            print('Working')

        def back_():
            ResultWindow.close()
            open_start_window()

        class_result.btn_show.clicked.connect(show)
        class_result.btn_back.clicked.connect(back_)

    def show_current_balance():
        global BalanceWindow
        BalanceWindow = QtWidgets.QMainWindow()
        class_balance = Ui_BalanceWindow()
        class_balance.setupUi(BalanceWindow)

        BalanceWindow.show()
        StartWindow.close()

        db = sql.connect('spend_history.db')
        cursor = db.cursor()

        balance = cursor.execute("""SELECT * FROM spend_history""").fetchall()[-1][-1]

        class_balance.label_result.setText(f"{balance} руб")

        db.close()

        def back_():
            BalanceWindow.close()
            open_start_window()

        class_balance.btn_back.clicked.connect(back_)

    def close_app():
        exit()

    start_window.btn_add_new.clicked.connect(open_add_window)
    start_window.btn_result.clicked.connect(show_result_table)
    start_window.btn_balance.clicked.connect(show_current_balance)
    start_window.btn_exit.clicked.connect(close_app)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    print(os.path.isfile("spend_history.db"))
    if not os.path.isfile("spend_history.db"):
        init_db()

    open_start_window()

    sys.exit(app.exec_())
