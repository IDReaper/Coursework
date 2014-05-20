import string, os
import time  

def inOut_4():
    
    #The "r" stands for read, the "w" stands for write.
    #Be sure to place the .dat and .out file in the same folder as the program.
    
    Infile = open("vData3.dat","r")              # input file
    Outfile = open("vOut3.out","w")            # output file

    r_val = Infile.readline()                   #Reads the entire first line of the file
    print "\nResistance values:",r_val
    sPr = string.split(r_val)                   #Seperates the two values on line 0, sPr is a list
    fPoint_r = map(float,sPr)
    r = fPoint_r[0]
    r2 = fPoint_r[1]
    r3 = fPoint_r[2]
    
    Outfile.write("   Simulation of System of Electrical Resistive Network")
    Outfile.write("\n==========================================================")
    Outfile.write("\n          R1 =%6.2f, R2 =%6.2f, R3 =%6.2f"%(r,r2,r3))
    Outfile.write("\n----------------------------------------------------------")
    Outfile.write("\nVs(t)           Vr1(t)           Vr2(t)           Vr3(t)")    
    Outfile.write("\n..........................................................")

    #v_val = Infile.read()                       #Read all lines in file. May be used to replace readline();single line
    #sPv = string.split(v_val)
    #fPoint_v = map(float,sPv)
    #x = fPoint_v[0]
    
    #print "\nVoltages", sPv
    
    #y = -1
    #yadd = 0
    a = Infile.readline()
    while a:
        #y = y + 1
        #sPv = string.split(v)
        #fPv = map(float,sPv)
        #volt = sPv[0]
        
        a = string.split(a)
        a = map(int,a)
        a = a[0]
        vr1 =((r)/(r+r2+r3))*a
        vr2 =((r2)/(r+r2+r3))*a
        vr3 =((r3)/(r+r2+r3))*a
        time.sleep(.5)
        print a,"   ",vr1,"   ",vr2,"   ",vr3
        #volt += [yadd]
        
        Outfile.write("\n\n%-8g        %-8g         %-8g         %-8g   "%(a,vr1,vr2,vr3))
  
        a = Infile.readline()
        Infile.close
        Outfile.close
    print "Calculations Complete."
    print "Stored values in .out file."
        
    
