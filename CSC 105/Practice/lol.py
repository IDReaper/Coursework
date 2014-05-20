from random import *

def lol():
    loop = 1
    cash = 2000
    while loop == 1:
        x = randrange(0,101)
        y = randrange(0,101)
        z = randrange(0,101)
        bets = raw_input("Bet on either x,y or z: ")
        print "Cash:",cash
        bet_cash = input("Play your bet: ")
        cash = cash - bet_cash
        print "Cash:",cash
        ready = raw_input("Ready? y/n: ")
        if ready == 'y':
            if bets == 'x':
                if x > y and x > z:
                    print "You have won!"
                    cash = cash+(bet_cash*2)
                    print "You now have",cash,"cash."
                else:
                    print "You have lost"  
                    
            if bets == 'y':
                if y > x and y > z:
                    print "You have won!"
                    cash = cash+(bet_cash*2)
                    print "You now have",cash,"cash."  
                else:
                    print "You have lost"
                            
            if bets == 'z':
                if z > x and z > y:
                    print "You have won!"
                    cash = cash+(bet_cash*2)
                    print "You now have",cash,"cash."     
                else:
                    print "You have lost"
                
            if cash <= 0:
                print "You have lost all your money!"
                break
            elif cash >= 10000:
                print "You have emptied out all the competitors! Congratulations!"
                break
            again = raw_input("Continue? y/n: ")
            if again == 'n':
                print "You have won",cash,"cash."
                print "Thanks for playing."
                break
                
        
    
    
        
