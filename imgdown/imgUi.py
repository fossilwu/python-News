# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgUi.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 202)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 10, 141, 31))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 50, 201, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_key = QtWidgets.QLabel(self.layoutWidget)
        self.label_key.setObjectName("label_key")
        self.gridLayout.addWidget(self.label_key, 0, 0, 1, 1)
        self.lineEdit_key = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.gridLayout.addWidget(self.lineEdit_key, 0, 1, 1, 1)
        self.label_num = QtWidgets.QLabel(self.layoutWidget)
        self.label_num.setObjectName("label_num")
        self.gridLayout.addWidget(self.label_num, 1, 0, 1, 1)
        self.lineEdit_num = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.gridLayout.addWidget(self.lineEdit_num, 1, 1, 1, 1)
        self.label_path = QtWidgets.QLabel(self.layoutWidget)
        self.label_path.setObjectName("label_path")
        self.gridLayout.addWidget(self.label_path, 2, 0, 1, 1)
        self.lineEdit_path = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.gridLayout.addWidget(self.lineEdit_path, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 20, 54, 12))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(240, 40, 191, 151))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "开始批量下载"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">图片批量下载器</span></p></body></html>"))
        self.label_key.setText(_translate("Form", "搜关键字"))
        self.label_num.setText(_translate("Form", "图片数量"))
        self.label_path.setText(_translate("Form", "保存位置"))
        self.label_2.setText(_translate("Form", "下载日志："))

