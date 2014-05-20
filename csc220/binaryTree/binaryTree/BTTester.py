# BTTester program

from BinaryTree import *

# main tester function
def main():
    # create an empty binary tree
    btree = BinaryTree()
    addEmployee(btree)
    
    if btree.root:
        print "Preorder\n"
        Preorder = btree.root.strPreorder()
        print "Inorder\n"
        Inorder = btree.root.strInorder()
        print "Postorder\n"
        Postorder = btree.root.strPostorder()

def addEmployee(btree):
    
    add = raw_input("Add an employee to the tree? >>")
    if add == 'yes' or add == 'y':
        firstName = raw_input("Please enter first name: ")
        lastName = raw_input("Please enter last name: ")
        hoursPerWeek = input("Please enter hours per week: ")
        payRate = input("Please enter pay rate: ")
        employee = Employee(firstName, lastName, hoursPerWeek, payRate)        

        if btree.isEmpty == True:
            btree.setRoot(employee)
            print firstName, "set as root."
        else:
            lrChoice = raw_input("Left or Right child?(l/r): ")
            if lrChoice == 'l':
                btree.insertLeft(employee)

            elif lrChoice == 'r':
                btree.insertRight(employee)
            
