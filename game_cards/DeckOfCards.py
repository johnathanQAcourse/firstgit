from Card import Card
import random


class DeckOfCards:
    def __init__(self):
        """this method is a constructor for the class - DeckofCards.
        this method constructs an empty list of cards
        after generating an empty list of cards the method fill the list with 52 cards."""
        self.deck = []
        for i in range(1, 5):
            for j in range(1, 14):
                card = Card(j, i)
                self.deck.append(card)

    def __repr__(self):
        """this method will return a string of the list of cards"""
        return f"{self.deck}"

    def cards_shuffle(self):
        """this method will shuffle the cards in the deck (using the random lib)"""
        random.shuffle(self.deck)

    def deal_one(self):
        """this method will randomly pick a card from the deck, remove it from the list and will return the card."""
        if len(self.deck) > 0:
            card = random.choice(self.deck)
            if card in self.deck:
                self.deck.remove(card)
            return card
        else:
            raise AttributeError("cannot deal anymore because deck ran out of cards")
