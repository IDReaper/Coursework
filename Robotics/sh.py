def n(threshold,t):
    for test in range(1):
        
        print "Starting pixel based recognition..."
        print "Scanning",test,"of 3"
        total = 0
        pic = takePicture()
        print "Imaging scanning initiated..."
        for i in range(getWidth(pic)):
            for j in range(getHeight(pic)):
                r, g, b = getRGB(getPixel(pic, i, j))
                total = total + r + g + b
        print "Image scanned! Manipulating data..."
    
        total= total / (getWidth(pic)*getHeight(pic)*3)
        print "Collected data :"
        print "R,G,B AVG = ",total
        print "Threshold = ",threshold
        if total > threshold:
            print "Color shift detected..."
            turnRight(.5,.5)
        if total < t:
            forward(1)

def x():
    forward(.75)
    if getObstacle('center') > 5500:
        turnRight(.5,.5)
        forward(.75)
        if getObstacle('center') > 5500:
            turnRight(.5,.5)
            n(150,100)
            forward(.75)
            if getObstacle('center') > 5500:
                turnLeft(.5,.5)
                n(150,100)
    
