from string import *
import os
import time

def dot():
    setLEDBack(1)
    wait(5)
    setLEDBack(0)
    #wait(1)

def dash():
    setLEDBack(1)
    wait(15)
    setLEDBack(0)
    #wait(1)

def pause():
    setLEDBack(0)
    wait(5)

def gap():
    setLEDBack(0)
    wait(15)

def char2morsecode(x):
    line = {'e':".",'t':"-",'s':"...",'u':"..-",'r':".-.",'w':".--",'d':"-..",'k':"-.-",'g':"--.",'o':"---",
             'h':"....",'v':"...-",'f':"..-.",'l':".-..",'p':".--.",'j':".---",'b':"-...",'x':"-..-",'c':"-.-.",
             'y':"-.--",'z':"--..",'q':"--.-",' ':"   ",'i':"..",'a':".-",'n':"-.",'m':"--"}
    morse = ''
    space = ' '
    for ch in x:
        morse = morse + line[ch]+ space
    print morse
    morsecode2LEDlight(morse)
    
def morsecode2LEDlight(y):
    space = ' '
    gap = '     '
    for ch in y:
        if ch == '.':
            dot()
            pause()
        elif ch == '-':
            dash()
            pause()            
        else:
            gap()
            print 
            
def send():
    z = raw_input("Enter message: ")
    char2morsecode(z)
        
        
    
    
    
    
    
def encoder():
    print "This program will take a message from user input and translate the message into morse code, which willthen be transmitted using a LED.\n\n"
    line = {'e':".",'t':"-",'s':"...",'u':"..-",'r':".-.",'w':".--",'d':"-..",'k':"-.-",'g':"--.",'o':"---",
             'h':"....",'v':"...-",'f':"..-.",'l':".-..",'p':".--.",'j':".---",'b':"-...",'x':"-..-",'c':"-.-.",
             'y':"-.--",'z':"--..",'q':"--.-",' ':"   ",'i':"..",'a':".-",'n':"-.",'m':"--"}    
    morse = ""
    space = "|"
    message = raw_input("Please enter the message you would like to encode.\n")   
    for ch in message:        
        morse = morse + line[ch] + space
    print morse
    

def decoder():
    print "This program will will take morse code as an input and output the corresonding message."
    line = {'.':"e",'-':"t",'...':"s",'..-':"u",'.-.':"r",'.--':"w",'-..':"d",'-.-':"k",'--.':"g",'---':"o",
             '....':"h",'...-':"v",'..-.':"f",'.-..':"l",'.--.':"p",'.---':"j",'-...':"b",'-..-':"x",'-.-.':"c",
             '-.--':"y",'--..':"z",'--.-':"q",'..':"i",'.-':"a",'-.':"n",'--':"m",'   ':" "}    
    chars = ""
    morse = ""
    space = "   "
    message = raw_input("Please enter the message you would like to decode.\n")   
    for ch in message: 
        if ch != '|':
            morse = morse+ch
        elif ch == '|':
            chars = chars + line[morse] 
            morse = ""
        else: 
            print space
            morse = ""       
    print chars
    

    

    

######################################################################3
def shift(ch):
    #plain text
    
    if ch == 'z':
        coded_ch = 'a'
    else:
        next_ascii_num = ord(ch) + 1
        coded_ch = chr(next_ascii_num)
    return coded_ch

def rev_shift(ch):
    #plain text
    
    if ch == 'z':
        coded_ch = 'a'
    else:
        next_ascii_num = ord(ch) - 1
        coded_ch = chr(next_ascii_num)
    return coded_ch

def main():
    #x = input("Enter range: ")
    
    plaintext = raw_input("Enter string: ")
    ciphertext = ""   
    for ch in plaintext:
        #y = shift(ch)
        #for i in range(x):
        ciphertext = ciphertext + shift(shift(y))
    print ciphertext

def main2():
    plaintext = raw_input("Enter string: ")
    ciphertext = ""
    for ch in plaintext:
        ciphertext = ciphertext + rev_shift(rev_shift(ch))
    print ciphertext
    
        
        
