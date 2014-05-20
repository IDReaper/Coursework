from math import *

def sumOdd():
    n = input("Please enter a value for n: ")
    sum = 0

    if n % 2 == 0:
        for i in range(1,n,2):
            sum = sum + i
    else:
        for i in range(1,n+1,2):
            sum = sum + i

    print "sum is", sum

def sumOdd_v2():
    n = input("Please enter a value for n: ")
    sum = 0

    if n % 2 == 0:
        upperLimit = n
    else:
        upperLimit = n + 1

    for i in range(1,upperLimit,2):
        sum = sum + i

    print "sum is", sum

def log_base_2():
    n = input("Please enter a value for n: ")
    number_of_divisions = 0

    while n > 1:
        n = n / 2
        number_of_divisions = number_of_divisions + 1

    print "the number of divisions is", number_of_divisions

def investment_question():
    rate = input("Please enter the APR: ")
    amount = 35
    years = 0

    while amount<=2*35:
        print "current amount = ",amount
        amount = amount + rate/100.0 * amount
        years = years + 1

    print "Your investment will double after", years, "years"

def prime():
    n = input("Please enter a number: ")

    divider = 2

    while divider <= sqrt(n):
        print "divider = ",divider
        remainder = n % divider
        #print remainder
        if remainder == 0:
            print "The number is not prime"
            break
        divider = divider + 1

    if divider>sqrt(n):
        print "The number is a prime"


def number_game_v1():
    total_chances = 5
    chances_so_far = 0
    secret_number = pickOne(100)

    for i in range(total_chances):
        guessed_number = input("Please guess the secret number: ")
        if guessed_number > secret_number:
            print "you guessed higher"
        elif guessed_number < secret_number:
            print "you guessed lower"
        else:
            print "you guessed correctly"
            break
    

    
