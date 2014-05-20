from string import*
import time

def dot():
    setLEDBack(1)
    wait(1)
    setLEDBack(0)

def dash():
    setLEDBack(1)
    wait(3)
    setLEDBack(0)


def encoder():
    #USE DICTIONARY FORMAT i.e. x = {'20':'.',''30':'..-'}
    #morse = morse + x['ord(ch)']
    #
    #
    #Example
    #s1 = replace(s,'bye','night')
    #or
    #morse = replace(message,'s','line3[0:3])
    #^^
    print "This program will take a message from user input and translate the message into morse code, which willthen be transmitted using a LED."
    space = " "
    line = {'e':".",'t':"-",'s':"...",'u':"..-",'r':".-.",'w':".--",'d':"-..",'k':"-.-",'g':"--.",'o':"---",
             'h':"....",'v':"...-",'f':"..-.",'l':".-..",'p':".--.",'j':".---",'b':"-...",'x':"-..-",'c':"-.-.",
             'y':"-.--",'z':"--..",'q':"--.-",' ':"   ",'i':"..",'a':".-",'n':"-.",'m':"--"}
    #E,T
    #line2 = {'i':"..",'a':".-",'n':"-.",'m':"--"}
    #I,A,N,M
    #line3 = {'s':"...",'u':"..-",'r':".-.",'w':".--",'d':"-..",'k':"-.-",'g':"--.",'o':"---"}
    #S,U,R,W,D,K,G,O
    #line4 = {'h':"....",'v':"...-",'f':"..-.",'l':".-..",'p':".--.",'j':".---",'b':"-...",'x':"-..-",'c':"-.-.",'y':"-.--",'z':"--..",'q':"--.-"}
    #H,V,F,L,P,J,B,X,C,Y,Z,Q

    morse = ""
    message = raw_input("Please enter the message you would like to encode.")   
    for ch in message:
        #ord(ch) 
        print ch
        #x = 0
        
        time.sleep(.5)
        #if ch == 'e':
            #morse = morse + replace(message, ch ,line1[0]), space
        morse = morse + line[ch] + space
        #else:
            #morse = morse + replace(message, ch ,line1[1]), space
            #morse = morse + line1[ord_loc], space
    print morse

    

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
    
        
        
