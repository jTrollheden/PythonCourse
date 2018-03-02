from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

qt_app = QApplication(sys.argv)
#qt_app = QApplication.instance()



window = QGroupBox()
# label = QLabel('This is a game', window)
# label.setFixedWidth(100)
# label.setAlignment(Qt.AlignCenter)

label = QLabel(window)
pixmap = QPixmap('texas-holdem.jpg')
label.setPixmap(pixmap)
label.move(70, 10)
label.show()

#self.blank_word_label = QLabel('This is a game', self)
#self.blank_word_label.setFixedWidth(162)

def DontPlay():
    print("Really?")

def callfunc():
    print("You called")

Call = QPushButton("Call", window)
#button.pressed.connect(DontPlay)
Call.clicked.connect(callfunc)
#button.
Call.show()

Fold = QPushButton("Fold", window)
Fold.clicked.connect(DontPlay)
Bet = QPushButton("Bet", window)
Raise = QPushButton("Raise", window)

StopPlaying = QPushButton("Exit", window)
StopPlaying.clicked.connect(QCoreApplication.instance().quit)

NewGame = QPushButton("New Game")

hbox = QHBoxLayout()
#hbox.addStretch(2)
hbox.addWidget(Call)

hbox.addWidget(Bet)
vbox = QVBoxLayout()
vbox.addStretch(1)
hbox.addWidget(Fold)
box = QHBoxLayout()
hbox.addWidget(Raise)

vbox.addLayout(hbox)
vbox.addSpacing(250)
vbox.addWidget(NewGame)
vbox.addWidget(StopPlaying)
vbox.addStretch(0)

window.setLayout(vbox)
window.setGeometry(200, 200, 150, 700)
window.setWindowTitle('The Game')
window.show()

print(qt_app.exec_())

window2 = QGroupBox()
