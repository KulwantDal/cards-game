from Card import Card
import random

class CardOpr():
    def getNewDeck(self):
        deck = []
        for suit in range(4):
            for rank in range(13):
                deck.append(Card(suit, rank + 1))

        return deck


    def printWholeDeck(self, deck):
        for card in deck:
            print(card)


    def shuffleDeck(self, deck):
        return random.shuffle(deck)