from unittest import TestCase
from unittest.mock import patch
from Card import Card
from DeckOfCards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test__init__(self):
        self.assertTrue(len(self.deck.deck) == 52)
        for i in range(1, 5):
            for j in range(1, 14):
                newcard = Card(j, i)
                self.assertIn(newcard, self.deck.deck)

    def test_cards_shuffle(self):
        """test to see if deck was actually shuffled and to see if the deck kept all the cards"""
        self.deck.cards_shuffle()
        self.assertTrue(len(self.deck.deck) == 52)
        for i in range(1, 5):
            for j in range(1, 14):
                newcard = Card(j, i)
                self.assertIn(newcard, self.deck.deck)

    def test_deal_one_1_Valid(self):
        """test to see if the card that dealt was actually removed from the list"""
        card = self.deck.deal_one()
        self.assertTrue(len(self.deck.deck) == 51)
        self.assertTrue(card not in self.deck.deck)

    def test_deal_one_2_with_mock(self):
        """test to see if the card that dealt was actually removed from the list using mock"""
        with patch("random.choice") as mock_choice:
            mock_choice.return_value = Card(3, 2)
            c1 = self.deck.deal_one()
            self.assertTrue(len(self.deck.deck) == 51)
            self.assertTrue(c1 not in self.deck.deck)

    def test_deal_one_3_with_empty_deck(self):
        """test to see if any exceptions were raised if the deck was empty"""
        deck = DeckOfCards()
        for i in range(52):
            deck.deal_one()
        with self.assertRaises(AttributeError):
            c1 = deck.deal_one()

    def test_deal_one_3_with_already_removed_card(self):
        """this is to test the function when the card is no longer in the list
        -needs to be said that this particular situation cannot happen because the function 'choice' is picking a random from the list,
        and cannot choose an item that is not on the list."""
        with patch("random.choice") as mock_choice:
            mock_choice.return_value = Card(2, 1)
            c1 = self.deck.deal_one()
            self.assertTrue(len(self.deck.deck) == 51)
            c2 = self.deck.deal_one()
            self.assertTrue(len(self.deck.deck) == 51)
            self.assertTrue(c1 not in self.deck.deck)
            self.assertTrue(c2 not in self.deck.deck)
