#from graphics import *
from random import *

def yesh():
    win = GraphWin('Point Return')

    r = Rectangle(Point(10,10),Point(50,50))
    Labelhit = Text(r.getCenter(), "HIT")
    r.setFill('red')
    r.draw(win)
    Labelhit.draw(win)

    g = Rectangle(Point(60,10),Point(100,50))
    Labelgo = Text(g.getCenter(), "GO")
    g.setFill('green')
    g.draw(win)
    Labelgo.draw(win)

    c = Circle(Point(50,100), radius = 10)
    c.setFill('blue')
    c.draw(win)
    
    
#def p_Return1():
    #win = GraphWin('Point Return')
    #for i in range(10):
        #p = win.getMouse()
        #print "(%d, %d)"%(p.getX(),p.getY())

#def p_Return():
    
    #x = 1
    #while x == 1:
    while True:
        xgo = randrange(-10,10)
        ygo = randrange(-10,10)
        
        p = win.getMouse()
        print "(%d, %d)"%(p.getX(),p.getY())
        #button(p.getX(),p.getY())
    
#def hiTbutton(x1,y1):
        if 10<p.getX()<50 and 10<p.getY()<50:
            print "HIT Clicked"
            win.close()
        
        elif 60<p.getX()<100 and 10<p.getY()<50:
            
            print "GO Clicked"
            c.move(xgo,ygo)
        else:
            print "No selection"
        
            
    
