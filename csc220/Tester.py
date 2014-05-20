from EmployeeQueue import *
from Person import *
from Employee import *

class Tester(self):

    def __init__(self):
        self.itemStore == []

    def promptQueue(self):
        startOp = raw_input("Would you like to preform a queue operation?(y/n): ")
        if startOp == "y":
            selectOp = raw_input("Please select an operation(peek, enqueue, dequeue): ")
            if selectOp == "peek":
                return peekOp
                

            elif selectOp == "enqueue":
                queueObject = raw_input("Please enter object to enqueue: ")
                self.itemStore.append(queueObject)
                return enqueueOp
                

            elif selectOp == "dequeue":
                return dequeueOp

            else:
                return "Unrecognized operation..."    

emp = EmployeeQueue()
myTest = Tester()

if emp.isEmpty == False:
    emp.dequeue()
emp.showAll()

myTest.promptQueue()


        
        
'''
class Tester:

    def __init__(self):
        self.emp = EmployeeQueue()
        print "emp = employeeQueue"
        if self.emp.isEmpty == False:
            print "If emp is not empty, dequeue"
            self.emp.dequeue()
            print "Dequeue complete"
        else:
            print "nothing to dequeue"
            self.emp.showAll()

        self.name = name
        self.name = EmployeeQueue()
        self.name.dequeue()
        self.name.isEmpty()
        '''
