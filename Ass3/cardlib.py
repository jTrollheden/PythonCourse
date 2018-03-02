import enum  # Easier data processing (Suit and Rank)
import random  # Rng lib
import abc  # Abstract functions
from collections import Counter  # Counter is convenient for counting objects (a specialized dictionary)


# ----------------------- Suit & rank Classes ------------------------------------------
class Suit(enum.IntEnum):
    """
        Is used as input when creating the different cards.

        :param Int: Integer corresponding to the suits below.
        :return Enum: Containing Suit and value of suit
        """
    Clubs = 0
    Diamonds = 1
    Hearts = 2
    Spades = 3


class Rank(enum.IntEnum):
    """
        Is used as input when creating the different cards.

        :param Int: Integer corresponding to the ranks below.
        :return Enum: Containing Rank and value of Rank
        """
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
    """
        Creates the values of the possible hands in a deck of cards used in best_poker_hand method.

        :param Int: Integer corresponding to the values for the hands below.
        :return Enum: Containing type of poker hand and it's value.
        """
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
    """
        The class for the cards. Used to create and compare the cards in the library.
        """
    def __init__(self, value, suit):
        """
                Creates the ranks and values of the cards in a deck of cards.

                :param self: Calls the object(card) and assigns the value to the object
                :param value: An enum from the class Rank.
                :param suit: An enum from the class Suit.
                :return: A playing card with information about value and suit on their corresponding position.
                """
        self.card = [value, suit]  # Creates the values of the playing card

    def __str__(self):
        """
                Formats the print function for the cards do that it is readable to the user.

                :param self: Card you want to print
                :return: A string representing the playing card.
                """
        return self.give_value().name + ' of ' + self.give_suit().name
        # Returns a string that's readable for the user about what card it is

    def __gt__(self, other):
        """
                Compares the self card rank and suit with the other card and returns if self is greater than other.

                :param self: Card you want to compare.
                :param playing card: Card to compare with.
                :return: A Boolean value for the operator > which determines if self card is bigger than other card.
                """
        if self.give_value().value > other.give_value().value:
            return True
        elif self.give_value().value == other.give_value().value and self.give_suit().value > other.give_suit().value:
            return True
        else:
            return False

    def __lt__(self, other):
        """
                Compares the self card rank and suit with the other card and returns if self is lesser than other.

                :param self: Card you want to compare.
                :param playing card: Card to compare with.
                :return: A Boolean value for the operator < which determines if self card is lesser than other card.
                """
        if self.give_value().value < other.give_value().value:
            return True
        elif self.give_value().value == other.give_value().value and self.give_suit().value < other.give_suit().value:
            return True
        else:
            return False

    def __eq__(self, other):
        """
                Compares the self card rank and suit with the other card and returns if self is equal to the other.

                :param self: Card you want to compare.
                :param playing card: Card to compare with.
                :return: A Boolean value for the operator == which determines if self card is equal to the other card.
                """
        return self.give_value().value == other.give_value().value

    @abc.abstractmethod
    def give_value(self):
        """
                Abstract function from the subclasses of playing cards that gives the value of a card.

                :param self: Card you want the value of.
                :raise: Raises error if implementation is missing in sub-classes.
                """
        raise NotImplementedError("Missing give_value implementation")

    @abc.abstractmethod
    def give_suit(self):
        """
                 Abstract function from the subclasses of playing cards that gives the Suit of a card.

                 :param self: Card you want the Suit of.
                 :raise: Raises error if implementation is missing in sub-classes.
                """
        raise NotImplementedError("Missing give_suit implementation")


class NumberedCard(PlayingCard):
    """
        Subclass to playing cards for the numbered cards (2 to 10).

        """
    def __init__(self, value, suit):
        """
                Creates the ranks and values of the numbered cards. Super calls for the function in the mother class
                PlayingCard.

                :param self: Calls the object(card) and assigns the value to the object
                :param value: An enum from the class Rank.
                :param suit: An enum from the class Suit.
                """
        super().__init__(value, suit)  # Calls for the __init__ in the PlayingCard class.

    def give_value(self):
        """
                Checks the value of the playing cards and returns it.

                :param self: A card of the subclass NumberedCard.
                :return Int: The value of the card.
                """
        self.card_value = self.card[0]
        return self.card_value  # Returns the Rank enum of the card

    def give_suit(self):
        """
                Checks the suit of the playing cards and returns it.

                :param self: A card of the subclass NumberedCard.
                :return Int: The suit of the card.
                        """
        self.card_suit = self.card[1]
        return self.card_suit  # Returns the Suit enum of the card


