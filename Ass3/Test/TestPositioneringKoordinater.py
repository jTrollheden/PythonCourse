# PySide works almost identically, just by changing the module name:
#from PySide.QtCore import *
#from PySide.QtGui import *
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

qt_app = QApplication(sys.argv)


window = QWidget()  # Create the simplest widget, just an empty window.

lbl1 = QLabel('Hello', window)  # The QLabel is owned by the window now
lbl1.move(15, 10)

lbl2 = QLabel('world!', window)
lbl2.move(35, 40)

window.setGeometry(30, 30, 100, 70)
window.setWindowTitle('Hello world agian!')
window.show()

ret = qt_app.exec_()