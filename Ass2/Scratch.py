import cardlib as cl

card = cl.NumberedCard(cl.Rank(6), cl.Suit(0))
card2 = cl.AceCard(cl.Suit(0))
card3 = cl.QueenCard(cl.Suit(3))

print(card2.card)
print(card.card)

hand = cl.Hand()
hand.add_card(card)
hand.add_card(card2)
hand.add_card(card3)

print(hand.cards)

#print(hand)
#hand.sort_cards()
#print(hand)

# print(card.give_value())
# print(card2.give_value()[0].value>card.give_value()[0].value)
# print(card2.give_value()[1].value==card.give_value()[1].value)
#
