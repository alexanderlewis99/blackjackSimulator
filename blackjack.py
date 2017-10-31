from random import randrange
from hand import Hand

#creates a deck of card as a list from 1 to 52
#called by: main()
def buildDeck():
	newDeck = []
	for i in range(1, 13+1):
		newDeck.append([i, "Clubs"])
	for i in range(1, 13+1):
		newDeck.append([i, "Diamonds"])
	for i in range(1, 13+1):
		newDeck.append([i, "Spades"])
	for i in range(1, 13+1):
		newDeck.append([i, "Hearts"])
	return newDeck

#called by drawCard()
#retrieves a random card from the deck and returns it
def getRandCard(deck):
	newCard = deck.pop(randrange(0, (len(deck))))
	return newCard, deck

#the player is given an option to take a new card or hold.
#if they bust the game is automatically over
#calls: drawCard(), seePHand(), testTotal()
#called by: startGame()
def playerMove(pHand, deck):
	#total updated earlier
	if pHand.total < 21:
		pChoice = input("Enter ‘Y’ for another card or ‘H’ to hold: ")
		if pChoice == 'Y' or pChoice == 'y' or pChoice == 'yes' or pChoice == 'Yes':
			deck = pHand.drawCard(deck)
			pHand.seePHand() #updates total
			if pHand.total > 21:
				return 'gameOver'
			else:
				return 'gameGoing'
		else: #pChoice == 'H' or pChoice == 'h' or pChoice == 'hold' or pChoice == 'Hold':
			return 'dealerTurn'
	else:
		pChoice = input("You have 21. Enter ‘H’ to hold: ")
		return 'dealerTurn'

#the dealer takes cards until they go over 16 points 
#calls: Hand.calcTotal(), drawCard()
#called by startGame()
def dealerMove(dHand, deck):
	print()
	print("Dealer's turn...")
	dHand.updateTotal()
	while dHand.total < 17:
		dHand.drawCard(deck)
		dHand.updateTotal()
	print("The dealer has made their move.")
	return dHand, deck

#compares the player and dealer hands and then determines the winner
#calls: Hand.calcTotal(), seePHand(), seeDHand()
#called by: startGame()
def assessHands(pHand, dHand, bet):
	print()
	#shows the cards
	print("The Reveal:")
	pHand.seePHand() #updates total
	dHand.seeDHand() #updates total
	#tests who wins
	if pHand.total > dHand.total and pHand.total <= 21 or dHand.total > 21:
		print("Player wins! Congrats!")
		return bet
	elif pHand.total == dHand.total:
		print("Tie game!")
		return 0
	else:
		print("House wins! Better luck next time")
		return -1*bet

#runs the game: determines whose turn is it and if the player busts
#starts off with the player and then the computer goes and then they're hands are compared
#calls: playerMove(), dealerMove(), assessHands()
#called by: main()

#introduction banner
#called by: main()
def startBanner():
	print("============================== blackjack.py v. 2.0 =============================")
	print("--------------------------------- by Alec Wang ---------------------------------")

#banner that exits the game
#called by: main()
def exitBanner():
	print("================================================================================")

#sets up the game and starts it
def main():
	startBanner()
	money = 10
	gameNum = 1
	gameRunning = True
	print("Your money: $", str(money))
	while gameRunning == True:
		pHand = []
		dHand = []
		deck = buildDeck()
		
		#takes four cards from the deck and gives two to each player
		pHand = Hand(deck)
		dHand = Hand(deck)
		print("----------------------------------- Round", gameNum, "------------------------------------")
		pHand.seePHand()
		dHand.seeDCard()
		print()
		
		#starts the game
		turn = 'player'
		turnNum = 0
		#player bets money
		ibet = -1
		while(ibet == -1):
			bet = int(input("How much would you like to bet?: "))
			if bet < 0:
				print("You can't bet negative money.")
			elif bet > money and money > 0:
				print("I'm sorry. You don't have that much money.")
			elif money <= 0 and bet > 5:
				print("You can only take out loans less than 5 dollars.")				
			else:
				ibet = bet
		#player's turn
		while turn == 'player':
			moveResult = playerMove(pHand, deck)
			if moveResult == 'gameOver':
				print("You busted!")
				turn = 'none'
			elif moveResult == 'dealerTurn':
				turn = 'computer'
			#else - if moveResult == 'gameGoing', nothing happens, the loop keeps running
		#computer's turn
		if turn == 'computer':
			dHand, deck = dealerMove(dHand, deck)
		#winner determined
		roundOutcome = assessHands(pHand, dHand, bet)
		
		#end of game; sees if player wants to continue
		money += roundOutcome
		print("Your money: $", str(money))
		print()
		print("Would you like to play again?")
		playAgain = input("Enter 'Y' for yes, 'N' for no: ")
		if not(playAgain == 'Y' or playAgain == 'y' or playAgain == 'yes' or playAgain == 'Yes'):
			gameRunning = False
		else:
			gameNum += 1
	print("Final money: $", str(money))
	exitBanner()

if __name__ == "__main__":
	main()