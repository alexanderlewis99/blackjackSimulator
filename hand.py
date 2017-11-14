#hand.py

''' Creates a hand of cards.'''

from random import randrange

class Hand:
	def __init__(self, deck):
		card1, deck = self.getRandCard(deck)
		card2, deck = self.getRandCard(deck)
		self.cards = [card1, card2]
		self.total = self.calcTotal()
	
	#takes a random card from the deck and returns the card and new deck
	#calls getRandCard()
	def drawCard(self, deck):
		newCard, deck = self.getRandCard(deck)
		self.cards.append(newCard)
		return deck

	#called by: seePHand(), seeDHand(), seeDCard(),
	#takes in a hand
	def getCards(self):
		return self.cards
	
	#changes the cards to the numbers of points
	#called by: calcTotal(), calcAceTotal()
	def updateTotal(self):
		self.total = self.calcTotal()

#calculates the total value of the card
#calls: measureCardPoints(), calcAceTotal()
#called by: playerMove(), dealerMove(), assessHands()
	def calcTotal(self):
		countingTotal = 0
		for card in self.cards:
			cardPoints = card[2]
			countingTotal = countingTotal + cardPoints
		#if the total value with ace being 11 is over 21, it uses the ace as 1 instead
		if countingTotal > 21 and (self.calcAceTotal() < 21 or self.calcAceTotal() < countingTotal):
			countingTotal = self.calcAceTotal()
		return countingTotal

#measures the total number of points with the ace being worth 1
	#calls: measureCardPoints()
	#called by: calcTotal()
	def calcAceTotal(self):
		aceTotal = 0
		acesCount = 0
		for card in self.cards:
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
	def getRandCard(self, deck):
		newCard = deck.pop(randrange(0, (len(deck))))
		return newCard, deck