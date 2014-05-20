# This program shows that the changed value of the input parameter 
# cannot be returned to the calling program. In order to return the
# updated value of x we can use the return statement.
from visual import *
def sq(x): # x is given the value 3
    print "Within function sq, at the beginning x = %s\n" % x
    y=x*x  # y has value 9
    x=5*x  # x now has value 15
    print "Within function sq, later on x = %s\n" % x
    return x, y
x=3   # 3 is passed to the function sq
x, c = sq(x)
print "x=%s,  c=%s" % (x,c)
