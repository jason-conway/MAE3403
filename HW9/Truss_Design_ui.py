# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Truss_Design_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(835, 775)
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(340, 720, 112, 34))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 0, 621, 81))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_GetTruss = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_GetTruss.setGeometry(QtCore.QRect(10, 30, 201, 34))
        self.pushButton_GetTruss.setObjectName("pushButton_GetTruss")
        self.textEdit_filename = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_filename.setGeometry(QtCore.QRect(240, 20, 371, 41))
        self.textEdit_filename.setReadOnly(True)
        self.textEdit_filename.setObjectName("textEdit_filename")
        self.openGLWidget = QtWidgets.QOpenGLWidget(Dialog)
        self.openGLWidget.setGeometry(QtCore.QRect(40, 380, 741, 321))
        self.openGLWidget.setObjectName("openGLWidget")
        self.textEdit_report = QtWidgets.QTextEdit(Dialog)
        self.textEdit_report.setGeometry(QtCore.QRect(50, 120, 511, 181))
        self.textEdit_report.setObjectName("textEdit_report")
        self.textEdit_linknamelong = QtWidgets.QTextEdit(Dialog)
        self.textEdit_linknamelong.setGeometry(QtCore.QRect(700, 120, 104, 31))
        self.textEdit_linknamelong.setObjectName("textEdit_linknamelong")
        self.textEdit_node1long = QtWidgets.QTextEdit(Dialog)
        self.textEdit_node1long.setGeometry(QtCore.QRect(700, 170, 104, 31))
        self.textEdit_node1long.setObjectName("textEdit_node1long")
        self.textEdit_node2long = QtWidgets.QTextEdit(Dialog)
        self.textEdit_node2long.setGeometry(QtCore.QRect(700, 220, 104, 31))
        self.textEdit_node2long.setObjectName("textEdit_node2long")
        self.textEdit_lengthlong = QtWidgets.QTextEdit(Dialog)
        self.textEdit_lengthlong.setGeometry(QtCore.QRect(700, 270, 104, 31))
        self.textEdit_lengthlong.setObjectName("textEdit_lengthlong")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(630, 130, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(610, 180, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(630, 270, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(610, 220, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(600, 90, 71, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 101, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(40, 350, 101, 20))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Wing Spar Structural Optimization"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))
        self.groupBox.setTitle(_translate("Dialog", "Truss File and Load Set"))
        self.pushButton_GetTruss.setText(_translate("Dialog", "Open and Read a Truss File"))
        self.label.setText(_translate("Dialog", "Link Name"))
        self.label_2.setText(_translate("Dialog", "Node1 Name"))
        self.label_3.setText(_translate("Dialog", "Link Length"))
        self.label_4.setText(_translate("Dialog", "Node2 Name"))
        self.label_5.setText(_translate("Dialog", "Longest Link"))
        self.label_6.setText(_translate("Dialog", "Design Report"))
        self.label_7.setText(_translate("Dialog", "Truss Drawing"))

