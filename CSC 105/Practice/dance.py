def yoyo(speed, time):
    forward(speed, time)
    backward(speed, time)
    stop()

def wiggle(speed, time):
    rotate(-speed)
    wait(time)
    rotate(speed)
    wait(time)
    rotate(speed)
    wait(time)
    stop()
    
def newDance(n):
    for i in range(n):
        yoyo(1,.3)
        wiggle(1,.1)

def beepLots(b):
    for i in range(b):
        beep(.5,400)
        beep(.5,400)
        beep(.5,400)
        beep(.5,400)
    
def moreDance():
    x = input("0 to loop, 1 to end after process: ")

    if x == 0:
        while x == 0:
            n = input("How long do da do da dance?: ")
            newDance(n)
            p = input("0 to continue: ")

            if p != 0:
                stop()

    else:
        n = input("How long do da do da dance?: ")
        newDance(n)

        
    
