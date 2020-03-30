# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QTSpline.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1029, 883)
        self.groupBox_Input = QtWidgets.QGroupBox(Dialog)
        self.groupBox_Input.setGeometry(QtCore.QRect(20, 10, 861, 331))
        self.groupBox_Input.setObjectName("groupBox_Input")
        self.label = QtWidgets.QLabel(self.groupBox_Input)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 21))
        self.label.setObjectName("label")
        self.pushButton_loadCalculate = QtWidgets.QPushButton(self.groupBox_Input)
        self.pushButton_loadCalculate.setGeometry(QtCore.QRect(350, 270, 201, 41))
        self.pushButton_loadCalculate.setObjectName("pushButton_loadCalculate")
        self.groupBox_slopeSelect = QtWidgets.QGroupBox(self.groupBox_Input)
        self.groupBox_slopeSelect.setGeometry(QtCore.QRect(90, 80, 751, 181))
        self.groupBox_slopeSelect.setObjectName("groupBox_slopeSelect")
        self.radioButton_useSpec = QtWidgets.QRadioButton(self.groupBox_slopeSelect)
        self.radioButton_useSpec.setGeometry(QtCore.QRect(50, 40, 161, 23))
        self.radioButton_useSpec.setObjectName("radioButton_useSpec")
        self.radioButton_useZero = QtWidgets.QRadioButton(self.groupBox_slopeSelect)
        self.radioButton_useZero.setGeometry(QtCore.QRect(50, 90, 161, 23))
        self.radioButton_useZero.setObjectName("radioButton_useZero")
        self.radioButton_useStandard = QtWidgets.QRadioButton(self.groupBox_slopeSelect)
        self.radioButton_useStandard.setGeometry(QtCore.QRect(50, 140, 161, 23))
        self.radioButton_useStandard.setObjectName("radioButton_useStandard")
        self.lineEdit_slopeFP = QtWidgets.QLineEdit(self.groupBox_slopeSelect)
        self.lineEdit_slopeFP.setGeometry(QtCore.QRect(510, 40, 131, 25))
        self.lineEdit_slopeFP.setObjectName("lineEdit_slopeFP")
        self.lineEdit_slopeSP = QtWidgets.QLineEdit(self.groupBox_slopeSelect)
        self.lineEdit_slopeSP.setGeometry(QtCore.QRect(510, 90, 131, 25))
        self.lineEdit_slopeSP.setObjectName("lineEdit_slopeSP")
        self.label_2 = QtWidgets.QLabel(self.groupBox_slopeSelect)
        self.label_2.setGeometry(QtCore.QRect(390, 40, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_slopeSelect)
        self.label_3.setGeometry(QtCore.QRect(390, 90, 121, 20))
        self.label_3.setObjectName("label_3")
        self.lineEdit_filePath = QtWidgets.QLineEdit(self.groupBox_Input)
        self.lineEdit_filePath.setGeometry(QtCore.QRect(90, 40, 751, 25))
        self.lineEdit_filePath.setObjectName("lineEdit_filePath")
        self.groupBox_Output = QtWidgets.QGroupBox(Dialog)
        self.groupBox_Output.setGeometry(QtCore.QRect(20, 340, 991, 531))
        self.groupBox_Output.setObjectName("groupBox_Output")
        self.lineEdit_firstSegEquation = QtWidgets.QLineEdit(self.groupBox_Output)
        self.lineEdit_firstSegEquation.setGeometry(QtCore.QRect(180, 40, 781, 25))
        self.lineEdit_firstSegEquation.setObjectName("lineEdit_firstSegEquation")
        self.label_equation = QtWidgets.QLabel(self.groupBox_Output)
        self.label_equation.setGeometry(QtCore.QRect(30, 40, 151, 19))
        self.label_equation.setObjectName("label_equation")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_Output)
        self.graphicsView.setGeometry(QtCore.QRect(30, 120, 931, 391))
        self.graphicsView.setObjectName("graphicsView")
        self.label_equation_2 = QtWidgets.QLabel(self.groupBox_Output)
        self.label_equation_2.setGeometry(QtCore.QRect(30, 80, 151, 19))
        self.label_equation_2.setObjectName("label_equation_2")
        self.lineEdit_lastSegEquation = QtWidgets.QLineEdit(self.groupBox_Output)
        self.lineEdit_lastSegEquation.setGeometry(QtCore.QRect(180, 80, 781, 25))
        self.lineEdit_lastSegEquation.setObjectName("lineEdit_lastSegEquation")
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(900, 150, 112, 41))
        self.pushButton_Exit.setObjectName("pushButton_Exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_Input.setTitle(_translate("Dialog", "Input"))
        self.label.setText(_translate("Dialog", "File Name:"))
        self.pushButton_loadCalculate.setText(_translate("Dialog", "Load and Calculate"))
        self.groupBox_slopeSelect.setTitle(_translate("Dialog", "End Slopes"))
        self.radioButton_useSpec.setText(_translate("Dialog", "Use Specified Slopes"))
        self.radioButton_useZero.setText(_translate("Dialog", "Use Zero Slopes"))
        self.radioButton_useStandard.setText(_translate("Dialog", "Use Standard Slopes"))
        self.label_2.setText(_translate("Dialog", "Slope at First Point"))
        self.label_3.setText(_translate("Dialog", "Slope at Last Point"))
        self.groupBox_Output.setTitle(_translate("Dialog", "Output"))
        self.label_equation.setText(_translate("Dialog", "First Segment Equation"))
        self.label_equation_2.setText(_translate("Dialog", "Last Segment Equation"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))
