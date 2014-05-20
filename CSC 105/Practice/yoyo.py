
def yoyo():

    forward(1)
    wait(1)
    backward(1)
    wait(1)
    stop()

def yoyo1(speed):
    forward(speed, 1)
    backwrad(speed, 1)

def yoyo2(waitTime):
    forward(1, waitTime)
    backward(1, waitTime)

def yoyo3(speed, waitTime):
    x = input("Enter 0 to loop: ")
    
    if x <=0:
        x = input("Enter 0 to loop: ")
        while x <=0:

            forward(speed, waitTime)
            backward(speed, waitTime)

    if x > 0:
        forward(speed, waitTime)
        backward(speed, waitTime)


    

    
