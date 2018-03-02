# PySide works almost identically, just by changing the module name:
#from PySide.QtCore import *
#from PySide.QtGui import *
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)

# Normally, one would just use the qt_app created above, but since I want to run applicaitons multiple times
# I have to create new instances of the app in this notebook document
qt_app = QApplication.instance()  # Only necessary when you wish to start multiple separate applications!

# Create a label widget with our text
label = QLabel('Hello world! \n')

# Show it as a standalone widget (this makes the widget become a minimal window)
label.show()

# Run the application's event loop. The application can return
print(qt_app.exec_())


