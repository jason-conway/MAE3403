import numpy as np

# standard PyQt5 imports
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QEvent

# standard OpenGL imports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGL_2D_class import gl2D, gl2DText, gl2DCircle

# the ui created by Designer and pyuic
from CAD_ui import Ui_Dialog

# import the Problem Specific class
# .... in this case, there is none ...


class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        # setup the GUI
        self.ui.setupUi(self)

        # create and setup the GL window object
        self.setupGLWindows()

        # and define any Widget callbacks (buttons, etc) or other necessary setup
        self.assign_widgets()

        # show the GUI
        self.show()

    def assign_widgets(self):  # callbacks for Widgets on your GUI
        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)

    def ExitApp(self):
        app.exit()

    # Setup OpenGL Drawing and Viewing
    def setupGLWindows(self):  # setup all GL windows
        # send it the   GL Widget     and the drawing Callback function
        self.glwindow1 = gl2D(self.ui.openGLWidget, self.DrawingCallback)

        # set the drawing space:    xmin  xmax  ymin   ymax
        self.glwindow1.setViewSize(-12, 132, -7.7, 84.7, allowDistortion=False)


    def DrawingCallback(self):
        # this is what actually draws the picture

        # Draw Perimeter of the part
        glColor3f(0, 0, 0)
        glLineWidth(3)
        glBegin(GL_LINE_STRIP)  # begin drawing connected lines
        glVertex2f(0, 0)
        glVertex2f(0, 44)
        glVertex2f(36, 77)
        glVertex2f(78, 77)
        glVertex2f(120, 44)
        glVertex2f(120, 0)
        glVertex2f(0, 0)
        glEnd()

        # Draw the holes in the part

        glColor3f(0, 0, 0)  #
        glLineWidth(3)

        radius = 18     # Circle 1
        gl2DCircle(36, 36, radius, fill=False)

        radius = 10     # Circle 2
        gl2DCircle(84, 20, radius, fill=False)

        # Write the name of the Contributors

        xmin, xmax, ymin, ymax = -12, 132, -7.7, 84.7
        dy = ymax - ymin

        xavg = (xmax - xmin) / 2.8

        glColor3f(1, 1, 1)
        gl2DText('Jason Conway', xavg, ymax - 0.15 * dy)
        gl2DText('Abdalrahman (Mann) Mansy', xavg, ymax - 0.25 * dy)
        gl2DText('Malorie Travis', xavg, ymax - 0.35 * dy)

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())