class JackCard(PlayingCard):
    """
            Subclass to playing cards for the Jacks.

            """
    def __init__(self, suit):
        """
                Creates the ranks and values of the Jack card. Super calls for the function in the mother class
                PlayingCard.

                :param self: Calls the object(card) and assigns the value to the object
                :param suit: An enum from the class Suit.
                        """
        super().__init__(Rank(11), suit)

    def give_value(self):
        """
                Checks the value of the Jack card.

                :param self: A card of the subclass JackCard.
                :return: The rank of the card.
                """
        self.card_value = self.card[0]
        return self.card_value  # Returns the Rank enum of the card

    def give_suit(self):
        """
                Checks the suit of the Jack card.

                :param self: A card of the subclass JackCard.
                :return: The suit of the card.
                """
        self.card_suit = self.card[1]
        return self.card_suit  # Returns the Suit enum of the card


class QueenCard(PlayingCard):
    """
                Subclass to playing cards for the Queens.

                """
    def __init__(self, suit):
        """
                Creates the ranks and values of the Queen card. Super calls for the function in the mother class
                PlayingCard.

                :param self: Calls the object(card) and assigns the value to the object
                :param suit: An enum from the class Suit.
                                """
        super().__init__(Rank(12), suit)

    def give_value(self):
        """
                Checks the value of the Queen card.

                :param self: A card of the subclass QueenCard.
                :return: The rank of the card.
                        """
        self.card_value = self.card[0]
        return self.card_value  # Returns the Rank enum of the card

    def give_suit(self):
        """
                Checks the suit of the Queen card.

                :param self: A card of the subclass QueenCard.
                :return: The suit of the card.
                        """
        self.card_suit = self.card[1]
        return self.card_suit  # Returns the Suit enum of the card


class KingCard(PlayingCard):
    """
                Subclass to playing cards for the Kings.

                """
    def __init__(self, suit):
        """
                Creates the ranks and values of the King card. Super calls for the function in the mother class
                            PlayingCard.

                :param self: Calls the object(card) and assigns the value to the object
                :param suit: An enum from the class Suit.
                                            """
        super().__init__(Rank(13), suit)

    def give_value(self):
        """
                Checks the value of the King card.

                :param self: A card of the subclass KingCard.
                :return: The rank of the card.
                                """
        self.card_value = self.card[0]
        return self.card_value  # Returns the Rank enum of the card

    def give_suit(self):
        """
                Checks the suit of the King card.

                :param self: A card of the subclass KingCard.
                :return: The rank of the card.
                                """
        self.card_suit = self.card[1]
        return self.card_suit  # Returns the Suit enum of the card


class AceCard(PlayingCard):
    """
                Subclass to playing cards for the Aces.

                """
    def __init__(self, suit):
        """
                Creates the ranks and values of the Ace card. Super calls for the function in the mother class
                                PlayingCard.

                :param self: Calls the object(card) and assigns the value to the object
                :param suit: An enum from the class Suit.
                                                """
        super().__init__(Rank(14), suit)

    def give_value(self):
        """
                Checks the value of the Ace card.

                :param self: A card of the subclass AceCard.
                :return: The rank of the card.
                                """
        self.card_value = self.card[0]
        return self.card_value  # Returns the Rank enum of the card

    def give_suit(self):
        """
                Checks the suit of the Ace card.

                :param self: A card of the subclass AceCard.
                :return: The rank of the card.
                                """
        self.card_suit = self.card[1]
        return self.card_suit  # Returns the Suit enum of the card


