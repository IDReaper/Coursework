def km2miles():
    p = input("Enter 1 to loop the program, 0 to run once. ")

    if p == 1:

        while p == 1:
        
            x = input("What is the distance in kilometers? ")
            print x, 'km is', x *.62, 'miles.'
            
            z = raw_input("Continue? Yes/No ")

            if z == 'No':
                
                

    if p != 1:

        x = input("What is the distance in kilometers? ")
        print x, 'km is', x *.62, 'miles.'

km2miles()
    
