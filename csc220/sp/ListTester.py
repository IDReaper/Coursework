'''
Shawn Thompson
CSC 220
Project #1
'''
from Person import *        #Import both the Person and Employee classes
from Employee import *

class tester:

    def __init__(self):
        print "W.I.P."
        self.eList = []

    def ListTester(self):           
        print "W.I.P."
        numEmployee = input("Enter the number of employees: ")  
        return numEmployee
        
    def storeEmployees(self, numEmployee):
        print "W.I.P."
        for n in range(numEmployee):
            
            firstName = raw_input("First name: ") #Get user input for employee data
            lastName = raw_input("Last name: ")
            hoursPerWeek = input("Hours per week: ")
            payRate = input("Pay rate: ")
            
            self.eList.append(Employee(firstName, lastName, hoursPerWeek, payRate)) #Append to list
        
    def displayEmployees(self): #Displays the employee data
        print "W.I.P." 
        self.eList.sort()
        for item in self.eList:
            print item  

    def avgPay(self):
        print "W.I.P."
        #Return the average pay rate for all employees
        
x = tester()
y = x.ListTester()
x.storeEmployees(y)
x.displayEmployees()

        
        
        
        
