# change.py
# A program to calculate the value of some change in dollars
def main():
    print "Change Counter"
    print
    print "Please enter the count of each coin type."
    quarters = input("Quarters: ")
    dimes = input("Dimes: ")
    nickels = input("Nickels: ")
    pennies = input("Pennies: ")
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print
    print "The total value of your change is", total
    
def main2():
    print "Change Organizer"
    print
    print "Please enter the total money value."
    value = input("Total money value: ")
    quarters = int(value*100)/25
    rQ = int(value*100)%25
    print quarters
    dimes = rQ/10
    rD = rQ%10
    print dimes
    nickels = rD/5
    rN = rD%5
    print nickels
    pennies = rN/1
    print pennies
    
