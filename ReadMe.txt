ReadMe

This program is designed to simulate games of blackjack (also known as twenty-one) against a single dealer from a standard deck of 52 cards.

I) How to run
        This program runs on Python 3.6.1. If you have not installed this version, install it from here: 
https://www.python.org/downloads/
	
	To run through terminal on Macs:
		1.	Place the program folder ‘blackjackSimulator’ on your desktop 
	
		2.	Open Terminal on Mac. 
		3.	Enter into the command line: 	cd Desktop/blackjackSimulator 
		4.	Enter into the command line:	python blackjack.py

	Or run on IDLE on PC or Mac:
		1.	Open the file in IDLE

		2.	Go to: Run -> Run Module in the menu bar 

II) Using the program
Gameplay:
	1.	Both the user and house start off with two cards, with one hidden to the other user
		The user starts off with 10 “money” to bet with. 
	2.	The user enters how much money they want to bet against the house and clicks the ‘Bet’ button. 
	3.	The user then has two options: 
		A.	They can take a card by clicking the ‘Draw Card’ button.
			But if the user goes over 21 points, they automatically lose. 
		B.	Or they can play their current hand by clicking the ‘Hold’ button

	4.	After the user clicks ‘Hold’, the dealer takes cards until their total points is above 16. 
	5.	The two hands are then compared and the user with the highest hand less than or equal to 21 points wins. 
Game rules to note:
	1.	The number of points for each card is attributed to their value, except for face cards. All face cards count as 10 points, except for the ace which counts as 1 or 11 depending on the other cards in the hand (i.e. an ace with two face cards would be worth 1 point because if it was worth 11, the player would be over 21: 11 + 10 + 10 = 31 while 1 + 10 + 10 = 21) 
	2.	The user starts off with $10 and cannot bet more than they currently have. 
	3.	However, if the user’s total money reaches or drops below $0, they can take out $5 as a “loan” to bet with.

III) Program Design
blackjack.py:	runs unit tests and creates the GUI interface object.
interface.py	runs the gameplay by creating the interface
		enables user-interface interaction
		keeps track of turns
		makes the dealer take cards
		determines the winner of each round
		accounts for the user’s bets and money.
hand.py:	contains the code for the hand object created in interface.py
		It keeps track of the cards in  hand, draws card from the deck, and calculates the total points.
visualCard.py	Creates the rectangles and diamond, heart, club and spade icons that make up the cards.
button.py:	the code to make the buttons in the game.
		It was created by John M. Zelle and modified by me.
graphics.py:	a graphics library created by John M. Zelle that enables most of the GUI functionality.

The code in this program is intended for educational use and is not intended for the promotion of gambling, underage or otherwise. Any attempt to profit from this code without explicit permission from the author is a violation of the usage agreement.

Acknowledges: I’d like to thank Professor Blake Howald for his fun classes and his suggestions to the program, my roommate Pierce McDonnell for beta-testing the game, Carleton College for the incredible learning environment it provides, and John M. Zelle for his instructive book Python Programming: An Introduction to Computer Science.

Sincerely,
A.L.E. Wang
Contact Email: alewang99@gmail.com
Github: https://github.com/alexanderlewis99
Last Updated: November 14, 2017
