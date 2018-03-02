import cardlib as cl


def test_cards():
    #  Testing so that the card functions give the correct values
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[0].value == 2
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[0].name == "Two"
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[1].value == 0
    assert cl.NumberedCard(cl.Rank(2), cl.Suit(0)).card[1].name == "Clubs"
    assert cl.JackCard(cl.Suit(0)).give_value().value == 11
    assert cl.QueenCard(cl.Suit(0)).give_value().value == 12
    assert cl.KingCard(cl.Suit(0)).give_value().value == 13
    assert cl.AceCard(cl.Suit(0)).give_value().value == 14


def test_hand_and_deck():
    #  Creating the cards and then testing them towards the values they should have. Checking if the functions in the
    #  hand and deck classes are working as well as the values from the poker_hand class.
    deck = cl.Deck()
    deck.create_deck()  # Testing create_deck func
    hand = cl.Hand()
    hand2 = cl.Hand()
    n = 5
    k = [0, 2, 4]
    for i in range(n):
        hand.add_card(deck.draw())  # Testing add_card function
    hand.drop_cards(k)              # Testing drop_cards funtion
    hand2.add_card(cl.KingCard(cl.Suit(0)))
    hand2.add_card(cl.JackCard(cl.Suit(0)))
    assert len(hand.cards) == n - len(k)
    assert hand.cards == hand2.cards
    hand2.add_card(cl.AceCard(cl.Suit(0)))
    hand2.sort_cards()  # Test of sort function
    assert hand2.cards[0] == cl.AceCard(cl.Suit(0))
    poker_hand = hand2.best_poker_hand()
    assert poker_hand.type == cl.HandType(1)  # Test of best_poker_hand
    assert poker_hand.value == cl.AceCard(cl.Suit(0)).card[0]
    assert poker_hand.cards == hand2.cards


def test_pokerhand():
    #  Creating the pokerhand objects and then testing them against other pokerhands.
    deck = cl.Deck()
    deck.create_deck()
    hand = cl.Hand()
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
    #  Checking the Straight Flush function
    deck = cl.Deck()
    deck.create_deck()
    hand = cl.Hand()
    for i in range(5):
        hand.add_card(deck.draw())
    k = cl.check_straight_flush(hand.cards)
    assert k[0] == 14
    assert k[1] == cl.AceCard(cl.Suit(3))
    hand.drop_cards(0)
    assert cl.check_straight_flush(hand.cards) is None


def test_four_kind():
    #  Checking the four kind function
    hand = cl.Hand()
    for i in range(4):
        hand.add_card(cl.NumberedCard(cl.Rank(2), cl.Suit(0)))
    k = cl.check_four_kind(hand.cards)
    assert k[0] == hand.cards[0].give_value().value
    assert k[1] == hand.cards
    hand.drop_cards(0)
    assert cl.check_four_kind(hand.cards) is None


def test_full_house():
    #  Checking the full house function
    hand = cl.Hand()
    for i in range(3):
        hand.add_card(cl.NumberedCard(cl.Rank(2), cl.Suit(0)))
    for i in range(2):
        hand.add_card(cl.NumberedCard(cl.Rank(3), cl.Suit(0)))
    k = cl.check_full_house(hand.cards)
    hand.sort_cards()
    assert k[0][0] == cl.NumberedCard(cl.Rank(2), cl.Suit(0)).give_value().value
    assert k[0][1] == cl.NumberedCard(cl.Rank(3), cl.Suit(0)).give_value().value
    assert k[1][0][0].give_value() == hand.cards[4].give_value()
    assert k[1][1][0].give_value() == hand.cards[0].give_value()
    hand.drop_cards(0)
    assert cl.check_full_house(hand.cards) is None


def test_flush():
    #  Checking the flush function
    hand = cl.Hand()
    for i in range(5):
        hand.add_card(cl.NumberedCard(cl.Rank(2), cl.Suit(0)))
    k = cl.check_flush(hand.cards)
    assert k[0] == cl.NumberedCard(cl.Rank(2), cl.Suit(0)).give_value().value
    assert k[1] == hand.cards
    hand.drop_cards(0)
    assert cl.check_flush(hand.cards) is None


def test_straight():
    #  Checking the straight function
    hand = cl.Hand()
    for i in range(2, 11):
        hand.add_card(cl.NumberedCard(cl.Rank(i), cl.Suit(0)))
    k = cl.check_straight(hand.cards)
    assert k[0] == cl.NumberedCard(cl.Rank(10), cl.Suit(0)).give_value().value
    hand.sort_cards()
    assert k[1] == hand.cards[:5]
    hand.cards = hand.cards[:4]
    assert cl.check_straight(hand.cards) is None


def test_three_kind():
    #  Checking the three kind function
    hand = cl.Hand()
    for i in range(3):
        hand.add_card(cl.NumberedCard(cl.Rank(3), cl.Suit(0)))
    k = cl.check_three_kind(hand.cards)
    assert k[0] == cl.NumberedCard(cl.Rank(3), cl.Suit(0)).give_value().value
    assert k[1] == hand.cards
    hand.drop_cards(0)
    hand2 = cl.Hand()
    hand2.cards = hand.cards
    assert cl.check_three_kind(hand2.cards) is None


def test_two_pair():
    #  Checking the two pair function
    hand = cl.Hand()
    for i in range(3, 5):
        hand.add_card(cl.NumberedCard(cl.Rank(i), cl.Suit(0)))
        hand.add_card(cl.NumberedCard(cl.Rank(i), cl.Suit(0)))
    k = cl.check_two_pair(hand.cards)
    assert k[0][0] == cl.NumberedCard(cl.Rank(4), cl.Suit(0)).give_value().value
    assert k[0][1] == cl.NumberedCard(cl.Rank(3), cl.Suit(0)).give_value().value
    assert k[1][0][0] == cl.NumberedCard(cl.Rank(4), cl.Suit(0))
    assert k[1][1][0] == cl.NumberedCard(cl.Rank(3), cl.Suit(0))


def test_pair():
    #  Checking the pair function
    hand = cl.Hand()
    hand.add_card(cl.NumberedCard(cl.Rank(2), cl.Suit(0)))
    hand.add_card(cl.NumberedCard(cl.Rank(2), cl.Suit(0)))
    hand.add_card(cl.NumberedCard(cl.Rank(4), cl.Suit(0)))
    hand.add_card(cl.NumberedCard(cl.Rank(4), cl.Suit(0)))
    k = cl.check_pair(hand.cards)
    hand.sort_cards()
    hand.drop_cards([2, 3])
    assert k[0] == cl.NumberedCard(cl.Rank(4), cl.Suit(0)).give_value().value
    assert k[1] == hand.cards


def test_high_card():
    #  Checking the highest card function
    hand = cl.Hand()
    hand.add_card(cl.AceCard(cl.Suit(2)))
    hand.add_card(cl.AceCard(cl.Suit(3)))
    hand.add_card(cl.NumberedCard(cl.Rank(2), cl.Suit(0)))
    k = cl.check_high_card(hand.cards)
    assert k[1] == hand.cards
    assert k[0] == cl.AceCard(cl.Suit(3)).give_value().value
    assert k[1][0].give_suit().value == cl.AceCard(cl.Suit(3)).give_suit().value