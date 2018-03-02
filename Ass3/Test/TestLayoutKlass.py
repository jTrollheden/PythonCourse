# PySide works almost identically, just by changing the module name:
# from PySide.QtCore import *
# from PySide.QtGui import *
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

qt_app = QApplication(sys.argv)


class MyWindow(QGroupBox):
    def __init__(self):
        super().__init__("My window content")  # Call the QWidget initialization as well!

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')


win = MyWindow()
win.show()
qt_app.exec_()