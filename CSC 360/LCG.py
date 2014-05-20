from visual import *
import string, os
from random import *
import time

#Linear Congruential Generator
#pg. 84-86
#Generate random numbers within [0,1]
#z0 = seed value  (begins at this number)
#Hull-Dobell Theorem
#All nums disticnt if:
#   (a,c) = 1 i.e. relatively prime
#   Any prime number dividing m must divide a-1
#   If 4 divides m, 4 must 
addList = []
dist = "Random numbers are distinct."


a, c, m, z0 = input("Enter 4 comma seperated numbers for values a, c ,m ,z0: ")
print "\n\nStarting LCG...\n\n"
time.sleep(.5)
for i in range(m):
    z = (a*z0+c)%m
    u = z0/float(m)
    print "%.3f "%u
    addList.append(u)
    z0 = z
    time.sleep(.1)
print "\n\nLCG Complete. Getting count in list...\n\n"
time.sleep(.5)
for ch in addList:
    x = addList.count(ch)
    if x == 1:
        print "%5.3f, %u"%(ch, x)
        time.sleep(.1)
    else:
        #print ch, x
        print "%5.3f, %u"%(ch, x)
        dist = "Random numbers not disticnt, check values."
        addList.remove(ch)

print dist
    
