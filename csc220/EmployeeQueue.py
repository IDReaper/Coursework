# class to implement a queue of Employee objects
class EmployeeQueue:

    # __init__() - default constructor
    # Purpose: initializes items to empty list  
    def __init__(self):
        self.items = []

    # isEmpty() method		
    # Purpose: returns True if queue empty, else False
    # Return Type: bool
    def isEmpty(self):
        return self.items == []

    # enqueue() method		
    # Purpose: adds an object to end of queue
    def enqueue(self, item):
        self.items.append(item)
        
        

    # dequeue() method		
    # Purpose: removes and returns the object at the front of the queue
    # Return Type: Employee
    def dequeue(self):
        return self.items.pop(0)

    # peek() method		
    # Purpose: returns the object at the front of the queue
    # Return Type: Employee
    def peek(self):
        return self.items[0]

    #To help me see what is happening in the list
    def showAll(self):
        return self.items

    # size() method		
    # Purpose: returns the number of items in the queue
    # Return Type: int
    def size(self):
        return len(self.items)

    # __str__() method		
    # Purpose: returns entire contents of the queue formatted as a table
    # Return Type: string
    def __str__(self):
        print "\nEmployee\tHours\tPay Rate\n"
        for item in self.items:
            print item
        return ""
        


