def drawSquare(xCoor,yCoor,color,sideLength):
    xturtle.hideturtle()
    xturtle.pencolor("grey")
    xturtle.fillcolor(color)
    xturtle.begin_fill()
    xturtle.penup()
    xturtle.speed(20)
    goto(xCoor,yCoor)
    xturtle.pendown()
    for i in range(4):
        forward(sideLength)
        right(90)
    xturtle.end_fill()

def moreSquare(x,y,x2,y2):
    drawSquare(x,y,"grey",100)
    xturtle.penup()
    xturtle.pendown()
    drawSquare(x2,y2,"grey",100)

def drawRow(num_squares,start,length):
    for i in range(num_squares):
        drawSquare(start,0,"black",length)
        setheading(0)
        start = start+length


    
    
    
    
    
