#from PySide.QtCore import *
#from PySide.QtGui import *
#from PySide.QtSvg import *
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
#from PyQt4.QtSvg import *
from PyQt5.QtCore import *
import cardlib as cl
from PyQt5.QtGui import *
from PyQt5.QtSvg import *
from PyQt5.QtWidgets import *
import sys

qt_app = QApplication(sys.argv)
qt_app = QApplication.instance()

class CommonResources:  # KOMMER BLI GAME KLASSEN
    def __init__(self):
        self.cards = ['QS', 'AD', '5D', '6C', '3H']
        self.marked_cards = [False]*len(self.cards)
        self.pot = 10000
        self.folded = False
        self.cb = None
        self.usrname = "Sofia"

    def set_callback(self, cb):
        # Instead of the sophisticated signal system, I have a simple callback here.
        # This only works if there is just one viewer!
        # But I want to reduce the complexity in this example to make it clear why things occur.
        self.cb = cb

    def active(self):
        return credits > 0 and not self.folded

    def mark_position(self, i):
        # Mark the card as position "i" to be thrown away
        self.marked_cards[i] = not self.marked_cards[i]
        if self.cb is not None: self.cb()

    def marked(self, id):
        return self.marked_cards[id]


class Player:  # ÄR TILLSAMMANS MED GAME KLASSEN I EN ANNAN FIL
    def __init__(self):
        # Lets use some hardcoded values for most of this to start with:
        self.cards = ['QS', 'AD']
        self.marked_cards = [False]*len(self.cards)
        self.credits = 100
        self.folded = False
        self.cb = None
        self.usrname = "Sofia"

    def set_callback(self, cb):
        # Instead of the sophisticated signal system, I have a simple callback here.
        # This only works if there is just one viewer!
        # But I want to reduce the complexity in this example to make it clear why things occur.
        self.cb = cb

    def active(self):
        return credits > 0 and not self.folded

    def mark_position(self, i):
        # Mark the card as position "i" to be thrown away
        self.marked_cards[i] = not self.marked_cards[i]
        if self.cb is not None: self.cb()

    def marked(self, id):
        return self.marked_cards[id]


