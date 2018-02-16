import enum


# ----------------------- Suit & rank Classes ------------------------------------------
class Suit(enum.IntEnum):
    Hearts = 0
    Diamonds = 1
    Spades = 2
    Clubs = 3


class Rank(enum.IntEnum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    J = 11
    Q = 12
    K = 13
    A = 14


# ----------------------- PlayingCard class ------------------------------------------
class PlayingCard:
    def __init__(self, value, suit):
        self.card = [value, suit]

    def __str__(self):
        return self.card[0].name + ' of ' + self.card[1].name

    def give_value(self):
        return self.card

class NumberedCard(PlayingCard):  # The NumberedCard IS a PlayingCard
    def __init__(self, value, suit):
        super().__init__(value, suit)


class JackCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(11), suit)


class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(12), suit)


class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(13), suit)


class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(14), suit)


# ----------------------- Hand class ------------------------------------------
class Hand:
    def __init__(self):
        self.cards = []    # creates a new empty list for each hand

    def __str__(self):
        output = ''
        for item in enumerate(self.cards):
            output = output + str(item[1]) + ', '
        return output[:-2]

    def add_card(self, card):
        self.cards.append(card)

    def drop_card(self, ind):
        self.cards.__delitem__(ind)

    def sort_cards(self):
        self.cards.sort()

    def hand_give_value


# ----------------------- Deck class ------------------------------------------
class Deck:
    def __init__(self):
        self.deck_cards = []

    def create_deck(self):
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        suites = [0, 1, 2, 3]
        #for
        ##self.deck =