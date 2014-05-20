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

def hand_13():
    draw = []
    x = []
    hand = randrange(1,53)
    spades = draw[1:14]
    hearts = draw[14:27]
    clubs = draw[27:40]
    diamonds = draw[40:53]
    n = 0
    z = 0      
    for i in range(13+n):
        n = 0
        hand = randrange(1,53)
        if hand == draw[0:13]:
            n = 1
            draw.remove(hand)
        else:
            x.append(hand)
            draw.append(hand)
            
    print draw

    for ch in draw:
        if i == draw[1:14]:
            print "Spades"
        elif i == draw[14:27]:
            print "Hearts"
        elif i == draw[27:40]:
            print "Clubs"
        elif i == draw[40:53]:
            print "Diamonds"
            
            
            
            
        
            
        
        
