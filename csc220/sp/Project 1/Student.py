# Class to implement the Student ADT as a subclass of Person
from Person import *

class Student(Person):

    # instance variables:
    #   firstName (string, inherited from Person) - first name of student (default: empty string) 
    #   lastName (string, inherited from Person) - last name of student (default: empty string)
    #   credits (int) - total number of credits completed by student (default: 0) 
    #   gpa (float) - current grade-point-average of student (default: 0.0)

    # __init__(string, string, int, float) - constructor with parameters
    # Purpose: initializes instance variables of new Student object with
    #   parameter values
    def __init__(self, firstName = "", lastName = "", credits = 0, gpa = 0.0):                     
        Person.__init__(self, firstName, lastName)
        self.credits = int(credits)
        self.gpa = float(gpa)

    # Accessor Methods
	
    # getCredits() method		
    # Purpose: returns the number of credits
    # Return Type: int
    def getCredits(self):                                                      
        return self.credits

    # getGpa() method
    # Purpose: returns the gpa
    # Return Type: float
    def getGpa(self):                                                           
        return self.gpa

    # Mutator Methods
	 
    # setCredits(int) method
    # Purpose: sets the number of credits
    def setCredits(self, credits):                                         
        self.credits = credits

    # setGpa(float) method
    # Purpose: sets the gpa
    def setGpa(self, gpa):                                                    
        self.gpa = gpa

    # Other Methods
	
    # __eq__(object) - overrides __eq__ method from Person class
    # Purpose: compares the instance variable values of the self object
    #   with other object; returns True if equal, else False
    # Return Type: bool
    def __eq__(self, other):
        return Person.__eq__(self, other)               \
            & (self.credits == other.credits)           \
            & (self.gpa == other.gpa)

    # __str__() - overrides __str__ method from Person class
    # Purpose: returns a string containing the first and last name, credits
    #   and gpa in one line
    # Return Type: string
    def __str__(self):
        return Person.__str__(self) + "\t" + str(self.credits) \
               + "\t" + str(self.gpa)

