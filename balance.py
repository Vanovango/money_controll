# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'balance.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BalanceWindow(object):
    def setupUi(self, BalanceWindow):
        BalanceWindow.setObjectName("BalanceWindow")
        BalanceWindow.resize(308, 240)
        self.centralwidget = QtWidgets.QWidget(BalanceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(90, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(75, 80, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_result.setFont(font)
        self.label_result.setObjectName("label_result")
        self.btn_show_balance = QtWidgets.QPushButton(self.centralwidget)
        self.btn_show_balance.setGeometry(QtCore.QRect(160, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_show_balance.setFont(font)
        self.btn_show_balance.setObjectName("btn_show_balance")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        BalanceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(BalanceWindow)
        QtCore.QMetaObject.connectSlotsByName(BalanceWindow)

    def retranslateUi(self, BalanceWindow):
        _translate = QtCore.QCoreApplication.translate
        BalanceWindow.setWindowTitle(_translate("BalanceWindow", "Баланс"))
        self.label_title.setText(_translate("BalanceWindow", "Баланс"))
        self.label_result.setText(_translate("BalanceWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.btn_show_balance.setText(_translate("BalanceWindow", "Показать"))
        self.btn_back.setText(_translate("BalanceWindow", "Назад"))