# ----------------------- Hand class ------------------------------------------
class Hand:
    """
        A class that contains all functions needed for the hand and also creates the object that we use as a hand.

        """
    def __init__(self):
        """
                Creates an object of the Hand class.

                """
        self.cards = []    # creates a new empty list for each hand

    def __str__(self):
        """
                Prints the Hand.

                :param self: A hand object of the class Hand.
                :return: A string representing what cards there is in the hand.
                """
        output = ''
        for item in enumerate(self.cards):  # looping over the cards in the hand and then converting them to string
            output = output + str(item[1]) + ', '  # using the str function from the PlayingCard class.
        return output[:-2]

    def add_card(self, card):
        """
                Adds a card to the Hand

                :param self: A hand object of the class Hand.
                :param card: A card from the class PlayingCard.
                """
        self.cards.append(card)  # Adds a card to the self.cards list

    def drop_cards(self, ind):
        """
                Removes a card from the Hand.

                :param self: A hand object of the class Hand.
                :param ind: The index of the card you want to remove from the hand.
                """
        if isinstance(ind, int):
            ind = [ind]
        i = 0
        for item in ind:
            del self.cards[item - i]  # Removes a card by index to the self.cards list
            i += 1                # i is used to keep the index from the imput, since the index changes each iteration

    def sort_cards(self):
        """
                Checks which cards are in the Hand and sorts them from low to high.

                :param self: A hand object of the class Hand.
                """
        self.cards.sort(reverse=True)  # Sorts the cards in descending order

    def best_poker_hand(self):
        """
                Checks which pokerhands below that are present in the hand.

                :param self: A hand object of the class Hand.
                :return: Top pokerhand present in the Hand, if none of the pokerhands below exist in the Hand None is returned.
                """
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
        # Goes through each check of the different types in descending order and gives the best poker_hand available

# ----------------------- Best Poker Hand class ------------------------------------------
class PokerHand:
    """
        A class with the necessary functions for a pokerhand.
        """
    def __init__(self, value, kind, cards):
        """
                Creates the pokerhand.
                :param value: The value of the pokerhand.
                :param kind: The type of the pokerhand.
                :param cards: The cards in the pokerhand.
                """
        self.type = kind
        self.value = value
        self.cards = cards
        # Iniates the PokerHand object and assigns to it what kind of hand it is (pair, straight etc), the value of the
        # best card and also all the cards that are needed in the combination.

    def __gt__(self, other):
        """
                Checks if the pokerhand is greater than the other pokerhand.

                :param self: A pokerhand.
                :param other: A pokerhand.
                :return: A Boolean determining if self > other.
                """
        # First it's checking the straight forward values of the hand.
        if self.type > other.type or (self.value > other.value and self.type == other.type):
            return True
        elif self.type < other.type or (self.value < other.value and self.type != other.type):
            return False
        # Here it goes a bit deeper since everything is equal. It checks every card in each pokerhand until it finds the
        # first difference and then gives a bool answer.
        else:
            scards = [self.cards]
            ocards = [other.cards]
            while len(scards) > 0:
                if max(scards) > max(ocards):
                    return True
                del scards[0]
                del ocards[0]
            return False

    def __lt__(self, other):
        """
                Checks if the pokerhand is lesser than the other pokerhand.

                :param self: A pokerhand.
                :param other: A pokerhand.
                :return: A Boolean determining if self < other.
                        """
        # First it's checking the straight forward values of the hand.
        if self.type < other.type or (self.value < other.value and self.type == other.type):
            return True
        elif self.type > other.type or (self.value > other.value and self.type == other.type):
            return False
        # Here it goes a bit deeper since everything is equal. It checks every card in each pokerhand until it finds the
        # first difference and then gives a bool answer.
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
        """
                Checks if the pokerhand is equal to the other pokerhand.

                :param self: A pokerhand.
                :param other: A pokerhand.
                :return: A Boolean determining if self == other.
                        """
        # First it's checking the straight forward values of the hand.
        if self.value != other.value or self.type != other.type:
            return False
        # Here it goes a bit deeper since everything is equal. It checks every card in each pokerhand until it finds the
        # first difference and then gives a bool answer.
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
    """
    A class with the necessary functions for the deck.

    """
    def __init__(self):
        """
                Creates the deck upon calling upon the Class Deck.
                """
        self.cards = []  # Creates the deck object adds an empty list that you can add cards to.

    def __str__(self):
        """
                Prints the cards of the deck.

                :param self: A deck you want to print.
                :return: A string that represents the deck.
        """
        output = ''
        for item in enumerate(self.cards):
            output = output + str(item[1]) + ', '
        return output[:-2]  # Formating the string output of a deck so it's readable to the user

    def create_deck(self):
        """
                Creates all the cards in the deck. Adds the 52 cards that are in a deck to the specified deck.

                :param self: The deck you want to add the cards to.
                """
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        suites = [3, 2, 1, 0]
        # Creates all the 13 cards for each suit
        for i in suites:
            self.cards.append(AceCard(Suit(i)))
            self.cards.append(KingCard(Suit(i)))
            self.cards.append(QueenCard(Suit(i)))
            self.cards.append(JackCard(Suit(i)))
            for k in values:
                self.cards.append(NumberedCard(Rank(k), Suit(i)))

    def shuffle_deck(self):
        """
                Shuffles the cards in the deck.

                :param self: The deck you want to shuffle.
        """
        random.shuffle(self.cards)  # Shuffles the deck

    def draw(self):
        """
                Draws the top card from the deck.

                :param self: The deck you want to draw a card from.
                :return card: The card drawn.
                """
        drawn_card = self.cards[0]
        self.cards.__delitem__(0)
        return drawn_card
        # removes a card and returns the drawn card so that the function add_card for the hand can use it while at the
        # same time be able to be discarded straight from the deck.


