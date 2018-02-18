import cardlib as cl
from nose.tools import assert_raises

def test_cards():
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[0].value == 2
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[0].name == "Two"
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[1].value == 0
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[1].name == "Clubs"

def test_hand_and_deck():
    deck = cl.Deck()
    deck.create_deck()
    hand=cl.Hand()
    hand2 = cl.Hand()
    n = 5
    k = 0, 2, 4
    for i in range(n):
        hand.add_card(deck.draw())
    hand.drop_card(k)
    hand2.add_card(cl.KingCard(cl.Suit(0)))
    hand2.add_card(cl.JackCard(cl.Suit(0)))
    assert len(hand.cards) == n - len(k)
    assert hand.cards == hand2.cards
    hand2.add_card(cl.AceCard(cl.Suit(0)))
    hand2.sort_cards()
    assert hand2.cards[0] == cl.AceCard(cl.Suit(0))
    poker_hand = hand2.best_poker_hand()
    assert poker_hand.type == cl.HandType(1) # Test of best_poker_hand
    assert poker_hand.value == cl.AceCard(cl.Suit(0)).card[0]
    assert poker_hand.cards == hand2.cards

def test_pokerhand():
    deck = cl.Deck()
    deck.create_deck()
    hand=cl.Hand()
    hand2 = cl.Hand()
    for i in range(5):
        hand.add_card(deck.draw())
    for i in range(5):
        hand2.add_card(deck.draw())
    bph = hand.best_poker_hand()
    bph2 = hand2.best_poker_hand()
    assert bph > bph2
    assert bph == bph
    assert bph2 < bph

def test_straight_flush():
    deck = cl.Deck()
    deck.create_deck()
    hand = cl.Hand()
    for i in range(5):
        hand.add_card(deck.draw())
    k = cl.check_straight_flush(hand.cards)
    assert k[0] == 14
    assert k[1] == cl.AceCard(cl.Suit(3))
