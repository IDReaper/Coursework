import string, os
import sys
import time
#Assignment 3
#2bit Binary Counter
#Shawn Thompson
#See Finite state machine

def counter():
    print "In progress"
    inRange = 0
    addCount = 0
    outList = []
    initState = input("Please enter the initial state of the Finite State Machine.[(x,y)]: ")
    print initState
    x = int(initState[0])
    inBinary = input("Enter as input string a 2-bit binary list\n[1,1,0,0,1,0,1,0,1,1,1]\n... ")
    print inBinary
    #inList = inBinary
    for i in inBinary:
         if i == x:
             #outList.append(inList[inRange])
             #outList.append(inBinary[inRange])
             outList.append(addCount)
             inRange = inRange + 1
         else:
             #addCount = addCount + inList[inRange]
             addCount = addCount + inBinary[inRange]
             outList.append(addCount)
             inRange = inRange + 1
    
            
    outVal(inBinary,outList) 


def outVal(inPut,outPut):
    print "In progress"
    print "Input:  ",inPut
    print "Output: ",outPut


def counter2nd():
    print "In progress"
    inRange = 0
    addCount = 0
    outList = []
    initState = raw_input("Please enter the initial state of the Finite State Machine.[(x,y)]: ")
    print initState
    state = string.split(initState,',')
    x = state[0]
    y = state[1]
    inBinary = input("Enter as input string a 2-bit binary list\n[1,1,0,0,1,0,1,0,1,1,1]\n... ")
    print inBinary
    #inList = inBinary
    for i in inBinary:
        if i == 0:
            #outList.append(inList[inRange])
            outList.append(inBinary[inRange])
            inRange = inRange + 1
        else:
            #addCount = addCount + inList[inRange]
            addCount = addCount + inBinary[inRange]
            outList.append(addCount)
            inRange = inRange + 1
    outVal(inBinary,outList,x,y)
    #for i in outList:
        #if x == 0:
            #outList = [i]
            #i = i + 1
        #else:
            #outList = [i + 1]
            #i = i +1
    
#def outVal(inPut,outPut,x,y):
    #print "In progress" 
    #print inPut
    
    #print outPut

def sq(x):
    y = x*x
    return y

