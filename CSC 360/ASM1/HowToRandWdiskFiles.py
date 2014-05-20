#          How To Read from and Write to disk Files.
# This program shows how to read data from a disk file named "asm1p2.dat"
# The disk file contains only one line with two integers 17 and 5 separated by space.
# The program then converts the data into integer values, computes their sum,
# difference, product, quotient, and remainder of the division, and writes
# the results to a disk file named "asm1p2.out"
# To run this program, you must first create a disk file named asm1p2.dat
# Make sure you use the Notepad to create the disk file. Steps to use Notepad
# are:
#         Start --> All Programs --> Accessories --> Notepad
# Left click Notepad to open a Notepad window, then 
# type the two numbers 17 and 5 separated by space. Save them with file name
# "asm1p2.dat". Make sure you type the name asm1p2.dat inside the double
# quotation marks. Then run the program. When execution ends, you should see
# a file named "asm1p2.out" gererated in the same folder where both the source 
# program "HowToRandWdiskFiles.py" and the data file "asm1p2.dat" are in.

#import sys, os, string, math # Bring in the standard librarirs for use in the program.
from sys import *
from os import *
from string import *
from math import *


#infile = open("asm1p2dat.txt",'r')
infile = open("asm1p2.dat", 'r')  # open file "asm1p2.dat" for reading only,
                            # and have variable named infile point to it.
outfile = open("asm1p2.out", 'w') # open file "asm1p2.out" for writing only,
                            # and have variable named outfile point to it.

a = infile.readline()  # read the first data line from file pointed to by
                       # infile, store that line in variable a. 
                                        
b = string.split(a)    # split the line into one list of words, store it in b.

c[0] = map(int, b)        # convert b into a list of integers, store it in c.

x = c[0]               # assign the first number of list c to x
y = c[1]               # assign the second number of list c to y

s = x + y               # assign the sum of x + y to s
d = x - y               # assign the difference of x - y to d
p = x* y                # assign the product of x * y to p
q = x / y               # assign the quotient of x divided by y to q
r = x % y               # assign the remainder of x divided by y to r

outfile.write( "x = %s,  y = %s " % (x, y)) # write to disk file the input 
outfile.write( "\n%s + %s = %s" % (x, y, s))# the input value and sum
outfile.write("\n%s - %s = %s" % (x,y,d))   # the input value and difference
outfile.write("\n%s * %s = %s" % (x,y,p))   # the input value and product
outfile.write("\n%s / %s = %s" % (x,y,q))   # the input value and quotient
outfile.write("\n%s  mod %s = %s" % (x,y,r))# the input value and remainder

infile.close() # close the input file, so that it is no longer available 
outfile.close()#close the output file, so that data written to it is saved.

print ".... Normal End of Job ...." #Display on Python Shell work is done
