'''
Shawn Thompson
CSC 220
Project #1
'''

from Person import *
from Student import *
import os

class tester:

    def __init__(self):
        self.students = []

    def addStudents(self, number):
        for n in range(number):
            
            firstName = raw_input("First name: ") 
            lastName = raw_input("Last name: ")
            credits = input("Credits: ")
            GPA = input("GPA: ")
            
            self.students.append(Student(firstName, lastName, credits, GPA))  

    def showStudents(self):
        self.students.sort()
        for item in self.students:
            print item

    def showGPA(self):     
        print 'work in progress'

Tester = tester()

while True:
    choice = raw_input("Add, Show, or GPA?(0 to quit): ")

    if choice == 'Add':
        number = input("How manny students would you like to add?: ")
        Tester.addStudents(number)

    elif choice == 'Show':
        Tester.showStudents()

    elif choice == 'GPA':
        print 'work in progress'

    elif choice == '0':
        break
        
        

   

    


