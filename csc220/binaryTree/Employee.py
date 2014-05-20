# Class to implement the Employee ADT as a subclass of Person
from Person import *

class Employee(Person):

    # objects of class Employee have four instance variables:
    # firstName - a string, inherited from Person
    # lastName - a string, inherited from Person
    # hoursWorked - an int
    # payRate - a float

    # Empoyee() - default constructor
    # Purpose: initializes instance variables of new Employee object
    #   with default values
    def __init__(self):
        Person.__init__(self)
        self.hoursPerWeek = 0
        self.payRate = 0

    # Employee(string, string, int, float) - constructor with parameters
    # Purpose: initializes instance variables of new Employee object with
    #   parameter values
    def __init__(self, firstName, lastName, hoursPerWeek, payRate):                     
        Person.__init__(self, firstName, lastName)
        self.hoursPerWeek = int(hoursPerWeek)
        self.payRate = float(payRate)

    # Accessor Methods
	
    # getHoursWorked() method		
    # Purpose: returns the number of hours
    # Return Type: int
    def getHoursPerWeek(self):                                                      
        return self.hoursPerWeek

    # getPayRate() method
    # Purpose: returns the rate
    # Return Type: float
    def getPayRate(self):                                                           
        return self.payRate

    # Mutator Methods
	 
    # setHoursWorked(int) method
    # Purpose: sets the number of hours
    def setHoursPerWeek(self, hoursPerWeek):                                         
        self.hoursPerWeek = hoursPerWeek

    # setPayRate(float) method
    # Purpose: sets the rate
    def setPayRate(self, payRate):                                                    
        self.payRate = payRate

    # Other Methods
	
    # __eq__(object) - overrides __eq__ method from Person class
    # Purpose: compares the instance variable values of the self object
    #   with other object; returns True if equal, else False
    # Return Type: bool
    def __eq__(self, other):
        return Person.__eq__(self, other)               \
            & (self.hoursPerWeek == other.hoursPerWeek) \
            & (self.payRate == other.payRate)

    # __str__() - overrides __str__ method from Person class
    # Purpose: returns a string containing the first and last name, hours worked
    #   and pay rate in one line
    # Return Type: string
    def __str__(self):
        return Person.__str__(self) + "\t" + str(self.hoursPerWeek) \
               + "\t" + str(self.payRate)

