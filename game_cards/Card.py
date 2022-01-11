class Card:
    def __init__(self, value, suit):
        """this method gets a value and a suit and constructs a card with the Attributes: value and suit.
        Also, this method checks if the value that we got is valid (0<x<14)
        and also this method checks if the suit that we got is valid (0<x<5)
        the method will not return anything."""
        if type(value) != int:
            raise TypeError
        if type(suit) != int:
            raise TypeError
        if value > 13 or value < 1:
            raise TypeError("value needs to be between 1 and 13")
        if suit > 4 or suit < 1:
            raise TypeError("suit needs to be between 1 and 4")
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        """this method gets a card and another card, if the cards have the same value and suit,
        the method will return True. if the method and the value are not the same the method will return False."""
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False

    def __gt__(self, other):
        """this method gets a card and another card, the method will return the higher card with the following terms:
        - if the cards are the same; then the method will return the card with the higher suit.
        - the value 1 means 'Ace', and it's equivalent to the highest value"""
        if self.value == 1 or other.value == 1:
            if self.value == 1 and other.value == 1:
                if self.suit > other.suit:
                    return True
                else:
                    return False
            if self.value == 1 and other.value != 1:
                return True
            if other.value == 1 and self.value != 1:
                return False
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        if self.value > other.value:
            return True
        else:
            return False

    def __repr__(self):
        """this method will return a string of a card"""
        if self.suit == 1:
            if self.value == 1:
                return f"Ace of Diamond"
            if self.value == 11:
                return f"Jack of Diamonds"
            if self.value == 12:
                return f"Queen of Diamonds"
            if self.value == 13:
                return f"King of Diamonds"
            else:
                return f"{self.value} of Diamond"
        if self.suit == 2:
            if self.value == 1:
                return f"Ace of Spade"
            if self.value == 11:
                return f"Jack of Spades"
            if self.value == 12:
                return f"Queen of Spades"
            if self.value == 13:
                return f"King of Spades"
            else:
                return f"{self.value} of Spades"
        if self.suit == 3:
            if self.value == 1:
                return f"Ace of Heart"
            if self.value == 11:
                return f"Jack of Hearts"
            if self.value == 12:
                return f"Queen of Hearts"
            if self.value == 13:
                return f"King of Hearts"
            else:
                return f"{self.value} of Hearts"
        if self.suit == 4:
            if self.value == 1:
                return f"Ace of Club"
            if self.value == 11:
                return f"Jack of Clubs"
            if self.value == 12:
                return f"Queen of Clubs"
            if self.value == 13:
                return f"King of Clubs"
            else:
                return f"{self.value} of Clubs"

