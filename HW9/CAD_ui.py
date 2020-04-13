# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CAD_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(842, 583)
        self.openGLWidget = QtWidgets.QOpenGLWidget(Dialog)
        self.openGLWidget.setGeometry(QtCore.QRect(10, 10, 821, 531))
        self.openGLWidget.setObjectName("openGLWidget")
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(370, 550, 93, 28))
        self.pushButton_Exit.setObjectName("pushButton_Exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HW9 part B - CAD Drawing"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))

