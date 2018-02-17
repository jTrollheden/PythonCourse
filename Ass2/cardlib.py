import enum  # Easier data processing (Suit and Rank)
import random  # Rng lib
import abc  # Abstract functions
from collections import Counter # Counter is convenient for counting objects (a specialized dictionary)


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
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


# ----------------------- PlayingCard class ------------------------------------------
class PlayingCard(metaclass=abc.ABCMeta):
    def __init__(self, value, suit):
        self.card = [value, suit]

    def __str__(self):
        return self.give_value().name + ' of ' + self.give_suit().name

    def __gt__(self, other):
        if self.give_value().value > other.give_value().value:
            return True
        elif self.give_value().value == other.give_value().value and self.give_suit().value > other.give_suit().value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.give_value().value < other.give_value().value:
            return True
        elif self.give_value().value == other.give_value().value and self.give_suit().value < other.give_suit().value:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.give_value().value == other.give_value().value

    @abc.abstractmethod
    def give_value(self):
        raise NotImplementedError("Missing give_value implementation")

    @abc.abstractmethod
    def give_suit(self):
        raise NotImplementedError("Missing give_suit implementation")


class NumberedCard(PlayingCard):  # The NumberedCard IS a PlayingCard
    def __init__(self, value, suit):
        super().__init__(value, suit)

    def give_value(self):
        self.card_value = self.card[0]
        return self.card_value

    def give_suit(self):
        self.card_suit = self.card[1]
        return self.card_suit


class JackCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(11), suit)

    def give_value(self):
        self.card_value = self.card[0]
        return self.card_value

    def give_suit(self):
        self.card_suit = self.card[1]
        return self.card_suit


class QueenCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(12), suit)

    def give_value(self):
        self.card_value = self.card[0]
        return self.card_value

    def give_suit(self):
        self.card_suit = self.card[1]
        return self.card_suit


class KingCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(13), suit)

    def give_value(self):
        self.card_value = self.card[0]
        return self.card_value

    def give_suit(self):
        self.card_suit = self.card[1]
        return self.card_suit


class AceCard(PlayingCard):
    def __init__(self, suit):
        super().__init__(Rank(14), suit)

    def give_value(self):
        self.card_value = self.card[0]
        return self.card_value

    def give_suit(self):
        self.card_suit = self.card[1]
        return self.card_suit


# ----------------------- Hand class ------------------------------------------
class Hand:
    def __init__(self):
        self.cards = []    # creates a new empty list for each hand
        self.card_values = []

    def __str__(self):
        output = ''
        for item in enumerate(self.cards):
            output = output + str(item[1]) + ', '
        return output[:-2]

    def add_card(self, card):
        self.cards.append(card)

    def drop_card(self, ind):
        for item in enumerate(ind):
            del self.cards[item[1]]

    def sort_cards(self):
        self.cards.sort()


# ----------------------- Best Poker Hand class ------------------------------------------
class PokerHand:
    def __init__(self, kind, cards):
        self.hand_type = kind
        self.highest_value = cards

    # def __gt__(self, other):
    #
    # def __lt__(self, other):
    #
    # def __eq__(self, other):


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
        suites = [3, 2, 1, 0]
        for i in suites:
            self.deck_cards.append(AceCard(Suit(i)))
            self.deck_cards.append(KingCard(Suit(i)))
            self.deck_cards.append(QueenCard(Suit(i)))
            self.deck_cards.append(JackCard(Suit(i)))
            for k in values:
                self.deck_cards.append(NumberedCard(Rank(k), Suit(i)))

    def shuffle_deck(self):
        random.shuffle(self.deck_cards)

    def draw(self):
        drawn_card = self.deck_cards[0]
        self.deck_cards.__delitem__(0)
        return drawn_card


# ---------------- Value Checking funcs ----------------------
def check_straight_flush(cards):
    """
    Checks for the best straight flush in a list of cards (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if no straight flush is found, else the value of the top card.
    """
    vals = [(c.give_value().value, c.give_suit().value) for c in cards] \
        + [(1, c.give_suit().value) for c in cards if c.give_value().value == 14]  # Add the aces!
    for c in reversed(cards):  # Starting point (high card)
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.give_value().value - k, c.give_suit().value) not in vals:
                found_straight = False
                break
        if found_straight:
            return c.give_value()


def check_four_kind(cards):
    """Done"""
    value_count = Counter()
    for c in cards:
        value_count[c.give_value().value] += 1
    four_kind = [v[0] for v in value_count.items() if v[1] >= 4]
    if len(four_kind) > 0:
        return Rank(max(four_kind))


def check_full_house(cards):
    """
    Checks for the best full house in a list of cards (may be more than just 5)

    :param cards: A list of playing cards
    :return: None if no full house is found, else a tuple of the values of the triple and pair.
    """
    value_count = Counter()
    for c in cards:
        value_count[c.give_value().value] += 1
    # Find the card ranks that have at least three of a kind
    threes = [v[0] for v in value_count.items() if v[1] >= 3]
    threes.sort(reverse=True)
    # Find the card ranks that have at least a pair
    twos = [v[0] for v in value_count.items() if v[1] >= 2]
    twos.sort(reverse=True)
    # Threes are dominant in full house, lets check that value first:
    for three in threes:
        for two in twos:
            if two != three:
                return Rank(three), Rank(two)


def check_flush(cards):
    """Done"""
    value_count = Counter()
    for c in cards:
        value_count[c.give_suit()] += 1
    flush = [v[0] for v in value_count.items() if v[1] >= 5]
    if len(flush) > 0:
        return max(flush)


def check_straight(cards):
    """Done"""
    vals = [c.give_value().value for c in cards] \
           + [1 for c in cards if c.give_value().value == 14]  # Add the aces!
    for c in reversed(cards):  # Starting point (high card)
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.give_value().value - k) not in vals:
                found_straight = False
                break
        if found_straight:
            return c.give_value()

# Three of a kind

# Two pair

# One pair

# High card
