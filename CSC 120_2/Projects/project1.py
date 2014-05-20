#project1.py
#F5 to run, save with .py extension

def simpleCommands():
    print "WORLD! HELLO!"
    print "How is it going?"
    print "NO YOU!"
    print "Hmmm..."
    print "Madness?"
    
#Shell history is 'alt-p' and 'alt-n'
#The shell can also be used as a calculator

def calc():
    x = 3.0/0.5
    y = 2+3+4*2-10
    print x
    print y

#The former program is also an example of setting variables
#Here is one more example

def varSet():
    w = 20
    h = 15
    #l = 12
    print w * h
    print "Width * Height"

#The above program can also be modified to find volume
#So far we have been using function definitions
#Here is another simple example including a for loop

def me(x):
    for i in range(x):
        print "Your doing it!"

#This definition has a parameter which controls the for loop
#Run this program then type 'me(3)' in the shell and see what happens

def me2():
    x = input("Vegeta, what does your scouter say about his power level?")
    for i in range(x):
        print "IT'S OVER 9000!!!!!!!"

#This definition uses x as a user input value
#When run, the program will take input from the user and store it for use in the loop.


    


    
    

    

