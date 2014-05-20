# This program shows that the return statement can be used to return
# multiple number of values not just one.
from visual import *
def compute(x,y): # given two integer values x, y
    s=x+y
    d=x-y
    p=x*y
    q=x/y #quotient
    r=x%y # remainder of division
    return s,d,p,q,r
m=13
n=5
a1,a2,a3,a4,a5 = compute(m,n)
print "m=%s,  n=%s" % (m,n)
print "m+n=%3d, m-n=%3d, m*n=%3d\n" % (a1,a2,a3)
print "m/n=%3d, m%sn=%3d\n" % (a4,'%',a5)  
