# This program shows that the return statement can be used to return
# multiple number of values not just one, by using a list.
from visual import *
def compute(x,y): # given two integer values x, y
    myList = [ ]
    s=x+y
    d=x-y
    p=x*y
    q=x/y #quotient
    r=x%y # remainder of division
    myList = [s]+[d]+[p]+[q]+[r] # add the 5 singleton lists together
    print "Within the compute function, myList = %s\n" % myList
    return myList
m=13
n=5
L = compute(m,n)
print "m=%s,  n=%s\n" % (m,n)
print "m+n=%3d, m-n=%3d, m*n=%3d\n" % (L[0],L[1],L[2])
print "m/n=%3d, m%sn=%3d\n" % (L[3],'%',L[4])  