class TableBackground(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.tile = QPixmap('cards/table.png')
        self.setBackgroundBrush(QBrush(self.tile))


class CardSvgItem(QGraphicsSvgItem):
    def __init__(self, renderer, id):
        super().__init__()
        self.setSharedRenderer(renderer)
        self.position = id


class CardView(QGraphicsView):
    # Underscores indicate a private function!
    def __read_cards():  # Ignore the PyCharm warning on this line. It's correct.
        """
        Reads all the 52 cards from files.
        :return: Dictionary of SVG renderers
        """
        all_cards = dict()  # Dictionaries let us have convenient mappings between cards and their images
        for suit_file, suit in zip('HDSC', range(4)): # Check the order of the suits here!!!
            for value_file, value in zip(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'], range(2, 15)):
                file = value_file + suit_file
                key = (value, suit)  # I'm choosing this tuple to be the key for this dictionary
                all_cards[key] = QSvgRenderer('cards/' + file + '.svg')
        return all_cards

    # We read all the card graphics as static class variables:
    back_card = QSvgRenderer('cards/Red_Back_2.svg')
    all_cards = __read_cards()

    def __init__(self, active_instance, card_spacing=250, padding=10):
        """
        Initializes the view to display the content of the given model
        :param cards_model: A model that represents a set of cards.
        The model should have: data_changed, cards, clicked_position, flipped,
        :param card_spacing: Spacing between the visualized cards.
        :param padding: Padding of table area around the visualized cards.
        """

        self.scene = TableBackground()
        super().__init__(self.scene)

        self.setFixedSize(150*len(active_instance.cards), 200)

        self.card_spacing = card_spacing
        self.padding = padding
        self.active_instance = active_instance

        # Whenever the this window should update, it should call the "change_cards" method.
        # This can, for example, be done by connecting it to a signal.
        # The view can listen to changes:
        active_instance.data_changed.connect(self.change_cards)
        # It is completely optional if you want to do it this way, or have some overreaching Player/GameState
        # call the "change_cards" method instead. z

        # Add the cards the first time around to represent the initial state.
        self.change_cards()

    def change_cards(self):  # Fix so that the
        # Add the cards from scratch:
        self.scene.clear()  # Removes old cards
        for i, card in enumerate(self.active_instance.cards):  # Player/center cards goes here
            graphics_key = (card.value, card.suit)
            renderer = self.back_card if self.model.flipped(i) else self.all_cards[graphics_key]
            # TODO: När ska korten vara flippade?
            c = CardSvgItem(renderer, i)

            shadow = QGraphicsDropShadowEffect(c)
            shadow.setBlurRadius(10.)
            shadow.setOffset(5, 5)
            shadow.setColor(QColor(0, 0, 0, 180))  # Semi-transparent black!
            c.setGraphicsEffect(shadow)

            # Position cards
            c.setPos(c.position * self.card_spacing, 0)

            self.scene.addItem(c)

        self.update_view()

    def update_view(self):
        for c in self.scene.items():
            # Lets have the cards take up almost the (current) full height
            card_height = c.boundingRect().bottom()
            scale = (self.height()-2*self.padding)/(card_height)

            c.setPos(c.position * self.card_spacing*scale, 0)
            c.setScale(scale)
            #c.setOpacity(0.5 if self.active_instance.marked_cards[c.position] else 1.0)

        # Put the scene bounding box
        self.scene.setSceneRect(-self.padding, -self.padding, self.viewport().width(), self.viewport().height())

    def resizeEvent(self, painter):
        # If the widget is resize, we gotta adjust the card sizes.
        # QGraphicsView automatically re-paints everything when we modify the scene.
        self.update_view()
        super().resizeEvent(painter)

    # This is the Controller part of the GUI, handling input events that modify the Model
    def mousePressEvent(self, event):  # Not sure what this will be used for since the game -> driven by buttons
        item = self.scene.itemAt(event.pos(), self.transform())
        if item is not None:
            # Report back that the Model that the user marked a given position:
            self.active_instance.mark_position(item.position)


class PlayerView(QGroupBox):
    def __init__(self, player):
        super().__init__()
        self.player = player

        layout = QHBoxLayout()
        vlayout = QVBoxLayout()
        layout.addLayout(vlayout)
        self.setLayout(layout)

        self.who_money = QLabel()
        vlayout.addWidget(self.who_money)

        self.cards = CardView(self.player)
        layout.addWidget(self.cards)

        self.update()

    def update(self):
        self.who_money.setText("Player: " + str(self.player.usrname) + " has " + str(self.player.credits) + "kr")


class GameView(QGroupBox):
    def __init__(self, common_resources):
        super().__init__()
        self.cresources = common_resources

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.cards = CardView(self.cresources)


        player_view = PlayerView(Player())
        player_view2 = PlayerView(Player())

        layout.addWidget(player_view)
        layout.addWidget(self.cards)
        layout.addWidget(player_view2)

        self.setStyleSheet("""
            color: white; 
            background-image: url(/Users/joeltrollheden/Documents/GitHub/PythonCourse/Ass3/cards/table.png);
        """);


class InteractionBox(QGroupBox):
    def __init__(self, CommonResources):
        super().__init__()

        # Layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.cresources = CommonResources

        # Buttons
        bet_raiseb = QPushButton("Bet/Raise")  # Ändra så att texten beror på state
        call_checkb = QPushButton("Call/Check")  # Ändra så att texten beror på state
        foldb = QPushButton("Fold")
        new_gameb = QPushButton("New Game")
        stop_playingb = QPushButton("Exit")
        self.buttons_game = [bet_raiseb, call_checkb, foldb]
        self.buttons_status = [new_gameb, stop_playingb]

        def bet_raise():
            1+1
            # Add money to the pot (GameState)

        def check_call():
            1+1
            # Call the previous bet/raise or just check

        def fold_cards():
            1+1
            # Fold

        def new_game():
            1+1
            # Ändra GameState till Playing

        def stop_playing():
            choice = QMessageBox.question(self, "", "Do you want to quit?", QMessageBox.Yes | QMessageBox.No)
            if choice == QMessageBox.Yes:
                sys.exit()
            else:
                pass

        self.buttons_game[0].clicked.connect(bet_raise)
        self.buttons_game[1].clicked.connect(check_call)
        self.buttons_game[2].clicked.connect(fold_cards)
        self.buttons_status[0].clicked.connect(new_game)
        self.buttons_status[1].clicked.connect(stop_playing)

        for item in enumerate(self.buttons_game):
            hbox.addWidget(item[1])

        self.turn = QLabel()
        self.pot = QLabel()
        vbox.addWidget(self.turn)
        vbox.addWidget(self.pot)

        for item in enumerate(self.buttons_status):
            vbox.addWidget(item[1])

        self.update()

        self.setMaximumWidth(self.sizeHint().width())
        self.setMaximumHeight(self.sizeHint().height())

    def update(self):
        self.turn.setText("Turn: Player " + str(1))  # status of game
        self.pot.setText("The total pot is: " + str(self.cresources.pot) + "kr")  # status of game


intbox = InteractionBox(CommonResources())
game_view = GameView(CommonResources())

superlayout = QHBoxLayout()
superlayout.addWidget(game_view)
superlayout.addWidget(intbox)

window_view = QGroupBox()
window_view.setLayout(superlayout)
window_view.setMaximumSize(window_view.sizeHint())

window_view.show()

qt_app.exec()