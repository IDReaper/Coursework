from random import randrange
from opencv.cv import *

def stuff():
    x = input("Enter the number of rounds: ")
    y = raw_input("Bet on a, b or c: ")
    a, b, c = 10, 20, 5
    z = 0
    d = 0
    d != z
    for i in range(x):
        n = randrange(0,2,1)
        d = randrange(0,1,1)
        if n == 0:
            z = c
            if d == 0:
                d = b
            else:
                d = a                

        elif n == 1:
            z = b
            if d == 0:
                d = a
            else:
                d = c

        else:
            z = a
            if d == 0:
                d = b
            else:
                d = c

        

        
            
        
                
            
        
    
