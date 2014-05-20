# BTTester program

from BinaryTree import *

# main tester function
def main():
    # create an empty binary tree
    btree = BinaryTree()

    add = raw_input("Add an employee to the tree? >>")
    if add == 'yes' or add == 'y':
        firstName = raw_input("Please enter first name: ")
        lastName = raw_input("Please enter last name: ")
        hoursPerWeek = input("Please enter hours per week: ")
        payRate = input("Please enter pay rate: ")
        employee = Employee(firstName, lastName, hoursPerWeek, payRate)

        if btree.isEmpty == True:
            btree.setRootVal(employee)
            print firstName, "set as root."
        else:
                
            
        
        
        


    



    
