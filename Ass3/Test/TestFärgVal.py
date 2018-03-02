# PySide works almost identically, just by changing the module name:
#from PySide.QtCore import *
#from PySide.QtGui import *
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

qt_app = QApplication(sys.argv)  # Only necessary when you wish to start multiple separate applications!


class ButtonPainter:
    def __init__(self, button):
        self.button = button

    def choose_color(self):
        # Select color
        color = QColorDialog().getColor()

        if color.isValid():
            self.button.setStyleSheet(u'background-color:' + color.name())
        else:
            msgbox = QMessageBox()
            msgbox.setWindowTitle(u'No Color was Selected')
            msgbox.exec_()


# Create top level window/button
button = QPushButton('Choose Color')
# button.clicked.connect() doesn't support passing custom parameters to
# handler function (reference to the  button that we want to paint), so we
# create object that will hold this parameter
button_painter = ButtonPainter(button)
button.clicked.connect(button_painter.choose_color)
button.show()

qt_app.exec_()