import random
from Card import Card


class Player:
    def __init__(self, name, cards_to_deal=26):
        """this method is a constructor for the Player class
        the method gets the name of the player and sets the attribute name to the parameter it got
        the method also gets the number of cards to deal, by default it's 26. Also, if the number of cards to deal is over 26 or under 10,
        the method will set the number back to defalut."""
        if type(cards_to_deal) != int:
            raise TypeError("the number of cards to deal needs to be int")
        self.name = name
        if cards_to_deal > 26 or cards_to_deal < 10:
            cards_to_deal = 26
        self.cards_to_deal = cards_to_deal
        self.players_deck = []

    def set_hand(self, deck):
        """This method gets a deck of cards. The method uses it's attribute of how many cards to deal,
        and using a loop it will run the 'cards_to_deal' times.
        each time it runs, the player's deck will be added a card from the Deck the method got."""
        if self.cards_to_deal <= len(deck.deck):
            for i in range(self.cards_to_deal):
                card = deck.deal_one()
                if card not in self.players_deck:
                    self.players_deck.append(card)
        else:
            raise AttributeError("the deck needs to be bigger or equal than the 'cards_to_deal'")

    def get_card(self):
        """This method is randomly choosing a card from the player's deck.
        Once a card is chosen, the method is removing it from the player's deck.
        The method will return the Random Card."""
        if len(self.players_deck) > 0:
            card = random.choice(self.players_deck)
            if card in self.players_deck:
                self.players_deck.remove(card)
            return card
        else:
            raise AttributeError("cannot get a card from an empty deck")

    def add_card(self, card: Card):
        """This method is getting a card, and adds it to list of player's deck."""
        if type(card) != Card:
            raise TypeError("needs to be from Card Type")
        if card not in self.players_deck:
            self.players_deck.append(card)
        else:
            raise AttributeError("card already in players deck")

    def __repr__(self):
        """This method is returning a string with the player's name and his deck of cards."""
        return f"player's name: {self.name} \n" \
               f"player's deck: {self.players_deck}"
