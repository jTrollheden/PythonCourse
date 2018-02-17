import cardlib as cl

deck = cl.Deck()
deck.create_deck(1)
#deck.shuffle_deck()

card = cl.AceCard(cl.Suit(2))
card2 = cl.AceCard(cl.Suit(1))

hand = cl.Hand()
#for i in range(5):
#    hand.add_card(deck.draw())

card3 = cl.KingCard(cl.Suit(1))
card4 = cl.KingCard(cl.Suit(1))
card5 = cl.KingCard(cl.Suit(1))
card6 = cl.QueenCard(cl.Suit(1))
card7 = cl.QueenCard(cl.Suit(1))
card8 = cl.QueenCard(cl.Suit(1))

hand.add_card(card)
hand.add_card(card)
hand.add_card(card2)
hand.add_card(card3)
hand.add_card(card4)
hand.add_card(card5)
hand.add_card(card6)
hand.add_card(card7)
hand.add_card(card8)

hand.sort_cards()
#x = cl.check_straight_flush(hand.cards)
x = cl.check_full_house(hand.cards)

print(x)