import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from QTSatWater import Ui_Dialog
from SatSteamClass import SatSteam

class main_window(QDialog):
    def __init__(self):
        '''De facto default main_window __init__'''
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.handleClicked() #Execute the proper methods when specific actions occur in the GUI
        self.show()
        self.pressure = None #Initialize pressure and quality with no values
        self.quality = None
    
    def handleClicked(self):
        self.ui.pushButton_calculate.clicked.connect(self.calculateValues) #Execute the calculateValues method when the calculate button is clicked
        self.ui.pushButton_Exit.clicked.connect(self.exitApplication) #Execute the exitApplication method when the exit button is clicked

    
    def calculateValues(self):
        pressure = float(self.ui.lineEdit_pressure.text()) #Grab the user-entered parameters from the GUI and save as a float
        quality = float(self.ui.lineEdit_quality.text())

        steamObj = SatSteam(pressure, quality) #Create an object using the SatSteam class with the user's specified pressure and quality

        self.ui.lineEdit_temp.setText('{:.3f}'.format(steamObj.tsat)) #Display the temperature with the calculated temperature from SatSteam
        self.ui.lineEdit_enthalpy.setText('{:.3f}'.format(steamObj.h)) #Display the enthalpy with the calculated enthalpy from SatSteam
        self.ui.lineEdit_entropy.setText('{:.3f}'.format(steamObj.s)) #Display the entropy with the calculated entropy from SatSteam
        self.ui.lineEdit_specificVolume.setText('{:.3f}'.format(steamObj.v)) #Display the specific volume with the calculated specific volume from SatSteam

    def exitApplication(self): #Method for cleanly exiting the application
        qtInstance.exit() 

if __name__ == "__main__":
    '''De facto default PyQt initialization'''
    qtInstance = QApplication.instance()
    if not qtInstance: qtInstance = QApplication(sys.argv)
    qtInstance.aboutToQuit.connect(qtInstance.deleteLater)
    main_window = main_window()
    sys.exit(qtInstance.exec_())
    