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

	#called by: readHand()
	#tests if the card is a royal card (11 to 13) and a returns it as a string
	def testRoyal(self, cardValue):
		if cardValue == 1:
			cardValue = "Ace"
		if cardValue == 11:
			cardValue = "Jack"
		if cardValue == 12:
			cardValue = "Queen"
		if cardValue == 13:
			cardValue = "King"
		return cardValue
		
	#calls: testRoyal(), 
	#called by: seePHand(), seeDHand(), seeDCard(),
	#takes in a hand
	def readHand(self):
		rHand = []
		for card in self.cards:
			rCard = self.testRoyal(card[0])
			rHand.append(str(rCard) + " of " + card[1])
		return rHand
	
	#convert's the given hand and prints it out to the screen
	#calls: readHand()
	#called by: main(), playerMove(), assessHands()
	def seePHand(self):
		self.updateTotal()
		print("Your Hand:", self.total)
		rHand = self.readHand()
		for card in rHand:
			print("     " + card)

	#convert's the dealer's hand and prints it out as to the screen
	#calls: readHand()
	#called by: assessHands()
	def seeDHand(self):
		self.updateTotal()
		print("Dealer's hand:", self.total)
		rHand = self.readHand()
		for card in rHand:
			print("     " + card)

	#show's the dealer's hand at the beginning of the game:
	#on card visible, one card unknown
	#calls: readHand()
	#called by: main()
	def seeDCard(self):
		rHand = self.readHand()
		print("Dealer's hand:", ">", end=" ")
		if self.measureCardPoints(self.cards[0][0]) == 11:
			print("11 or 1")
		else:
			print(self.measureCardPoints(self.cards[0][0]))
		print("     " + rHand[0])
		print("     " + "???????????")
	
	#changes the cards to the numbers of points
	#called by: calcTotal(), calcAceTotal()
	def measureCardPoints(self, card):
		points = card
		if not card <= 13:
			if card <= 26:
				points = card - 13
			elif card <= 39:
				points = card - 26
			else:
				points = card - 39
		if points == 11: #jack
			points = 10
		if points == 12: #queen
			points = 10
		if points == 13: #king
			points = 10
		if points == 1: #ace - this if-statement must go after #jack
			points = 11
		return points
	
	def updateTotal(self):
		self.total = calcTotal(self)

#calculates the total value of the card
#calls: measureCardPoints(), calcAceTotal()
#called by: playerMove(), dealerMove(), assessHands()
def calcTotal(Hand):
	total = 0
	for card in Hand.cards:
		cardPoints = Hand.measureCardPoints(card[0])
		total = total + cardPoints
	#if the total value with ace being 11 is over 21, it uses the ace as 1 instead
	if total > 21 and calcAceTotal(Hand) < 21:
		total = calcAceTotal(Hand)
	return total

#measures the total number of points with the ace being worth 1
	#calls: measureCardPoints()
	#called by: calcTotal()
def calcAceTotal(Hand):
	aceFactor = 0
	aceTotal = 0
	tested1ace = False
	acesCount = 0
	for card in Hand.cards:
		cardPoints = Hand.measureCardPoints(card[0])
		if cardPoints == 11:
			acesCount += 1
		else:
			aceTotal = aceTotal + cardPoints
	#determines the different possibilities with different numbers of aces
	if acesCount == 1:
		aceTotal = aceTotal + 1
	elif acesCount == 2:
		if (aceTotal + 12) > 21:
			aceTotal = aceTotal + 2
		else:
			aceTotal = aceTotal + 12
	elif acesCount == 3:
		if (aceTotal + 11 + 1 + 1) > 21:
			aceTotal = aceTotal + 3
		else:
			aceTotal = aceTotal + 13
	elif acesCount == 4:
		if (aceTotal + 11 + 1 + 1) > 21:
			aceTotal = aceTotal + 4
		else:
			aceTotal = aceTotal + 14
	print("aceTotal is", aceTotal)
	return aceTotal

#called by drawCard()
#retrieves a random card from the deck and returns it
def getRandCard(deck):
	newCard = deck.pop(randrange(0, (len(deck))))
	return newCard, deck