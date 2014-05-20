'''
Shawn Thompson
CSC 220
Project #1    *** Grade: 77 (improve and resubmit by midnight, Friday, 18) ***
'''

from Student import *
import os

#*** methods need comments (-5) ***
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
        print "Student Name" + "\t" + "Credits" + "\t" + "GPA"
        for item in self.students:
            print item

    def showGPA(self):
        counter = 0
        sumGpa = 0
        avgGpa = 0
        for item in self.students:
            counter = counter + 1
            sumGpa = sumGpa + item.getGpa()
        avgGpa = sumGpa / counter
                return avgGpa
#*** counter, sumGPA, and avgGPA should just be local variables, not instance variables (-3) ***
            
Tester = tester()

while True:
    choice = raw_input("Add, Show, or GPA?(0 to quit): ")

    if choice == 'Add':
        number = input("How manny students would you like to add?: ")
        Tester.addStudents(number)

    elif choice == 'Show':
        Tester.showStudents()

    elif choice == 'GPA':
        Tester.showGPA()
        
    elif choice == '0':
        break

    else:
        print "Unrecognized Command"
        
 #*** equality test missing (-10) ***       

   

    


