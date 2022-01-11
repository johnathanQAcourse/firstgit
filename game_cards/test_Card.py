from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card(1, 1)
        self.card2 = Card(1, 1)

    def test__Init__1(self):
        c1 = Card(1, 1)
        self.assertEqual(c1.value, 1)
        self.assertEqual(c1.suit, 1)
        with self.assertRaises(TypeError):
            c1 = Card(0, 1)
        with self.assertRaises(TypeError):
            c1 = Card(14, 1)
        with self.assertRaises(TypeError):
            c1 = Card(2, 0)
        with self.assertRaises(TypeError):
            c1 = Card(2, 5)

    def test__Init__2(self):
        """this test is to see if the constructor function accepts variable types that are not int"""
        with self.assertRaises(TypeError):
            c1 = Card("a", True)
        with self.assertRaises(TypeError):
            c1 = Card(1.2, "b")

    def test__eq__1(self):
        """test when the value and the suit are equal"""
        self.assertTrue(self.card1 == self.card2)

    def test__eq__2(self):
        """test when the values are the same but suits are not."""
        self.card2.suit = 2
        self.assertFalse(self.card1 == self.card2)

    def test__eq__3(self):
        """test when the values are different but suits are the same."""
        self.card2.value = 2
        self.assertFalse(self.card1 == self.card2)

    def test__eq__4(self):
        """test when the values and the suit are different."""
        self.card2.suit = 2
        self.card2.value = 2
        self.assertFalse(self.card1 == self.card2)

    def test__gt__1(self):
        """test when card1's value and the suit are greater"""
        self.card1.value = 3
        self.card1.suit = 3
        self.card2.value = 2
        self.card2.suit = 2
        self.assertTrue(self.card1 > self.card2)

    def test__gt__2(self):
        """test when card2's value and the suit are greater"""
        self.card2.value = 3
        self.card2.suit = 3
        self.card1.value = 2
        self.card1.suit = 2
        self.assertFalse(self.card1 > self.card2)

    def test__gt__3(self):
        """test when cards values are the same, card1's suit is greater"""
        self.card1.value = 3
        self.card1.suit = 3
        self.card2.value = 3
        self.card2.suit = 2
        self.assertTrue(self.card1 > self.card2)

    def test__gt__4(self):
        """test when cards values are the same, card2's suit is greater"""
        self.card1.value = 3
        self.card1.suit = 2
        self.card2.value = 3
        self.card2.suit = 3
        self.assertFalse(self.card1 > self.card2)

    def test__gt__5(self):
        """test when card1's value is Ace, card2's value is 13 and the suits are the same"""
        self.card1.value = 1
        self.card1.suit = 3
        self.card2.value = 13
        self.card2.suit = 3
        self.assertTrue(self.card1 > self.card2)

    def test__gt__6(self):
        """test when card2's value is Ace, card1's value is 13 and the suits are the same"""
        self.card1.value = 13
        self.card1.suit = 3
        self.card2.value = 1
        self.card2.suit = 3
        self.assertFalse(self.card1 > self.card2)

    def test__gt__7(self):
        """test when card1's value is Ace, card2's value is also Ace, card1's suit is greater."""
        self.card1.value = 1
        self.card1.suit = 3
        self.card2.value = 1
        self.card2.suit = 2
        self.assertTrue(self.card1 > self.card2)

    def test__gt__8(self):
        """test when card1's value is Ace, card2's value is also Ace, card2's suit is greater."""
        self.card1.value = 1
        self.card1.suit = 1
        self.card2.value = 1
        self.card2.suit = 2
        self.assertFalse(self.card1 > self.card2)
