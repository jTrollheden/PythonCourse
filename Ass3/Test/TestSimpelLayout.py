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
window = QWidget()

okButton = QPushButton("OK")
cancelButton = QPushButton("Cancel")

hbox = QHBoxLayout()
hbox.addStretch(1)
hbox.addWidget(okButton)
hbox.addWidget(cancelButton)

vbox = QVBoxLayout()
vbox.addLayout(hbox)
vbox.addStretch(1)

window.setLayout(vbox)

window.setGeometry(300, 300, 300, 150)  # positionering av fönstret på skärmen först, därefter storleken
window.setWindowTitle('Buttons')
window.show()

ret = qt_app.exec_()