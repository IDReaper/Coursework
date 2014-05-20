def tempGet():

    celsius = input("What is the temp in celsius? ")
    while celsius >= -9999:
        print 9.0/5.0*celsius+32, "Fahrenheit"
        celsius = input("What is the temp in celsius? ")
        
tempGet()


