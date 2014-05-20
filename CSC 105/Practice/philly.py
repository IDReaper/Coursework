def philly_cheese_steak():
    dem = input("The democrats!")
    rep = input("The republicans!")
    ind = input("Them other fools!")
    all = dem+rep+ind
    if dem >= all/3:
        print "HOPE!"
    elif rep >= all/3:
        print "DOPE!"
    elif ind >= all/3:
        print "POPE!"
    else:
        print "NOPE!"
    
    