# ---------------- Value Checking funcs ----------------------
def check_straight_flush(cards):
    """
    Checks for the best straight flush in a list of cards (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if no straight flush is found, else the value of the top card as well as the card object.
    """
    vals = [(c.give_value().value, c.give_suit().value) for c in cards] \
        + [(1, c.give_suit().value) for c in cards if c.give_value().value == 14]  # Add the aces!
    for c in cards:  # Starting point
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.give_value().value - k, c.give_suit().value) not in vals:
                found_straight = False
                break
        if found_straight:
            return c.give_value().value, c


def check_four_kind(cards):
    """
    Checks if there are four cards of the same value in a list of cards (may be more than just 5) and also picks out the
    four cards of the same kind with the highest value.

    :param cards: A list of playing cards.
    :return: None if four of a kind are not found, else the value of the four cards and the card objects.
    """
    value_count = Counter()
    four_return = []
    for c in cards:
        value_count[c.give_value().value] += 1
    four_kind = [v[0] for v in value_count.items() if v[1] >= 4]
    # At this point all the cards that have four of a kind has been identified.
    if len(four_kind) > 0:
        ind = max(four_kind)
        for item in enumerate(cards):
            if ind == item[1].give_value().value:
                four_return.append(cards[item[0]])  # here the cards of the best four kind is added to the return.
        four_return.sort(reverse=True)
        four_return = four_return[:4]
        # If larger decks would be used and there would be more than 4 of the card that makes up the best 4 kind
        return max(four_kind), four_return


