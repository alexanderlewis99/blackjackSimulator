from graphics import *

class GUICard:
    def __init__(self, GraphWin, rank, suit, rxCoord, playerOrDealerTest):
        self.GraphWin = GraphWin
        self.rank = rank
        self.suit = suit
        self.pieces = [] #appends pieces to systematically delete them later
        self.coords = [[rxCoord - 60, 50], [rxCoord, 50], [rxCoord, 130], [rxCoord - 60, 130]]
        if playerOrDealerTest == "Dealer": #increases the y value for the dealer's cards to make them appear higher
        	for point in self.coords:
	        	point[1] += 100

    def drawSelf(self):         
        self.buildCard()
        self.buildMarker()

    def buildCard(self):
        points = [Point(self.coords[0][0], self.coords[0][1]), Point(self.coords[1][0], self.coords[1][1]),
                  Point(self.coords[3][0], self.coords[3][1]), Point(self.coords[2][0], self.coords[2][1])]
        cardGUI = Polygon(points[0], points[1], points[3], points[2])
        cardGUI.setFill("white")
        cardGUI.setOutline("black")
        cardGUI.draw(self.GraphWin)
        self.pieces.append(cardGUI)

    def buildMarker(self): #draws markers on the card according to their rank
        if not self.rank in ("Ace", "Jack", "Queen", "King"):
            if self.rank in (2, 8, 10):
                self.marker(self.coords[0][0]+30, self.coords[0][1]+30)
                self.marker(self.coords[0][0]+30, self.coords[0][1]+30+20)
            if self.rank == 3:
                for i in range(3):
                    self.marker(self.coords[0][0]+30, self.coords[0][1]+20+20*i)
            if self.rank in (4, 5):
                for i in range(2):
                    self.marker(self.coords[0][0]+10+i*40, self.coords[0][1]+10)
                    self.marker(self.coords[0][0]+10+i*40, self.coords[0][1]+70)
            if self.rank in (5, 7, 9):
                self.marker(self.coords[0][0]+30, self.coords[0][1]+40)
            if self.rank in (6, 7, 8):
                for i in range(3):
                    self.marker(self.coords[0][0]+10, self.coords[0][1]+15+i*25)
                    self.marker(self.coords[0][0]+10+40, self.coords[0][1]+15+i*25)
            if self.rank in (9, 10):
                for i in range(4):
                    self.marker(self.coords[0][0]+10, self.coords[0][1]+10+i*20)
                    self.marker(self.coords[0][0]+10+40, self.coords[0][1]+10+i*20)
        else:
            royalLabel = Text(Point(self.coords[0][0]+30, self.coords[0][1]+40), str(self.rank))
            self.marker(self.coords[0][0]+30, self.coords[0][1]+50)
            royalLabel.setSize(36)
            royalLabel.draw(self.GraphWin)
            self.pieces.append(royalLabel)
        
    #creates the symbols on the cards (Diamonds, Hearts, Clubs, Spades)
    def marker(self, centerx, centery):
        if self.suit == "Diamonds": #creates a diamond symbol
            bP = Point(centerx, centery - 6)
            uP = Point(centerx, centery + 6)
            lP = Point(centerx - 4, centery)
            rP = Point(centerx + 4, centery)
            diamond = Polygon(lP, uP, rP, bP)
            diamond.setFill("red")
            diamond.draw(self.GraphWin)
            self.pieces.append(diamond)
        elif self.suit == "Hearts": #creates a heart symbol
            for i in range(2):
                valve = Circle(Point(centerx + 1.8 + i*-3.6, centery), 2)
                valve.setFill("Red")
                valve.setOutline("Red")
                valve.draw(self.GraphWin)
                self.pieces.append(valve)
            triangeBottom = Polygon(Point(centerx - 4.12, centery), Point(centerx + 4.12, centery), Point(centerx, centery - 5))
            triangeBottom.setFill("Red")
            triangeBottom.setOutline("Red")
            triangeBottom.draw(self.GraphWin)
            self.pieces.append(triangeBottom)
        elif self.suit == "Clubs": #creates a clover/clubs symbol
            for i in range(2):
                cloverLeaf = Circle(Point(centerx + 2 + i*-4, centery + 1), 2)
                cloverLeaf.setFill("Black")
                cloverLeaf.draw(self.GraphWin)
                self.pieces.append(cloverLeaf)
            cloverLeaf2 = Circle(Point(centerx, centery + 4), 2)
            cloverLeaf2.setFill("Black")
            cloverLeaf2.draw(self.GraphWin)
            cloverStem = Line(Point(centerx, centery+5), Point(centerx, centery-3))
            cloverStem.draw(self.GraphWin)
            self.pieces.append(cloverLeaf2)
            self.pieces.append(cloverStem)
        else: #self.suit == "Spades": #creates a spade symbol
            for i in range(2):
                spadeLeaf = Circle(Point(centerx + 1 + i*-2, centery + 1), 2)
                spadeLeaf.setFill("Black")
                spadeLeaf.draw(self.GraphWin)
                self.pieces.append(spadeLeaf)
            triangeCenter = Polygon(Point(centerx + 3, centery + 1), Point(centerx - 3, centery + 1), Point(centerx, centery + 5))
            triangeCenter.setFill("Black")
            triangeCenter.draw(self.GraphWin)
            triangeBottom = Polygon(Point(centerx, centery - 1), Point(centerx - 1, centery - 2), Point(centerx + 1, centery - 2))
            triangeBottom.setFill("Black")
            triangeBottom.draw(self.GraphWin)
            self.pieces.append(triangeCenter)
            self.pieces.append(triangeBottom)
    
    #deletes the pieces of the cards
    def undrawSelf(self):
    	for i in range(len(self.pieces)):
    		self.pieces[i].undraw()