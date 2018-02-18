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


class HandType(enum.IntEnum):
    Straight_flush = 9
    Four_of_a_kind = 8
    Full_house = 7
    Flush = 6
    Straight = 5
    Three_of_a_kind = 4
    Two_pair = 3
    One_pair = 2
    High_card = 1


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

    def drop_card(self, *ind):
        i = 0
        if len(ind[0]) > 1:
            ind = ind[0]
        for item in enumerate(ind):
            del self.cards[item[1]-i]
            i += 1

    def sort_cards(self):
        self.cards.sort(reverse=True)

    def best_poker_hand(self):
        temp = check_straight_flush(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(9), temp[1])
        temp = check_four_kind(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(8), temp[1])
        temp = check_full_house(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(7), temp[1])
        temp = check_flush(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(6), temp[1])
        temp = check_straight(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(5), temp[1])
        temp = check_three_kind(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(4), temp[1])
        temp = check_two_pair(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(3), temp[1])
        temp = check_pair(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(2), temp[1])
        temp = check_high_card(self.cards)
        if temp is not None:
            return PokerHand(temp[0], HandType(1), temp[1])


# ----------------------- Best Poker Hand class ------------------------------------------
class PokerHand:
    def __init__(self, value, kind, cards):
        self.type = kind
        self.value = value
        self.cards = cards

    def __gt__(self, other):
        if self.type > other.type or (self.value > other.value and self.type == other.type):
            return True
        elif self.type < other.type or (self.value < other.value and self.type != other.type):
            return False
        else:
            scards = [self.cards]
            ocards = [other.cards]
            while len(scards) > 0:
                if scards[0] > ocards[0]:
                    return True
                del scards[0]
                del ocards[0]
            return False

    def __lt__(self, other):
        if self.type < other.type or (self.value < other.value and self.type == other.type):
            return True
        elif self.type > other.type or (self.value > other.value and self.type == other.type):
            return False
        else:
            scards = [self.cards]
            ocards = [other.cards]
            while len(scards) > 0:
                if max(scards) < max(ocards):
                    return True
                del scards[0]
                del ocards[0]
            return False

    def __eq__(self, other):
        if self.value != other.value or self.type != other.type:
            return False
        else:
            scards = [self.cards]
            ocards = [other.cards]
            while len(scards) > 0:
                if max(scards) != max(ocards):
                    return False
                del scards[0]
                del ocards[0]
            return True


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
    for c in cards:  # Starting point (high card)
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.give_value().value - k, c.give_suit().value) not in vals:
                found_straight = False
                break
        if found_straight:
            return c.give_value().value, c


def check_four_kind(cards):
    """Done"""
    value_count = Counter()
    four_return = []
    for c in cards:
        value_count[c.give_value().value] += 1
    four_kind = [v[0] for v in value_count.items() if v[1] >= 4]
    if len(four_kind) > 0:
        ind = max(four_kind)
        for item in enumerate(cards):
            if ind == item[1].give_value().value:
                four_return.append(cards[item[0]])
        four_return.sort(reverse=True)
        four_return = four_return[:4]
        return max(four_kind), four_return


def check_full_house(cards):
    """
    Checks for the best full house in a list of cards (may be more than just 5)

    :param cards: A list of playing cards
    :return: None if no full house is found, else a tuple of the values of the triple and pair.
    """
    threes_return = []
    twos_return = []
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
                ind = [max(threes), max(twos)]
                for item in enumerate(cards):
                    if ind[0] == item[1].give_value().value:
                        threes_return.append(cards[item[0]])
                    if ind[1] == item[1].give_value().value:
                        twos_return.append(cards[item[0]])
                twos_return.sort(reverse=True)
                twos_return = twos_return[:2]
                threes_return.sort(reverse=True)
                threes_return = threes_return[:3]
                return [three, two], [threes_return, twos_return]


def check_flush(cards):
    """Done"""
    flush_return = []
    value_count = Counter()
    for c in cards:
        value_count[c.give_suit()] += 1
    flush = [v[0] for v in value_count.items() if v[1] >= 5]
    if len(flush) > 0:
        suit_check = max(flush)
        for item in enumerate(cards):
            if suit_check == item[1].give_suit().value:
                flush_return.append(cards[item[0]])
        flush_return.sort(reverse=True)
        flush_return = flush_return[:5]
        return flush_return[0].give_value().value, flush_return


def check_straight(cards):
    """Done"""
    straight_return = []
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
            for i in range(5):
                for item in enumerate(cards):
                    if c.give_value().value - i == item[1].give_value().value:
                        straight_return.append(cards[item[0]])
                        break
            straight_return.sort(reverse=True)
            return c.give_value().value, straight_return


# Three of a kind
def check_three_kind(cards):
    """Done"""
    value_count = Counter()
    three_kind_return = []
    for c in cards:
        value_count[c.give_value().value] += 1
    # Find the card ranks that have a pair
    three_pair = [v[0] for v in value_count.items() if v[1] >= 2]
    if len(three_pair) > 0:
        for i in range(3):
            for item in enumerate(cards):
                if max(three_pair) == item[1].give_value().value:
                    three_kind_return.append(cards[item[0]])
                    break
        return max(three_kind_return).give_value().value, three_kind_return


# Two pair
def check_two_pair(cards):
    """Done"""
    pair1_return = []
    pair2_return = []
    value_count = Counter()
    for c in cards:
        value_count[c.give_value().value] += 1
    # Find the card ranks that have at least three of a kind
    pair1 = [v[0] for v in value_count.items() if v[1] >= 2]
    pair1.sort(reverse=True)
    # Find the card ranks that have at least a pair
    pair2 = [v[0] for v in value_count.items() if v[1] >= 2]
    pair2.sort(reverse=True)
    # Threes are dominant in full house, lets check that value first:
    for p1 in pair1:
        for p2 in pair2:
            if p2 != p1:
                for item in enumerate(cards):
                    if p1 == item[1].give_value().value:
                        pair1_return.append(cards[item[0]])
                    if p2 == item[1].give_value().value:
                        pair2_return.append(cards[item[0]])
                pair2_return.sort(reverse=True)
                pair2_return = pair2_return[:2]
                pair1_return.sort(reverse=True)
                pair1_return = pair1_return[:2]
                return [p1, p2], [pair1_return, pair2_return]


# One pair
def check_pair(cards):
    """Done"""
    value_count = Counter()
    pair_return = []
    for c in cards:
        value_count[c.give_value().value] += 1
    # Find the card ranks that have a pair
    twos = [v[0] for v in value_count.items() if v[1] >= 2]
    if len(twos) > 0:
        for item in enumerate(cards):
            if max(twos) == item[1].give_value().value:
                pair_return.append(cards[item[0]])
        pair_return.sort(reverse=True)
        pair_return = pair_return[:2]
        return max(twos), pair_return


# High card
def check_high_card(cards):
    """Done"""
    values = []
    for c in cards:
        values.append((c.give_value().value, c.give_suit().value))
    if len(values) > 0:
        cards.sort(reverse=True)
        high_card_output = cards[:5]
        return max(values[0]), high_card_output
