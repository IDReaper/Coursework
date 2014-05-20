#Shawn Thompson
#CSC 360
#ex 1.1
#List of input voltage
#Corrosponding output voltage
#Vr(t) = Ir2
#Vs(t) = I(r+r2)
#Vr(t)/Vs(t)= Ir2/(I(r+r2)) = r2/(r+r2)
#Vr(t) becomes equation used in line 12

def inOut_1(r,r2):
    control = 1
    while control == 1:
        x = input("Please enter the voltage: ")
        z = ((r2)/(r+r2))*x
        print "x(t) z(t)"
        print x,"  ", z
        qP = raw_input("Enter another value?: ")
        if qP == 'N' or qP == 'No' or qP == 'n' or qP == 'no':
            break
    print "All values processed. Program Ended."
            
def inOut_2(r,r2):
    #xList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #zList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    xList = [0]
    zList = [0]
    control = input("How many voltage values would you like to calculate?(20 Max): ")
    xL_con = -1
    zL_con = -1
    xadd_line = 0 
    zadd_line = 0
    for i in range(control):
        xL_con = xL_con + 1
        zL_con = zL_con + 1
        x = input("Please enter the voltage: ")
        z = ((r2)/(r+r2))*x
        xList[xL_con] = x
        zList[zL_con] = z
        xList += [xadd_line]
        zList += [zadd_line]
        #print "x(t) z(t)"
        #print x,"  ", z
    xList.remove(0)
    zList.remove(0)
    xnums = -1
    znums = -1
    for i in range(control):
        xnums = xnums + 1
        znums = znums + 1
        print xList[xnums],"   ", zList[znums] 
    print "All values processed. Program Ended."

#Suppose the input values are given in a data file. "vData.dat"
#ex:
#20 30
#220
#350
#1000
#3350
#1250
#600


#v = infile.readline()
#while v:
    #v = string.split(v)
    #v = map(float,v)
    #v = v[0]
    #vr = v*((r2)/(r1+r2)
    #outfile.write("%-6.2f     %-6.2f   "%(v,vr))
    #v = infile.readline()
    #infile.close
    #outfile.close
    
def inOut_3(control):
    import string, os
    #The "r" stands for read, the "w" stands for write.
    #Be sure to place the .dat and .out file in the same folder as the program.
    Outfile = open("vData.out","w")            # output file
    Outfile.write("Simulation of System of Electrical Resistive Network")
    print
    Outfile.write("======================================")
    print
    

    Infile = open("vData.dat","r")              # input file
    r_val = Infile.readline()                   #Reads the entire first line of the file
    print "Resistance values:",r_val
    sPr = string.split(r_val)                   #Seperates the two values on line 0, sPr is a list
    fPoint_r = map(float,sPr)
    r = fPoint_r[0]
    r2 = fPoint_r[1]
    Outfile.write("     R1 =%6.2f, R2 =%6.2f"%(r,r2))
    

    
    v_val = Infile.read()                       #Read all lines in file. May be used to replace readline();single line
    sPv = string.split(v_val)
    fPoint_v = map(float,sPv)
    x = fPoint_v[0]
    
    print "Voltages", sPv

    
    xList = [0]
    zList = [0]
    fPoint_v = [0]
    #control = input("How many voltage values would you like to calculate?(20 Max): ")
    xL_con = -1
    zL_con = -1
    xadd_line = 0 
    zadd_line = 0

    y = -1
    
    for i in range(control):
        
        y = y + 1
        
        #xL_con = xL_con + 1                     #Set slot in list to store data
        #zL_con = zL_con + 1
        #x = input("Please enter the voltage: ")
        
        z = ((r2)/(r + r2))* x

        
        #xList[xL_con] = fPoint_v[y]                     #Set the value of the slot in list
        #zList[zL_con] = z
        #xList += [xadd_line]                    #Add new line to list
        #zList += [zadd_line]
        #print "x(t) z(t)"
        #print x,"  ", z

        
    #xList.remove(0)                             #Drop the initial zero placeholder value
    #zList.remove(0)
    #xnums = -1
    #znums = -1

    
    #for i in range(control):
        #xnums = xnums + 1
        #znums = znums + 1
        #print xList[xnums],"   ", zList[znums] 
    print "All values processed. Program Ended."
        





    
