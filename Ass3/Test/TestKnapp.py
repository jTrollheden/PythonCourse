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

def sayHello():
    print("Hello World!")

def sayHi():
    print("Hi")
# Create a button, connect it and show it
button = QPushButton("Click me")
button.pressed.connect(sayHi)
button.clicked.connect(sayHello)
button.show()
print( qt_app.exec_() )