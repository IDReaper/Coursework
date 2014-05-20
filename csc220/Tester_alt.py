from EmployeeQueue import *
from Person import *
from Employee import *

def peek(peekObj):
    print "Peeking..."
    translate = peekObj.peek()
    print translate.__str__()
    
def enqueue(enqueueObj):
    
    firstName = raw_input("Please enter first name: ")
    lastName = raw_input("Please enter last name: ")
    hoursPerWeek = input("Please enter hours per week: ")
    payRate = input("Please enter pay rate: ")
    #item = raw_input("Please enter item to enqueue: ")
    newEmp = Employee(firstName, lastName, hoursPerWeek, payRate)
    print "Enqueue in progress..."
    enqueueObj.enqueue(newEmp)
    #enqueueObj = newEmp

def dequeue(dequeueObj):
    print "Dequeue in progress..."
    dequeueObj.dequeue()
    
def runTest():
    emp = EmployeeQueue()
    
    if emp.isEmpty == False:
        emp.dequeue()
    emp.showAll()
    
    while True:
        startOp = raw_input("Would you like to preform a queue operation?(y/n): ")
        if startOp == "y":
            selectOp = raw_input("Please select an operation(peek, enqueue, dequeue, stop): ")
            if selectOp == "peek":
                #print "WIP"
                #Choosable instance?
                peek(emp)
                
            elif selectOp == "enqueue":
                #print "WIP"
                enqueue(emp)
                
            elif selectOp == "dequeue":
                #print "WIP"
                dequeue(emp)

            elif selectOp == "q":
                break
                    
            else:
                print "Unrecognized operation..."
            print emp.size()
            print emp.showAll()
            
        elif startOp == "n":
            print emp.__str__()
            print "Ending program..."
            break
        
        else:
            print "Unrecognized operation..."

runTest()
                
                
                
