from random import randrange
from interface import *
from hand import *

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
    
def unitTestCalcTotal():
	testDeck = buildDeck()
	testHand = Hand(testDeck)
	testHand.cards = [["Ace", "Hearts", 11],[2, "Clubs", 2],[8, "Diamonds", 8]]
	return testHand.calcTotal() == 21

def unitTestAceTotal():
	test2Deck = buildDeck()
	test2Hand = Hand(test2Deck)
	test2Hand.cards = [["Ace", "Hearts", 11],["Ace", "Clubs", 11],["Ace", "Diamonds", 11]]
	return test2Hand.calcAceTotal() == 13

#sets up the game and starts it
#the majority of the program runs from interface.py
def main():
	if unitTestCalcTotal() == True and unitTestAceTotal() == True:
		print("All unit tests passed. Beginning game...")
		userInterface = interface()
		userInterface.run()
	else:
		print("Uh oh. Something went wrong.")
		print("We are sending our robot technitions to fix it")

if __name__ == "__main__":
	main()
