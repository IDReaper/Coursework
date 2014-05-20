def fear():
   while True:
        if getObstacle('center','left','right') < 5000:
            forward(.5)
        while getObstacle('center','left','right') > 5000:
            if getObstacle('left') > getObstacle('right'):
                turnLeft(1)
            elif getObstacle('left') < getObstacle('right'):
                turnRight(1)
            else:
                backward(1)
                turnRight(1,2)
            forward(1,10)
