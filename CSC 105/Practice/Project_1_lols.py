def drawOneFootSquare(Speed, Time, TSpeed, TTime):

    x = input("Go! ")
    while x >= 1:
        for i in range(4):
            forward(Speed,Time)
            turnLeft(TSpeed, TTime)
            beep(1,880)

drawOneFootSquare(1, .9, .9, .35)


    
