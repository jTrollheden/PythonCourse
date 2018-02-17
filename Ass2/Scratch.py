import cardlib as cl

deck = cl.Deck()
deck.create_deck()
#deck.shuffle_deck()
hand = cl.Hand()
for i in range(5):
    hand.add_card(deck.draw())

card = cl.AceCard(cl.Suit(2))
card2 = cl.AceCard(cl.Suit(1))
card3 = cl.KingCard(cl.Suit(1))
card4 = cl.QueenCard(cl.Suit(1))
card5 = cl.QueenCard(cl.Suit(2))
card6 = cl.NumberedCard(cl.Rank(2), cl.Suit(2))

hand.add_card(card)
hand.add_card(card)
hand.add_card(card)
hand.add_card(card3)
hand.add_card(card3)
hand.add_card(card3)
hand.add_card(card3)
hand.add_card(card3)
hand.add_card(card3)

hand.sort_cards()
#x = cl.check_straight_flush(hand.cards)
#x = cl.check_full_house(hand.cards)
#x = cl.check_four_kind(hand.cards)
#x = cl.check_straight(hand.cards)
x = cl.check_flush(hand.cards)

print(x)