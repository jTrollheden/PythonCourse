from PyQt5.QtCore import *
import cardlib as cl


class GameState(QObject):
    data_changed = pyqtSignal()

    def __init__(self, player1, player2):
        QObject.__init__(self)
        # TODO: dialog ruta där man matar in spelare, samt en loop
        # TODO: där spelarna skapas.
        self.players = [player1, player2]
        self.pot = 0
        self.running = False
        self.bet = False
        self.player_turn = 0
        self.old_bet = 0

    def update_pot(self, inc):
        self.pot = self.pot + inc
        self.old_bet = inc
        self.data_changed.emit()

    def change_turn(self, players):
        players.active = not players.active
        if self.player_turn == 0:
            self.player_turn = 1
        elif self.player_turn == 1:
            self.player_turn = 2
        else:
            self.player_turn = 1
        return

    def start_new_round(self):
        if self.running:
            self.game_message.emit("Can't start game. Game already running")
            # TODO: Fixa till dialog, "vill du starta om? Isf starta om hela spelet."
        self.running = True
        self.player_turn = 0
        self.pot = 0
        self.players[self.player_turn].set_active(True)
        self.data_changed.emit()

    def won(self):
        self.wins += 1
        self.data_changed.emit()
        # TODO: Fixa så att vinnaren av varje giv printas ut samt en ny giv delas ut


class Deck(cl.Deck, GameState):
    def __init__(self):
        cl.Deck.__init__(self)
        QObject.__init__(self)


class Player(cl.Hand, GameState):
    data_changed = pyqtSignal()

    def __init__(self, usrname, startcred):
        cl.Hand.__init__(self)
        QObject.__init__(self)
        self.credits = startcred
        self.usrname = usrname
        self.active = False

    def add_card(self, card):
        super().add_card(card)
        self.data_changed.emit()

    def flip(self):
        # Flips over the cards (to hide them)
        self.flipped_cards = not self.flipped_cards
        self.data_changed.emit()

    def marked(self, i):
        return self.marked_cards[i]

    def bet(self, cred, game_state):
        if self.credits >= cred:
            self.credits = self.credits - cred
            game_state.old_bet = cred
            game_state.bet = True
            self.data_changed.emit()
            return True
        else:
            return False

    def raise_pot(self, cred, game_state):
        if self.credits > (cred + game_state.old_bet):
            self.credits = self.credits - cred - game_state.old_bet
            self.data_changed.emit()
            return True
        else:
            return False

        # Dialog box

    def call_check(self):
        1+1

    def fold(self):
        1+1


class CenterCards(cl.Hand, GameState):
    data_changed = pyqtSignal()

    def __init__(self):
        cl.Hand.__init__(self)
        QObject.__init__(self)

    def flip(self):
        # Flips over the cards (to hide them)
        self.flipped_cards = not self.flipped_cards
        self.data_changed.emit()

    def marked(self, i):
        return self.marked_cards[i]

    def add_card(self, card):
        super().add_card(card)
        self.data_changed.emit()


def execute():
    deck = Deck()
    deck.create_deck()
    deck.shuffle_deck()

    player1 = Player("sofia", 3000)
    player2 = Player("joel", 2000)

    for i in range(2):
        player1.add_card(deck.draw())
        player2.add_card(deck.draw())

    centercards = CenterCards()

    for i in range(5):
        centercards.add_card(deck.draw())

    game_state = GameState(player1, player2)
    return game_state, centercards, player1, player2


[game_state, centercards, player1, player2] = execute()


# TODO: FIXA SÅ ATT PENGARNA UPPDATERAS VID BETS