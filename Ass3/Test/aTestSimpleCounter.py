# PySide works almost identically, just by changing the module name:
# from PySide.QtCore import *
# from PySide.QtGui import *
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSvg import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

qt_app = QApplication(sys.argv)


class MyCounterModel(QObject):
    # We create a new signal
    data_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.count = 0

    def value(self):
        return self.count

    def increment(self):
        self.count += 1
        self.data_changed.emit()


class MyCounterView(QWidget):
    def __init__(self, model):
        super().__init__()
        self.button = QPushButton("Add 1")
        self.label = QLabel()

        layout = QHBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Connect logic:
        self.model = model
        model.data_changed.connect(self.update)
        self.button.clicked.connect(model.increment)

        self.update()  # Make sure it's up-to-date from the start.

    def update(self):
        self.label.setText("Value is " + str(self.model.value()))


qt_app = QApplication.instance()

counter = MyCounterModel()
view = MyCounterView(counter)
view.show()

qt_app.exec_()