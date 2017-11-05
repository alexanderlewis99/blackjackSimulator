#hand.py

''' Creates a hand of cards.'''

from random import randrange

class Hand:
	def __init__(self, deck):
		card1, deck = getRandCard(deck)
		card2, deck = getRandCard(deck)
		self.cards = [card1, card2]
		self.total = calcTotal(self)
	
	#takes a random card from the deck and returns the card and new deck
	#calls getRandCard()
	def drawCard(self, deck):
		newCard, deck = getRandCard(deck)
		self.cards.append(newCard)
		return deck

	#called by: seePHand(), seeDHand(), seeDCard(),
	#takes in a hand
	def readHand(self):
		rHand = []
		for card in self.cards:
			rHand.append(str(card[0]) + " of " + card[1])
		return rHand
	
	#convert's the given hand and prints it out to the screen
	#calls: readHand()
	#called by: main(), playerMove(), assessHands()
	def seeHand(self, player):
		self.updateTotal()
		print(player, "hand:", self.total)
		rHand = self.readHand()
		for card in rHand:
			print("     " + card)

	#show's the dealer's hand at the beginning of the game:
	#on card visible, one card unknown
	#calls: readHand()
	#called by: main()
	def seeDCard(self):
		rHand = self.readHand()
		print("Dealer's hand: >", end=" ")
		if self.cards[0][2] == 11:
			print("11 or 1")
		else:
			print(self.cards[0][2])
		print("     " + rHand[0])
		print("     " + "???????????")
	
	#changes the cards to the numbers of points
	#called by: calcTotal(), calcAceTotal()
	
	def updateTotal(self):
		self.total = calcTotal(self)

#calculates the total value of the card
#calls: measureCardPoints(), calcAceTotal()
#called by: playerMove(), dealerMove(), assessHands()
def calcTotal(Hand):
	total = 0
	for card in Hand.cards:
		cardPoints = card[2]
		total = total + cardPoints
	#if the total value with ace being 11 is over 21, it uses the ace as 1 instead
	if total > 21 and (calcAceTotal(Hand) < 21 or calcAceTotal(Hand) < total):
		total = calcAceTotal(Hand)
	return total

#measures the total number of points with the ace being worth 1
	#calls: measureCardPoints()
	#called by: calcTotal()
def calcAceTotal(Hand):
	aceTotal = 0
	acesCount = 0
	for card in Hand.cards:
		cardPoints = card[2]
		if cardPoints == 11:
			acesCount += 1
		else:
			aceTotal += cardPoints
	#determines the different possibilities with different numbers of aces
	if (aceTotal + 11 + (acesCount-1)) < 21:
		aceTotal += 11 + (acesCount-1)
	else:
		aceTotal += acesCount
	return aceTotal

#called by drawCard()
#retrieves a random card from the deck and returns it
def getRandCard(deck):
	newCard = deck.pop(randrange(0, (len(deck))))
	return newCard, deck