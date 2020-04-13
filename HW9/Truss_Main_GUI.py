import numpy as np

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from Truss_Design_ui import Ui_Dialog
from Truss_Class import Truss

from OpenGL_2D_class import gl2D, gl2DCircle, gl2DText, glColor3f

class main_window(QDialog):
    def __init__(self):
        super(main_window,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()

        self.setupGLWindows()

        self.truss = None
        self.filename = None

        self.show()

    def assign_widgets(self):
        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)
        self.ui.pushButton_GetTruss.clicked.connect(self.GetTruss)

    def setupGLWindows(self):
        self.glwindow1 = gl2D(self.ui.openGLWidget, self.DrawingCallback)

        self.glwindow1.setViewSize(-10,500,-10,200, allowDistortion=False)

    def DrawingCallback(self):

        if self.truss is not None:
            self.truss.DrawTrussPicture()

    def GetTruss(self):
        self.filename=QFileDialog.getOpenFileName()[0]
        if len(self.filename)==0:
            no_file()
            return
        self.ui.textEdit_filename.setText(self.filename)
        app.processEvents()

        f1 = open(self.filename, 'r')
        data = f1.readlines()
        f1.close()

        self.truss = Truss()

        t = self.truss # a shorter name for convenience

        t.ReadTrussData(data)

        report = t.GenerateReport()

        # put the report in the large text box
        self.ui.textEdit_report.setText(report)

        # fill the small text boxes
        self.ui.textEdit_linknamelong.setText(t.longestLink.name)
        self.ui.textEdit_node1long.setText(t.longestLink.node1.name)
        self.ui.textEdit_node2long.setText(t.longestLink.node2.name)
        self.ui.textEdit_lengthlong.setText('{:8.2f}'.format(t.longest))

        # draw the picture
        [xmin,xmax,ymin,ymax] = self.truss.drawingsize
        dx = xmax - xmin
        dy = ymax - ymin
        xmin -= 0.05*dx
        ymin -= 0.05*dy
        xmax += 0.05*dx
        ymax += 0.05*dy
        self.glwindow1.setViewSize(xmin,xmax,ymin,ymax, allowDistortion=False)

        self.glwindow1.glUpdate()


    def ExitApp(self):
        app.exit()

def no_file():
    msg = QMessageBox()
    msg.setText('There was no file selected')
    msg.setWindowTitle("No File")
    retval = msg.exec_()
    return None

def bad_file():
    msg = QMessageBox()
    msg.setText('Unable to process the selected file')
    msg.setWindowTitle("Bad File")
    retval = msg.exec_()
    return None

if __name__ == "__main__":                                          # given main statement for GUIs
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())