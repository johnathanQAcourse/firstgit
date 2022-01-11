from unittest import TestCase
from Card import Card
from CardGame import CardGame
from DeckOfCards import DeckOfCards


class TestCardGame(TestCase):
    def setUp(self):
        self.game = CardGame("a", "b")

    def test__init__1(self):
        """test when the init variables are valid"""
        game = CardGame("A", "B", 15)
        self.assertTrue(game.p1.name == "A")
        self.assertTrue(game.p1.cards_to_deal == 15)
        self.assertTrue(game.p2.name == "B")
        self.assertTrue(game.p2.cards_to_deal == 15)
        self.assertIsInstance(game.deck, DeckOfCards)
        self.assertTrue(len(game.deck.deck) == 22)

    # noinspection PyUnusedLocal
    def test__init__2(self):
        """test when the parameters sent to init are invalid"""
        with self.assertRaises(TypeError):
            game = CardGame(1.5, "B", 15)
        with self.assertRaises(TypeError):
            game = CardGame("a", True, 15)
        with self.assertRaises(TypeError):
            game = CardGame("a", "B", "c")

    def test__init__3(self):
        """test when cards_to_deal parameter is invalid (9<x<27) x=9"""
        game = CardGame("A", "B", 9)
        self.assertTrue(game.p1.cards_to_deal == 26)
        self.assertTrue(game.p2.cards_to_deal == 26)
        self.assertTrue(len(game.deck.deck) == 0)

    def test__init__4(self):
        """test when cards_to_deal parameter is invalid (9<x<27) x=27"""
        game = CardGame("A", "B", 27)
        self.assertTrue(game.p1.cards_to_deal == 26)
        self.assertTrue(game.p2.cards_to_deal == 26)
        self.assertTrue(len(game.deck.deck) == 0)

    def test__init__5(self):
        """test when cards_to_deal parameter is not given"""
        game = CardGame("A", "B")
        self.assertTrue(game.p1.cards_to_deal == 26)
        self.assertTrue(game.p2.cards_to_deal == 26)
        self.assertTrue(len(game.deck.deck) == 0)

    def test_new_game(self):
        """test if the new_game function is only to be called from the constructor function
        -the other functionality of new game was checked in the init tests"""
        with self.assertRaises(AttributeError):
            self.game.new_game()

    def test_get_winner_1(self):
        """test when p2 is the winner, and p1 has no cards left"""
        self.game.p1.players_deck = []
        self.game.p2.players_deck = [Card(1, 2), Card(1, 1)]
        self.assertTrue(self.game.get_winner() == self.game.p2)

    def test_get_winner_2(self):
        """test when p1 is the winner, and p2 has no cards left"""
        self.game.p1.players_deck = [Card(1, 2), Card(1, 1)]
        self.game.p2.players_deck = []
        self.assertTrue(self.game.get_winner() == self.game.p1)

    def test_get_winner_3(self):
        """test when p1 is the winner, and p2 has 1 card less"""
        self.game.p1.players_deck = [Card(1, 2), Card(1, 1)]
        self.game.p2.players_deck = [Card(1, 2)]
        self.assertTrue(self.game.get_winner() == self.game.p1)

    def test_get_winner_4(self):
        """test when p2 is the winner, and p1 has 1 card less"""
        self.game.p1.players_deck = [Card(1, 2)]
        self.game.p2.players_deck = [Card(1, 2), Card(1, 1)]
        self.assertTrue(self.game.get_winner() == self.game.p2)

    def test_get_winner_5(self):
        """test when it's a tie"""
        self.game.p1.players_deck = [Card(1, 2), Card(1, 1)]
        self.game.p2.players_deck = [Card(1, 2), Card(1, 1)]
        self.assertTrue(self.game.get_winner() is None)

    def test_get_winner_6(self):
        """test when it's a tie, and both players have no cards left"""
        self.game.p1.players_deck = []
        self.game.p2.players_deck = []
        self.assertTrue(self.game.get_winner() is None)
