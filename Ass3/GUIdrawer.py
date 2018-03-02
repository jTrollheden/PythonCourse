from PyQt5.QtGui import *
from PyQt5.QtSvg import *
from PyQt5.QtWidgets import *
import logicTexas as tx
import sys


qt_app = QApplication(sys.argv)
qt_app = QApplication.instance()


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
        # call the "change_cards" method instead.

        # Add the cards the first time around to represent the initial state.
        self.change_cards()

    def change_cards(self):  # Fix so that the
        # Add the cards from scratch:
        self.scene.clear()  # Removes old cards
        for i, card in enumerate(self.active_instance.cards):  # Player/center cards goes here
            graphics_key = (card.give_value().value, card.give_suit().value)
            renderer = self.all_cards[graphics_key] #self.back_card if self.model.flipped(i) else
            # TODO: När ska korten vara flippade?
            c = CardSvgItem(renderer, i)

            shadow = QGraphicsDropShadowEffect(c)
            shadow.setBlurRadius(10.)
            shadow.setOffset(5, 5)
            shadow.setColor(QColor(0, 0, 0, 180))  # Semi-transparent black!
            c.setGraphicsEffect(shadow)

            # Position cards
            c.setPos(c.position * self.card_spacing, 0)
            # Sets the opacity of cards if they are marked.
            self.scene.addItem(c)

        self.update_view()

    def update_view(self):
        scale = (self.viewport().height() - 2 * self.padding) / 313
        self.resetTransform()
        self.scale(scale, scale)
        # Put the scene bounding box
        self.setSceneRect(-self.padding // scale, -self.padding // scale,
                          self.viewport().width() // scale, self.viewport().height() // scale)

    def resizeEvent(self, painter):
        # If the widget is resize, we gotta adjust the card sizes.
        # QGraphicsView automatically re-paints everything when we modify the scene.
        self.update_view()
        super().resizeEvent(painter)


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

        player.data_changed.connect(self.update)

        self.update()

    def update(self):
        self.who_money.setText("Player: " + str(self.player.usrname) + " has " + str(self.player.credits) + "kr")

class GameView(QGroupBox):
    def __init__(self, center_cards, player1, player2):
        super().__init__()
        self.center_cards = center_cards

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.cards = CardView(self.center_cards)


        player_view = PlayerView(player1)
        player_view2 = PlayerView(player2)

        layout.addWidget(player_view)
        layout.addWidget(self.cards)
        layout.addWidget(player_view2)

        player1.data_changed.connect(self.update)
        player2.data_changed.connect(self.update)

        self.setStyleSheet("""
            color: white; 
            background-image: url(/Users/joeltrollheden/Documents/GitHub/PythonCourse/Ass3/cards/table.png);
        """);


class InteractionBox(QGroupBox):
    def __init__(self, game_state):
        super().__init__()

        # Layout
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.game_state = game_state

        # Buttons
        bet_raiseb = QPushButton("Bet/Raise")  # Ändra så att texten beror på state
        call_checkb = QPushButton("Call/Check")  # Ändra så att texten beror på state
        foldb = QPushButton("Fold")
        new_gameb = QPushButton("New Game")
        stop_playingb = QPushButton("Exit")
        self.buttons_game = [bet_raiseb, call_checkb, foldb]
        self.buttons_status = [new_gameb, stop_playingb]

        game_state.data_changed.connect(self.update)

        def bet_raise():
            if game_state.bet:
                cred = QInputDialog.getInt(self, "Raise", ("How much do you want to raise the old bet? The old bet was:"
                                                           + str(game_state.old_bet)))
                if cred[1] and cred[0] > 0:
                    game_state.players[1].raise_pot(cred[0], game_state)
                    if game_state.poor:
                        QMessageBox.question(self, "", "You do not have enough credits",
                                             QMessageBox.Ok)
                else:
                    pass
            else:
                cred = QInputDialog.getInt(self, "Bet", "How much do you want to bet?")
                if cred and cred[0] > 0:
                    game_state.players[game_state.player_turn].bet(cred[0], game_state)
                    if game_state.poor:
                        QMessageBox.question(self, "", "You do not have enough credits",
                                             QMessageBox.Ok)
                else:
                    pass

        def check_call():
            1+1
            # Call the previous bet/raise or just check

        def fold_cards():
            1+1
            # Fold

        def new_game():
            if not game_state.running:
                choice = QMessageBox.question(self, "", "Do you want to start a new game?", QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    game_state.start_new_round()
                else:
                    pass
            else:
                choice = QMessageBox.question(self, "", "Do you want to start a new game and discard your current one?",
                                              QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    game_state.start_new_round()
                else:
                    pass
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
        if self.game_state.player_turn == 0:
            self.turn.setText("Game has not started")  # status of game
        else:
            self.turn.setText("Turn: Player " + str(self.game_state.player_turn))  # status of game
        self.pot.setText("The total pot is: " + str(self.game_state.pot) + "kr")  # status of game
        if not self.game_state.running:
            for b in self.buttons_game[:3]:
                b.setEnabled(False)
        if self.game_state.running:
            for b in self.buttons_game[:3]:
                b.setEnabled(True)


def execute(game_state, centercards, player1, player2):
    intbox = InteractionBox(game_state)
    game_view = GameView(centercards, player1, player2)

    superlayout = QHBoxLayout()
    superlayout.addWidget(game_view)
    superlayout.addWidget(intbox)

    window_view = QGroupBox()
    window_view.setLayout(superlayout)
    window_view.setMaximumSize(window_view.sizeHint())

    window_view.show()

    qt_app.exec()
