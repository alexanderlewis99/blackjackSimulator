#interface.py

from graphics import *
from button import Button 
from blackjack import *
from hand import *
from visualCard import GUICard

class interface():
	def __init__(self):
		self.win = GraphWin("Blackjack Simulator", 1050, 750)
		self.win.setCoords(0.0, 0.0, 350.0, 250.0)
		self.money = 10
		self.round = 1

	#creates a card
	#the card is either on the dealer or player's side depending on the variable playerOrDealer
	def drawACard(self, cardNumber, playerOrDealer):
		if playerOrDealer == "Player":
			rank = self.playerCards[cardNumber][0]
			suit = self.playerCards[cardNumber][1]
		else: #playerOrDealer == "Dealer":
			rank = self.dealerCards[cardNumber][0]
			suit = self.dealerCards[cardNumber][1]
		rxCoord = (10 + 60)*(cardNumber+1)
		visualCard = GUICard(self.win, rank, suit, rxCoord, playerOrDealer)
		visualCard.drawSelf()
		self.cardList.append(visualCard)

	#draws the first four cards, with the hidden one being a blue rectangle
	def drawInitialsCards(self):
		self.drawACard(0, "Player")
		self.drawACard(1, "Player")
		self.drawACard(0, "Dealer")
		rxCoord = (10 + 60)*2
		self.hiddenCard = Polygon(Point(rxCoord - 60, 50 + 80 + 20), Point(rxCoord, 50 + 80 + 20),
					    	Point(rxCoord, 130 + 80 + 20), Point(rxCoord - 60, 130 + 80 + 20))
		self.hiddenCard.setFill("blue")
		self.hiddenCard.draw(self.win)
		self.updatePlayerTotalLabel()
		if self.dHand.cards[0][0] == "Ace":
			self.dealerTotalLabel.setText("Dealer: > 11")
		else:
			self.dealerTotalLabel.setText("Dealer: > " + str(self.dHand.cards[0][2]))

	#runs the game and controls what is going on
	def run(self):
		#draws the background
		background = Polygon(Point(0, 0), Point(0, 250), Point(350, 250), Point(350, 0))
		bgColor = color_rgb(60, 170, 0)
		background.setFill(bgColor)
		background.draw(self.win)
		#constructs buttons
		self.buildButtonsAndTextbox()
		pt = self.win.getMouse()
		self.buildPlayerAndDealerTextboxes()
		gameRunning = True
		while gameRunning == True:
			#draws the cards
			self.setUpHandsAndCards()
			self.drawInitialsCards()
			turn = 'player'
			turnNum = 0
			#player bets money
			bet = self.makeBet()
			self.updateMoney(self.money-bet)
			#player's turn
			while turn == 'player':
				moveResult = self.playerMove()
				if moveResult == 'gameOver':
					self.updateInstructions("You busted!")
					self.deactivateChoiceButtons()
					turn = 'none'
				elif moveResult == 'dealerTurn':
					turn = 'computer'
					self.deactivateChoiceButtons()
				#else - if moveResult == 'gameGoing', nothing happens, the loop keeps running
			#computer's turn
			if turn == 'computer':
				self.dealerMove()
			#winner determined
			roundOutcome = self.assessHands(bet)
			#end of game; sees if player wants to continue
			self.updateMoney(self.money + roundOutcome)
			gameRunning = self.playAgainOrNot()
	
	def deactivateChoiceButtons(self):
		self.drawACardButton.deactivate()
		self.holdButton.deactivate()
	
	def playAgainOrNot(self):
		self.playAgainButton = Button(self.win,Point(130,125),60,30,'Play Again?')
		self.QuitGameButton = Button(self.win,Point(220,125),60,30,'End Game')
		self.playAgainButton.activate()
		self.QuitGameButton.activate()
		buttonPlayQuitClicked = False
		while buttonPlayQuitClicked == False:
			pt = self.win.getMouse()
			if self.playAgainButton.clicked(pt):
				self.updateRoundLabel()
				self.playerTotalLabel.setText("")
				self.dealerTotalLabel.setText("")
				self.updateInstructions("")
				self.playAgainButton.undrawSelf()
				self.QuitGameButton.undrawSelf()
				self.hiddenCard.undraw()
				for card in self.cardList:
					card.undrawSelf()
				self.cardList = []
				buttonPlayQuitClicked == True
				return True
			elif self.QuitGameButton.clicked(pt):
				buttonPlayQuitClicked = True
				self.win.close()
				return False

	def setUpHandsAndCards(self):
		self.deck = buildDeck()
		self.pHand = Hand(self.deck)
		self.dHand = Hand(self.deck)
		self.dealerCards = self.dHand.getCards()
		self.playerCards = self.pHand.getCards()		
		self.cardList = []

	#creates the "Draw Card", "Hold" and "Bet" buttons
	#creates the "Money" and "Round" text fields
	def buildButtonsAndTextbox(self):
		#The Buttons
		self.drawACardButton = Button(self.win,Point(10+30,10+15),60,30,'Draw Card')
		self.holdButton = Button(self.win,Point(80+30,10+15),60,30,'Hold')
		self.betButton = Button(self.win,Point(150+30,10+15),60,30,'Bet')
		#Money Total
		self.moneyLabel = Text(Point(320,10+15), ("Money: 10"))
		self.moneyLabel.setSize(36)
		self.moneyLabel.draw(self.win)
		#Text Instructions
		self.instructions = Text(Point(175,240), ("Welcome to Blackjack! Click to begin"))
		self.instructions.setSize(36)
		self.instructions.draw(self.win)
		#Round Number
		self.roundLabel = Text(Point(220+30,10+15), ("Round: " + str(self.round)))
		self.roundLabel.setSize(36)
		self.roundLabel.draw(self.win)
		#Betting Entry
		self.bet = Entry(Point(198,10+15), 3)
		self.bet.setSize(20)
	
	#creates the textboxes showing the Player's and Dealer's scores
	def buildPlayerAndDealerTextboxes(self):
		#dealer's's Total
		self.dealerTotalLabel = Text(Point(40,240), ("Dealer:"))
		self.dealerTotalLabel.setSize(36)
		self.dealerTotalLabel.draw(self.win)
		#dealer's's Total
		self.playerTotalLabel = Text(Point(40,140), ("Player:"))
		self.playerTotalLabel.setSize(36)
		self.playerTotalLabel.draw(self.win)

	#updates the money in the game and the label displaying it
	def updateMoney(self, newTotal):
		self.money = newTotal
		self.moneyLabel.setText("Money: " + str(newTotal))
	
	#updates the "instructions" – the text at the top of the window
	def updateInstructions(self, newInstructions):
		self.instructions.setText(newInstructions)
	
	#updates the round and the label displaying it
	def updateRoundLabel(self):
		self.round += 1
		self.roundLabel.setText("Round: " + str(self.round))
	
	#updates the label displaying the player's total
	def updatePlayerTotalLabel(self):
		self.playerTotalLabel.setText("Player: " + str(self.pHand.calcTotal()))

	def updateDealerTotalLabel(self):
		self.dealerTotalLabel.setText("Dealer: " + str(self.dHand.calcTotal()))
	
	def makeBet(self): #returns the entered amount
		self.updateInstructions("Make a bet")
		self.betButton.activate()
		self.bet.draw(self.win)
		buttonClicked = False
		while buttonClicked == False:
			pt = self.win.getMouse()
			if self.betButton.clicked(pt):
				try:
					if int(self.bet.getText()) < 0:
						self.updateInstructions("You can't bet negative money.")
					elif int(self.bet.getText()) > self.money and self.money > 0:
						self.updateInstructions("You don't have that much money.")
					elif self.money <= 0 and int(self.bet.getText()) > 5:
						self.updateInstructions("Loans must be less than 5 dollars.")
					else: #self.bet.getText() =< self.money
						return int(self.bet.getText()) 
						buttonClicked = True
				except:
					self.updateInstructions("Only integers are accepted")

	#used by Playermove
	def ChoiceDrawOrHold(self):
		self.bet.undraw()
		self.updateInstructions("Draw a card or hold")
		self.betButton.deactivate()
		self.drawACardButton.activate()
		self.holdButton.activate()
		buttonClicked = False
		while buttonClicked == False:
			pt = self.win.getMouse()
			if self.drawACardButton.clicked(pt):
				return "Draw"
				buttonClicked = True
			if self.holdButton.clicked(pt):
				return "Hold"
				buttonClicked = True
		
	def pressHold(self):
		self.holdButton.activate()
		pt = self.win.getMouse()
		while self.holdButton.clicked(pt) == False:
			pt = self.win.getMouse()
		self.holdButton.deactivate()
	
	def updatePlayerCards(self):
		self.playerCards = self.pHand.getCards()
		
	def updateDealerCards(self):
		self.dealerCards = self.dHand.getCards()
	
	#the player is given an option to take a new card or hold.
	#if they bust the game is automatically over
	#calls: drawCard(), seePHand(), testTotal()
	#called by: startGame()
	def playerMove(self):
		#total updated earlier
		if self.pHand.total < 21:
			pChoice = self.ChoiceDrawOrHold()
			if pChoice == 'Draw':
				self.deck = self.pHand.drawCard(self.deck)
				self.updatePlayerCards()
				self.drawACard((len(self.playerCards)-1), "Player")
				self.pHand.updateTotal()
				self.updatePlayerTotalLabel()
				if self.pHand.total > 21:
					return 'gameOver'
				else:
					return 'gameGoing'
			else: #pChoice == 'Hold'
				self.updateInstructions("Dealer's Turn")
				return 'dealerTurn'
		else:
			self.updateInstructions("You have 21. Press Hold: ")
			self.pressHold()
			return 'dealerTurn'
			
	#the dealer takes cards until they go over 16 points 
	#calls: Hand.calcTotal(), drawCard()
	#called by startGame()
	def dealerMove(self):
		self.updateInstructions("Dealer's turn...")
		self.dHand.updateTotal()
		cardNumber = 2
		self.drawACard(cardNumber-1, "Dealer")
		while self.dHand.total < 17:
			cardNumber += 1
			self.dHand.drawCard(self.deck)
			self.dHand.updateTotal()
			self.drawACard(cardNumber-1, "Dealer")
		self.updateInstructions("The dealer has made their move.")
		
	#compares the player and dealer hands and then determines the winner
	#calls: Hand.calcTotal(), seePHand(), seeDHand()
	#called by: startGame()
	def assessHands(self, bet):
		#shows the cards
		self.pHand.updateTotal()
		self.dHand.updateTotal()
		self.updateDealerCards()
		self.updatePlayerTotalLabel()
		self.updateDealerTotalLabel()
		if self.pHand.total > self.dHand.total and self.pHand.total <= 21 or self.dHand.total > 21:
			self.updateInstructions("Player wins! Congrats!")
			return 2*bet
		elif self.pHand.total == self.dHand.total:
			self.updateInstructions("Tie game!")
			return bet
		else:
			self.updateInstructions("House wins! Better luck next time")
			return 0