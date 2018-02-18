import cardlib as cl
import test_cardlib as tcl

deck = cl.Deck()
deck.create_deck()
#deck.shuffle_deck()
hand=cl.Hand()
for i in range(5):
    hand.add_card(deck.draw())

k = cl.check_straight_flush(hand.cards)
print((k))