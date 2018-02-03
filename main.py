from CardOpr import CardOpr

cardOpr = CardOpr()
deck = cardOpr.getNewDeck()
#cardOpr.printWholeDeck(deck)
cardOpr.shuffleDeck(deck)

length=len(deck)
while len(deck) >= 2:
    index_choosen = int(input("User please choose your card from 1-%d: " %(length)))
    card = deck.pop(index_choosen - 1)
    print("Your card is: ", card)

    print("Computer Choosing it's card ....")
    card_computer = deck.pop()
    print("Computer Card is: ", card_computer)

    if card < card_computer:
        print("You Loose")
        break

    length -= 2