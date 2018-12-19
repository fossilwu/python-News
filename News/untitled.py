# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 453)
        self.lineEdit_k = QtWidgets.QLineEdit(Form)
        self.lineEdit_k.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.lineEdit_k.setObjectName("lineEdit_k")
        self.label_k = QtWidgets.QLabel(Form)
        self.label_k.setGeometry(QtCore.QRect(20, 30, 54, 12))
        self.label_k.setObjectName("label_k")
        self.label_n = QtWidgets.QLabel(Form)
        self.label_n.setGeometry(QtCore.QRect(240, 30, 54, 12))
        self.label_n.setObjectName("label_n")
        self.label_p = QtWidgets.QLabel(Form)
        self.label_p.setGeometry(QtCore.QRect(20, 70, 61, 21))
        self.label_p.setObjectName("label_p")
        self.lineEdit_n = QtWidgets.QLineEdit(Form)
        self.lineEdit_n.setGeometry(QtCore.QRect(290, 20, 113, 20))
        self.lineEdit_n.setObjectName("lineEdit_n")
        self.lineEdit_p = QtWidgets.QLineEdit(Form)
        self.lineEdit_p.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.lineEdit_p.setObjectName("lineEdit_p")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 121, 51))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(230, 60, 241, 161))
        self.textBrowser.setObjectName("textBrowser")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(40, 250, 256, 192))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_k.setText(_translate("Form", "关键字"))
        self.label_n.setText(_translate("Form", "数量"))
        self.label_p.setText(_translate("Form", "<html><head/><body><p>路径</p></body></html>"))
        self.pushButton.setText(_translate("Form", "执行"))

