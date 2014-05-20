# Class to implement the Person ADT
class Person:

    # objects of class Person have two instance variables:
    # firstName - a string
    # lastName - a string

    # Person() - default constructor
    # Purpose: initializes instance variables of new Person object;
    #   first and last names are set to empty string										    
    def __init__(self):                     
        self.firstName = ""
        self.lastName = ""

    # Person(string, string) - constructor with parameters
    # Purpose: initializes instance variables of new Person object
    #   with parameter values
    def __init__(self, firstName, lastName):                     
        self.firstName = firstName
        self.lastName = lastName

    # Accessor methods
	
    # getFirstName() method
    # Purpose: returns the first name
    # Return Type: string
    def getFirstName(self):                                                         
        return self.firstName

    # getLastName() method
    # Purpose: returns the last name
    # Return Type: string
    def getLastName(self):                                                          
        return self.lastName

    # Mutator methods
    
    # setFirstName(string) method 
    # Purpose: sets the first name to parameter value
    def setFirstName(self, firstName):                                               
        self.firstName = firstName

    # setLastName(string) method
    # Purpose: sets the last name to parameter value
    def setLastName(self, lastName):                                                 
        self.lastName = lastName

    # Other methods
    
    # __eq__(Object) method - overrides default __eq__ method 
    # Purpose: returns True if self and other have equal values
    #   of their instance variables, else False
    # Return Type: bool
    def __eq__(self, other):
        return (self.firstName == other.firstName)  \
            & (self.lastName == other.lastName)
    
    # __str__() method - overrides default __str__ method 
    # Purpose: returns a string containing first and last name
    # Return Type: string
    def __str__(self):
        return self.firstName + " " + self.lastName
