from string import *

def phrase2acro():
    phrase = raw_input('Enter a phrase: ')

    acronym = ''
    for word in split(phrase):
        acronym = acronym + word[0]
        

    print acronym
     

    
