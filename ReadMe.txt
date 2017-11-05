ReadMe

This program is designed to simulate games of blackjack (also known as twenty-one) against a single dealer from a standard deck of 52 cards.

I) How to run
        0.	This program runs on Python 3.6.1. If you have not installed this version, install it from here: 
https://www.python.org/downloads/
	1.	Place the program folder blackjackSimulator on your desktop 
	2.	Open Terminal or other Unix platform. 
	3.	Enter into the command line: 	cd Desktop/blackjackSimulator 
	4.	Enter into the command line:	python blackjack.py 

II) Using the program
Gameplay:
	1.	Both the user and house start off with two cards, with one hidden to the other user 
	2.	The user makes a bet against the house by entering a value. 
	3.	The user goes first and have two options: 
	1.	They can take a card by entering ‘Y’ 
	2.	They can play with their current hand by entering ‘H’ 
If the user goes over 21 points, they automatically lose.
	4.	After the user holds, the dealer takes cards until their above 16 total points. 
	5.	The two hands are then compared and the user with the highest hand less than or equal to 21 points wins. 
Game rules to note:
	1.	The number of points for each card is attributed to their value, except for face cards. All face cards count as 10 points, except for the ace which counts as 1 or 11 depending on the other cards in hand. 
	2.	The user starts off with $10 and cannot bet more than they currently have. 
	3.	However, if the user’s total money reaches or drops below $0, they can take out $5 as a “loan” to bet with. 

III) Program Design
blackjack.py:	runs the gameplay by keeping track of turns, determining the winner, and accounting for 
the user’s bets and money.
hand.py:	contains the code for the hand object created in blackjack.py, keeps track of the cards in 
hand and the number of points each hand contains, and draws card from the deck.

The code in this program is intended for educational use and is not intended for the promotion of gambling, underage or otherwise. Any attempt to profit from this code without explicit permission from the author is a violation of the usage agreement.

Acknowledges: I’d like to thank Professor Blake Howald for his fun classes and his suggestions to the program, my roommate Pierce McDonnell for beta-testing the game, Carleton College for the incredible learning environment it provides, and John M. Zelle for his instructive book Python Programming: An Introduction to Computer Science.

Sincerely,
A.L.E. Wang
Contact Email: alewang99@gmail.com
Github: https://github.com/alexanderlewis99
Last Updated: October 28, 2017
