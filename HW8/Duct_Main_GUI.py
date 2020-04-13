'''Import... everything?'''
import sys
from scipy.optimize import fsolve
import numpy as np
from math import *
from copy import deepcopy

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Duct_Design import Ui_Dialog
from Duct_Class import Duct

class main_window(QDialog):
    def __init__(self):
        '''De facto default main_window __init__'''
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.handleClicked() #Execute the proper methods when specific actions occur in the GUI
        
        self.duct = None #Init duct as None
        self.filename = None #Init filename as None
        self.startupname = 'Duct Design Input File 1.txt' #Init the program with the textfile pre-selected

        self.show()

    def handleClicked(self):
        self.ui.openReadButton.clicked.connect(self.GetDuct) #Execute the calculateValues method when the calculate button is clicked
        self.ui.exitButton.clicked.connect(self.exitApplication)

    def GetDuct(self):
        if self.startupname is not None:  #Pull file
            self.filename = self.startupname
            self.startupname = None       
        else:
            self.filename = QFileDialog.getOpenFileName()[0]
            if self.filename == None:
                noFileSelected()
            self.ui.filePath.setText('{}'.format(self.filename))
        self.run()

    def run(self):
        file = open(self.filename, 'r') #Open the selected file
        fileData = file.readlines() #Read the entire file as a list of strings
        file.close() #Close the file we opened

        ductObj = Duct()
        ductObj.ReadDuctData(fileData)
        ductObj.FindLongestRun()
        
        self.ui.diffuserID.setText('{}'.format(ductObj.longestRunDiffuser))
        self.ui.runLength.setText('{}'.format(ductObj.longestRunVal))
        self.ui.longestRunPath.setText('{}'.format(ductObj.longestRunPath))

        report = ductObj.GenerateReport()
        self.ui.ductReport.setText(report)

    def exitApplication(self): #Method for cleanly exiting the application
        qtInstance.exit() 

    def noFileSelected(self):
        msg = QMessageBox()
        msg.setText('No File Selected')
        msg.setWindowTitle("No File")
        retval = msg.exec_()
        self.exitApplication()

if __name__ == "__main__":
    '''De facto default PyQt initialization'''
    qtInstance = QApplication.instance()
    if not qtInstance: qtInstance = QApplication(sys.argv)
    qtInstance.aboutToQuit.connect(qtInstance.deleteLater)
    main_window = main_window()

    if main_window.startupname is not None: main_window.GetDuct()

    sys.exit(qtInstance.exec_())
    