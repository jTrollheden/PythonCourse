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

window = QGroupBox("Box with layout inside!")

okButton = QPushButton("OK")
cancelButton = QPushButton("Cancel")

hbox = QHBoxLayout()
hbox.addStretch(1)
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)

vbox = QVBoxLayout()
vbox.addStretch(1)
vbox.addLayout(hbox)

window.setLayout(vbox)

window.setGeometry(300, 300, 300, 150)
window.setWindowTitle('Buttons')
window.show()

ret = qt_app.exec_()