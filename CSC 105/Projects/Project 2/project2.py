def rectangle(top_left_x,top_left_y,width,height,fill_color):
    setheading(0)
    color("black",fill_color)
    pu()
    goto(top_left_x,top_left_y)
    pd()
    begin_fill()
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    end_fill()

def isoceles_triangle(top_left_x,top_left_y,base,height,fill_color):
    color("black",fill_color)
    pu()
    goto(top_left_x+base/2.0,top_left_y)
    pd()
    begin_fill()
    goto(top_left_x,top_left_y-height)
    goto(top_left_x+base,top_left_y-height)
    goto(top_left_x+base/2.0,top_left_y)
    end_fill()

def houses():
    isoceles_triangle(-100,100,200,50,"red")
    rectangle(-100,50,200,50,"red")
    rectangle(-90,40,20,20,"yellow")
    rectangle(70,40,20,20,"yellow")
    rectangle(-10,35,20,35,"yellow")

def mountains(num_mountains,fill_color,start,base):
    #Mountains
    for i in range(num_mountains):
        isoceles_triangle(start,0,base,100,fill_color)
        setheading(0)
        start = start+base
        
    
def sun(xpos,ypos,size,fill_color):
    #Sun
    color("yellow",fill_color)
    pu()
    goto(xpos,ypos)
    pd()
    begin_fill()
    circle(size)
    end_fill()
    
def cars():
    #Cars
    print "no"

def trees():
    #Trees
    print "no"

def scenery():
    print "one call to this function should draw everything"
    mountains(5,"grey",0,100)
    sun(100,100,50,"yellow")
    # call the trees drawing function
    # call the houses drawing function
    # call the cars drawing function
    hideturtle() # this is so that the turtle shape i.e. triangle is hidden
    
    
    
    
