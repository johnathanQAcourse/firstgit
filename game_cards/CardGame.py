from DeckOfCards import DeckOfCards
from Player import Player

class CardGame:
    def __init__(self, name1, name2, cards_to_deal=26):
        """this method is a constructor for the CardGame class
                the method gets the names of the 2 players and sets two new attributes of new players in the class
                the method also gets the number of cards to deal, by default it's 26. Also, if the number of cards to deal is over 26 or under 10,
                the method will set the number back to default."""
        self.sentfrominit = True
        if type(cards_to_deal) != int:
            raise TypeError("cards_to_deal needs to be int")
        if type(name1) != str or type(name2) != str:
            raise TypeError("the players names must be string needs to be int")
        if cards_to_deal > 26 or cards_to_deal < 10:
            cards_to_deal = 26
        self.p1 = Player(name1, cards_to_deal)
        self.p2 = Player(name2, cards_to_deal)
        self.deck = DeckOfCards()
        self.new_game()

    def new_game(self):
        """This method is called only from the constructor and if is called from anywhere else it raises an error.
        The method is shuffling the deck, and sets the hand for every player using the shuffled deck.
        The method will set the hand for the second player using the remaining cards that weren't dealt to the other player. """
        if self.sentfrominit:
            self.deck.cards_shuffle()
            self.p1.set_hand(self.deck)
            self.p2.set_hand(self.deck)
            self.sentfrominit = False
        else:
            raise AttributeError("only the constructor can call this funq.")

    def get_winner(self):
        """This method returns the player who's left with more cards in his deck.
        if the two players are left with the same amount of cards then the method will return 'None'"""
        if len(self.p1.players_deck) < len(self.p2.players_deck):
            return self.p2
        if len(self.p1.players_deck) > len(self.p2.players_deck):
            return self.p1
        else:
            return None

    def __str__(self):
        """this method is returning a string of the game's players"""
        return f"player {self.p1}\n" \
               f"player {self.p2}"


