# convert.py
# A program to convert Celsius temps to Fahrenheit
# by: Suzie Programmer
import sys

def convert_celsius():
    print "This program takes the user input value for degrees celcius 5 times and converts these values into degrees fahrenheit."
    x = input("Enter 1 to continue; Enter 0 to exit; Enter 2 to view conversion table: ")
    if x == 1:
        for i in range(5):
            celsius = input("What is the temperature in degrees celsius? ")
            fahrenheit = 9.0 / 5.0 * celsius + 32
            print "The temperature is", fahrenheit, "degrees Fahrenheit."
        print "Session Complete"
        sys.exit()
    elif x == 0:
        sys.exit()
    elif x == 2:
        celsius = 0
        for i in range(11):
            fahrenheit = 9.0 / 5.0 * celsius + 32
            print "C: ", celsius, "F: ", fahrenheit
            celsius = celsius + 10
        convert()
    else:
        print "Invalid input, closing program."
        sys.exit()

def convert_fahrenheit():
    print "This program takes the user input value for degrees fahrenheit 5 times and converts these values into degrees celsius."
    x = input("Enter 1 to continue; Enter 0 to exit; Enter 2 to view conversion table: ")
    if x == 1:
        for i in range(5):
            fahrenheit = input("What is the temperature in degrees fahrenheit? ")
            celsius = (fahrenheit - 32) *  5.0 / 9.0
            print "The temperature is", celsius, "degrees celsius."
        print "Session Complete"
        sys.exit()
    elif x == 0:
        sys.exit()
    elif x == 2:
        fahrenheit = 0
        for i in range(11):
            celsius = (fahrenheit - 32) *  5.0 / 9.0
            print "F: ", fahrenheit, "C: ", celsius 
            fahrenheit = fahrenheit + 10
        convert()
    else:
        print "Invalid input, closing program."
        sys.exit()

# avg2.py
# A simple program to average two exam scores
# Illustrates use of multiple input
def average():
    print "This program computes the average of three exam scores."
    x = input("Enter 1 to continue; Enter 0 to exit: ")
    if x == 1:
        score1, score2, score3 = input("Enter three scores separated by a comma: ")
        average = (score1 + score2 + score3) / 3.0
        print "The average of the scores is:", average
        average()
    elif x == 0:
        sys.exit()
    else:
        print "Invalid input, closing program."
        sys.exit()

# futval.py
# A program to compute the value of an investment
# carried 10 years into the future
# by: John M. Zelle
def main():
    print "This program calculates the future value of a investment over years given by the user."
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annualized interest rate: ")
    years = input("Please enter the time in years: ")
    for i in range(years):
        principal = principal * (1 + apr)
        print "The amount in", years, "years is:", principal
        main()
