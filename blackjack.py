from random import randrange
from interface import *

#creates a deck of card as a list from 1 to 52
#called by: main()
def buildDeck():
    newDeck = []
    for suit in ["Clubs","Diamonds","Spades","Hearts"]:
        newDeck.append(["Ace", suit, 11])
        for numbered in range(2, 10+1):
            newDeck.append([numbered, suit, numbered])
        for royal in ["Jack", "Queen", "King"]:
            newDeck.append([royal, suit, 10])
    return newDeck

#called by drawCard()
#retrieves a random card from the deck and returns it
def getRandCard(deck):
	newCard = deck.pop(randrange(0, (len(deck))))
	return newCard, deck

#sets up the game and starts it
#the majority of the program runs from interface.py
def main():
	userInterface = interface()
	userInterface.run()

if __name__ == "__main__":
	main()