def check_full_house(cards):
    """
    Checks for the best full house in a list of cards (may be more than just 5)

    :param cards: A list of playing cards
    :return: None if no full house is found, else a list of the values of the triple and pair as well as the card objects.
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
                        threes_return.append(cards[item[0]])    # Add the correct cards to the return pile
                    if ind[1] == item[1].give_value().value:
                        twos_return.append(cards[item[0]])
                twos_return.sort(reverse=True)
                twos_return = twos_return[:2]
                threes_return.sort(reverse=True)
                threes_return = threes_return[:3]
                # If larger decks would be used and there would be more than 4 of the card that makes up the best 4 kind
                # then you just want the 3 first and 2 first cards respectively
                return [three, two], [threes_return, twos_return]


def check_flush(cards):
    """
    Checks for the best flush in a list of cards (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if no flush is found, else the suit of the flush and the card objects.
    """
    flush_return = []
    value_count = Counter()
    for c in cards:
        value_count[c.give_suit()] += 1
    flush = [v[0] for v in value_count.items() if v[1] >= 5]
    # Check if we have the value - k in the set of cards:
    # By here we have the best flush, we want the specific cards though.
    if len(flush) > 0:
        suit_check = max(flush)
        for item in enumerate(cards):
            if suit_check == item[1].give_suit().value:
                flush_return.append(cards[item[0]])  # Adds the best cards to the return pile
        flush_return.sort(reverse=True)
        flush_return = flush_return[:5]
        return flush_return[0].give_value().value, flush_return


def check_straight(cards):
    """
    Checks for the best straight in a list of cards (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if no straight is found, else the value of the top card in the straight and the card objects.
    """
    straight_return = []
    vals = [c.give_value().value for c in cards] \
           + [1 for c in cards if c.give_value().value == 14]  # Add the aces!
    cards.sort(reverse=True)
    for c in cards:  # Starting point (high card)
        # Check if we have the value - k in the set of cards:
        found_straight = True
        for k in range(1, 5):
            if (c.give_value().value - k) not in vals:
                found_straight = False
                break
        if found_straight:
            for i in range(5):  # i is used to get the correct card so that the straight is correct.
                for item in enumerate(cards):
                    if c.give_value().value - i == item[1].give_value().value:
                        straight_return.append(cards[item[0]])  # Adds the best cards to the return pile
                        break
            straight_return.sort(reverse=True)
            return c.give_value().value, straight_return


# Three of a kind
def check_three_kind(cards):
    """
    Checks for the best three of cards of the same kind (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if a three kind is not found, else the value of the top card and the card objects.
    """
    value_count = Counter()
    three_kind_return = []
    for c in cards:
        value_count[c.give_value().value] += 1
    # Find the card ranks that have a three kind
    three_pair = [v[0] for v in value_count.items() if v[1] >= 3]
    # By this point we have all the info we need to get the max three_kind value, but we want the cards as well.
    if len(three_pair) > 0:
        for i in range(3):
            for item in enumerate(cards):
                if max(three_pair) == item[1].give_value().value:
                    three_kind_return.append(cards[item[0]])  # Add the best cards to the return list.
                    break
        return max(three_kind_return).give_value().value, three_kind_return


# Two pair
def check_two_pair(cards):
    """
    Checks for the best two pairs (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if a two pair is not found, else the value of the top cards of the pairs and the card objects.
    """
    pair1_return = []
    pair2_return = []
    value_count = Counter()
    for c in cards:
        value_count[c.give_value().value] += 1
    # Find the card ranks that have at least two of a kind
    pair = [v[0] for v in value_count.items() if v[1] >= 2]
    pair.sort(reverse=True)
    for p1 in pair:
        for p2 in pair:
            if p2 != p1:
                for item in enumerate(cards):
                    if p1 == item[1].give_value().value:
                        pair1_return.append(cards[item[0]])  # Add the best cards to the return lists.
                    if p2 == item[1].give_value().value:
                        pair2_return.append(cards[item[0]])
                pair2_return.sort(reverse=True)
                pair2_return = pair2_return[:2]
                pair1_return.sort(reverse=True)
                pair1_return = pair1_return[:2]
                return [p1, p2], [pair1_return, pair2_return]


# One pair
def check_pair(cards):
    """
    Checks for the best pair (may be more than just 5)

    :param cards: A list of playing cards.
    :return: None if a two pair is not found, else the value of the top cards of the pair and the card objects.
    """
    value_count = Counter()
    pair_return = []
    for c in cards:
        value_count[c.give_value().value] += 1
    # Find the card ranks that have a pair
    twos = [v[0] for v in value_count.items() if v[1] >= 2]
    if len(twos) > 0:
        for item in enumerate(cards):
            if max(twos) == item[1].give_value().value:
                pair_return.append(cards[item[0]])  # Add the best cards to the return list.
        pair_return.sort(reverse=True)
        pair_return = pair_return[:2]
        return max(twos), pair_return


# High card
def check_high_card(cards):
    """
    Checks for the highest card in the hand (may be more than just 5)

    :param cards: A list of playing cards.
    :return: The value of the top card of the hand.
    """
    values = []
    for c in cards:
        values.append((c.give_value().value, c.give_suit().value))
    if len(values) > 0:
        cards.sort(reverse=True)
        high_card_output = cards[:5]
        return max(values)[0], high_card_output  # Returning the highest value card and 4 more that can be checked.

