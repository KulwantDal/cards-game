class Card():

    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self, suit=0, rank=1):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.ranks[self.rank - 1] +  " Of " + self.suits[self.suit]


    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        elif self.suit == other.suit and self.rank < other.rank:
            return True

        return False