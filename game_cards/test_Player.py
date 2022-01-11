from unittest import TestCase
from unittest.mock import patch
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player


class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("a")

    def test__init__1(self):
        """test to see if the parameters are inserted correctly into the attributes"""
        player = Player("a", 11)
        self.assertTrue(player.name == "a")
        self.assertTrue(player.cards_to_deal == 11)
        self.assertTrue(len(player.players_deck) == 0)

    def test__init__2(self):
        """test to see if the cards_to_deal is default without entering it"""
        player = Player("a")
        self.assertTrue(player.name == "a")
        self.assertTrue(player.cards_to_deal == 26)
        self.assertTrue(len(player.players_deck) == 0)

    def test__init__3(self):
        """test to see if the cards_to_deal is default when you enter invalid variable """
        player = Player("a", 9)
        self.assertTrue(player.name == "a")
        self.assertTrue(player.cards_to_deal == 26)
        self.assertTrue(len(player.players_deck) == 0)

    def test__init__4(self):
        """test to see if the cards_to_deal is default when you enter invalid variable """
        player = Player("a", 27)
        self.assertTrue(player.name == "a")
        self.assertTrue(player.cards_to_deal == 26)
        self.assertTrue(len(player.players_deck) == 0)

    # noinspection PyUnusedLocal
    def test__init__5(self):
        """test to see if the init function accepts other variable types for cards to deal"""
        with self.assertRaises(TypeError):
            p1 = Player("a", True)
        with self.assertRaises(TypeError):
            c1 = Card(1.2, "b")

    def test_set_hand1(self):
        """this is to test if the player's deck was dealt correctly"""
        with patch("DeckOfCards.DeckOfCards.deal_one") as mock_deal_one:
            mock_deal_one.return_value = Card(3, 2)
            deck = DeckOfCards()
            self.player.cards_to_deal = 1
            self.player.set_hand(deck)
            self.assertTrue(len(self.player.players_deck) == 1)
            self.assertTrue(mock_deal_one.return_value in self.player.players_deck)

    def test_set_hand2(self):
        """this is to test if the set hand function inserts cards that it already has"""
        with patch("DeckOfCards.DeckOfCards.deal_one") as mock_deal_one:
            mock_deal_one.return_value = Card(3, 2)
            deck = DeckOfCards()
            self.player.cards_to_deal = 5
            self.player.set_hand(deck)
            self.assertTrue(len(self.player.players_deck) == 1)
            self.assertTrue(mock_deal_one.return_value in self.player.players_deck)

    def test_set_hand3(self):
        """this is to test if the set hand function gets cards_to_deal that is bigger than the deck sent"""
        with patch("DeckOfCards.DeckOfCards.deal_one") as mock_deal_one:
            mock_deal_one.return_value = Card(3, 2)
            deck = DeckOfCards()
            self.player.cards_to_deal = 53
            with self.assertRaises(AttributeError):
                self.player.set_hand(deck)

    def test_get_card1(self):
        """this is to test that get_card function is randomly choosing a card from the deck
         and removing it from the players deck"""
        self.player.set_hand(DeckOfCards())
        length = len(self.player.players_deck)
        c1 = self.player.get_card()
        self.assertFalse(c1 in self.player.players_deck)
        self.assertTrue(length - 1 == len(self.player.players_deck))

    def test_get_card2(self):
        """test to see if any exceptions were raised if the players deck was empty"""
        self.player.set_hand(DeckOfCards())
        for i in range(26):
            self.player.get_card()
        with self.assertRaises(AttributeError):
            self.player.get_card()

    def test_add_card_Valid(self):
        """this is to test if the add_card function adds the card sent to it to the player's deck"""
        self.player.set_hand(DeckOfCards())
        length = len(self.player.players_deck)
        self.player.add_card(Card(3, 2))
        self.assertTrue(Card(3, 2) in self.player.players_deck)
        self.assertTrue(length + 1 == len(self.player.players_deck))

    def test_add_card_inValid_type(self):
        """this is to test if the add_card function adds the integer variable sent to it to the player's deck"""
        self.player.set_hand(DeckOfCards())
        length = len(self.player.players_deck)
        with self.assertRaises(TypeError):
            self.player.add_card(3)
        self.assertTrue(length == len(self.player.players_deck))

    def test_add_card_Already_in_deck(self):
        """this is to test if the add_card function adds cards that are already in the deck"""
        self.player.cards_to_deal = 52
        self.player.set_hand(DeckOfCards())
        length = len(self.player.players_deck)
        with self.assertRaises(AttributeError):
            self.player.add_card(Card(3, 2))
        self.assertTrue(length == len(self.player.players_deck))
