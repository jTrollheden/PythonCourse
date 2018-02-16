import enum
import random


# ----------------------- Suit & rank Classes ------------------------------------------
class Suit(enum.IntEnum):
    Clubs = 0
    Diamonds = 1
    Hearts = 2
    Spades = 3


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
        self.card_value = []

    def __str__(self):
        return self.card[0].name + ' of ' + self.card[1].name

    def give_value(self):
        self.card_value = [self.card[0].value, self.card[1].value]
        return self.card_value

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
        self.hand_value = []

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

    def hand_give_value(self):
        for item in self.cards:
            self.hand_value.append([item.give_value()[0], item.give_value()[1]])
        return self.hand_value


# ----------------------- Deck class ------------------------------------------
class Deck:
    def __init__(self):
        self.deck_cards = []

    def __str__(self):
        output = ''
        for item in enumerate(self.deck_cards):
            output = output + str(item[1]) + ', '
        return output[:-2]

    def create_deck(self):
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        suites = [0, 1, 2, 3]
        for i in suites:
            self.deck_cards.append(AceCard(Suit(i)))
            self.deck_cards.append(KingCard(Suit(i)))
            self.deck_cards.append(QueenCard(Suit(i)))
            self.deck_cards.append(JackCard(Suit(i)))
            for k in values:
                self.deck_cards.append(NumberedCard(Rank(k), Suit(i)))

    def sort_deck(self):
        temp_deck = []
        l = len(self.deck_cards)
        for i in range(l):
            rng = random.randint(0, l-i)-1
            temp_deck.append(self.deck_cards[rng])
            del self.deck_cards[rng]
        self.deck_cards = temp_deck
