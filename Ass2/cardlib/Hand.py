def get_key0(item):
    return item[0]


def get_key1(item):
    return item[1]


class Hand:

    def __init__(self):
        self.cards = []    # creates a new empty list for each dog

    def add_card(self, card):
        self.cards.append(card)

    def drop_card(self, ind):
        self.cards.__delitem__(ind)

    def sort_cards(self, order):
        if order == 0:  # Sort after suit
            self.cards.sort(key=get_key0)
        elif order == 1:  # Sort after value
            self.cards.sort(key=get_key1)



hand = Hand()
hand.add_card((0,2))
hand.add_card((2,3))
hand.add_card((2,8))
hand.add_card((1,10))
hand.drop_card(0)
hand.sort_cards(1)

print(isinstance(hand, Hand))
print(hand.cards)
