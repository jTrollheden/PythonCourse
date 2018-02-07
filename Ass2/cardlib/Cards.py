class PlayingCard:
    def give_value(self):
        # This is one common way to make an abstract method,
        # though there isn't any special language features used here.
        raise NotImplementedError("Missing give_value implementation")


class NumberedCard(PlayingCard):  # The NumberedCard IS a PlayingCard
    def __init__(self, value, suit):
        self.card = [suit, value]

    def give_value(self):  # Overloads the method from Shape
        return self.card


class JackCard(PlayingCard):
    def __init__(self, suit):
        self.card = [suit, 11]

    def give_value(self):
            return self.card


class QueenCard(PlayingCard):
    def __init__(self, suit):
        self.card = [suit, 12]

    def give_value(self):
            return self.card


class KingCard(PlayingCard):
    def __init__(self, suit):
        self.card = (suit, 13)

    def give_value(self):  # Overloads the method from Shape
            return self.card


class AceCard(PlayingCard):
    def __init__(self, suit):
        self.card = [suit, 14]

    def give_value(self):  # Overloads the method from Shape
            return self.card


x = KingCard(0)
y = QueenCard(0)

