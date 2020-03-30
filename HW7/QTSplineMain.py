import numpy as np
import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from QTSpline import Ui_Dialog
from Cubic_Spline import CubicSpline

class PlotCanvas(FigureCanvas):
    '''De facto default PlotCanvas __init__'''
    def __init__(self, parent, width = None, height = None, dpi = 100): 
        if width == None: #Set window width if not provided
            width = parent.width() / 100
        if height == None: #Set window height if not provided
            height = parent.height() / 100
        fig = Figure(figsize = (width, height), dpi=dpi) #Create and init the figure
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    '''Method for plotting the Cubic Spline Interpolation'''
    def plotCubicSpline(self, coefficients, xValues, yValues):
        self.figure.clf() #Clear the plot
        graphWindow = self.figure.add_subplot(111) #Create the window where the cubic spline will be graphed
        graphWindow.set_title('Cubic Spline Curve Fitting') #Add a nice title
        graphWindow.set_xlabel('X Axis') #Add axis labels
        graphWindow.set_ylabel('Y Axis') #Add axis labels
        graphWindow.plot(xValues, yValues, 'bo') #Plot the original data points
        for i in range(len(xValues) - 1): #Loop through the values in the main x array
            valuesX = np.linspace(xValues[i], xValues[i + 1], 500) #Create 500 points between the current two points in X
            valuesY = np.zeros(len(valuesX))#Create 500 points between the current points in the x array and a placeholder of the same size for storing the values of y
            for j in range(len(valuesX)): #Loop through the values in this valuesX array
                valuesY[j] = coefficients[i][0] + coefficients[i][1] * (valuesX[j] - xValues[i]) + coefficients[i][2] * (valuesX[j] - xValues[i]) ** 2 + coefficients[i][3] * (valuesX[j] - xValues[i]) ** 3 #Solve for the current value of y with the coefficients and add it to the valuesY array
            graphWindow.plot(valuesX, valuesY) #Add the x and calculated y values to the plot
        self.draw() #Display the graph

class main_window(QDialog):
    def __init__(self):
        '''De facto default main_window __init__'''
        super(main_window, self).__init__()   
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.handleClicked() #Execute the proper methods when specific actions occur in the GUI
        graphWindow = self.ui.graphicsView
        self.graph = PlotCanvas(graphWindow)
        self.show()

        self.slope1 = None #Initialize slope1 as None
        self.slope2 = None #Initialize slope2 as None
        self.filename = None #Start with no filename

    '''Set the endSlopeOption variable based on which option is checked in the GUI'''
    def selectedEndSlope(self, int):
        if self.ui.radioButton_useSpec.isChecked(): #Use specified slopes in checked
            self.slope1 = float(self.ui.lineEdit_slopeFP.text()) #Grab the user-entered parameters from the GUI and save as a float
            self.slope2 = float(self.ui.lineEdit_slopeSP.text())
        elif self.ui.radioButton_useZero.isChecked(): #Use zero slopes is checked
            self.slope1 = 0 #Set slope1 and slope2 to zero
            self.slope2 = 0
        elif self.ui.radioButton_useStandard.isChecked(): #Use standard slopes is checked
            self.slope1 = ((self.yValues[1] - self.yValues[0]) / (self.xValues[1] - self.xValues[0])) #Calculate the slope between the first 2 points
            self.slope2 = ((self.yValues[len(self.xValues) - 1] - self.yValues[len(self.xValues) - 2]) / (self.xValues[len(self.xValues) - 1] - self.xValues[len(self.xValues) - 2])) #Calculate the slope between the last 2 points
        return

    def handleClicked(self):
        self.ui.pushButton_loadCalculate.clicked.connect(self.splineTime) #Execute the splineTime method when the calculate button is clicked
        self.ui.pushButton_Exit.clicked.connect(self.exitApplication) #Execute the exitApplication method when the exit button is clicked

    def splineTime(self):
        self.filename = self.ui.lineEdit_filePath.text() #Get the filename from the input box
        self.xValues, self.yValues = np.loadtxt(self.filename, skiprows = 1, unpack = True) #Load data from the specified file into xValues and yValues
        self.selectedEndSlope(1) #Handle the slopes based on the selected button

        self.coefficients = CubicSpline(self.xValues, self.yValues, self.slope1, self.slope2) #Use CubicSpline to obtain the coefficients

        '''Display the equation of the first spline in the textbox'''
        c = self.coefficients[0] 
        strval = '{:.4f} + {:.4f} * (x - {:.4f}) + {:.4f} * (x - {:.4f})^2 + {:.4f} * (x - {:.4f})^3'.format(c[0], c[1], self.xValues[0], c[2], self.xValues[0], c[3], self.xValues[0])
        self.ui.lineEdit_firstSegEquation.setText(strval)

        '''Display the equation of the last spline in the textbox'''
        c = self.coefficients[len(self.coefficients) - 2]
        strval = '{:.4f} + {:.4f} * (x - {:.4f}) + {:.4f} * (x - {:.4f})^2 + {:.4f} * (x - {:.4f})^3'.format(c[0], c[1], self.xValues[len(self.coefficients)-2], c[2], self.xValues[len(self.coefficients)-2], c[3], self.xValues[len(self.coefficients)-2])
        self.ui.lineEdit_lastSegEquation.setText(strval)

        self.graph.plotCubicSpline(self.coefficients, self.xValues, self.yValues) #Pass the coefficients, x values, and y values to the plotting method

    def exitApplication(self): #Method for cleanly exiting the application
        qtInstance.exit() 

if __name__ == "__main__":
    '''De facto default PyQt initialization'''
    qtInstance = QApplication.instance()
    if not qtInstance: qtInstance = QApplication(sys.argv)
    qtInstance.aboutToQuit.connect(qtInstance.deleteLater)
    main_window = main_window()
    sys.exit(qtInstance.exec_())