from random import *

def this():
    inventory = []
    myLvl = 1
    while True:
            x = randrange(1,10)
            y = randrange(10,21)
            l = randrange(x,y)
            print "A level", l, "enemy has appeared."
            choice = input("What will you do?(1=Atk, 2=Def, 3=Run, 4=Inv): ")
            

def dieThrow():
    x = randrange(1,7)
    print "You threw", x,"."



def giveHand():
    #Lists for Deck/Hand
    deck = range(1,53)
    hand = []
    #Remove/Append from lists
    for i in range(13):
        num = choice(deck)
        deck.remove(num)
        hand.append(num)
    #Print the hand        
    for n in hand:
        #print n
        getCard(n)
    


    

def getCard(number):
    #Determine suits
    if 1<=number<=13:
        position = number
        suit = "Spades"
    elif 14<=number<=26:
        position = number - 13
        suit = "Hearts"
    elif 27<=number<=39:
        position = number - 26
        suit = "Clubs"
    else:
        position = number - 39
        suit = "Diamonds"

    #Determine Rank
    #if position =
    if 1<=position<=4: 
        intRank = ['','Ace','King','Queen','Jack']
        rank = intRank[position]
    else:
        #15 used to get corrosponding face number
        rank = 15 - position

    print str(rank) + " of " + suit
            
            
            
            
        
            
        
        
