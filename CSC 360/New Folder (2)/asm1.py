import string, os


infile = open("asm1.dat", "r")#open .dat

outfile = open("asm1.out", "w")#open.out

a = infile.readline()#read line 0

#Split r1 and r2
b = string.split(a)
c = map(float, b)

r1 = c[0]
r2 = c[1]

#Write to .out
outfile.write("Simulation of System of Electrical Resistive Network")
outfile.write("\n====================================================")
outfile.write("\nR1 =%6.2f, R2 =%6.2f"%(r1,r2))
outfile.write("\nVs(t)              Vr(t)\n")

vs = infile.readline()
while vs:
    vs = string.split(vs)
    vs = map(int,vs)
    vs = vs[0]
    vr =(r2/(r1+r2))*vs
    outfile.write("\n%s          %s  "%(vs,vr))
    vs = infile.readline()
    infile.close
    outfile.close
print "Calculations Complete"
    
