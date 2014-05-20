def r1():
    ambL, ambC, ambR = getLight()
    amb_lev = (ambL + ambC + ambR)/3.0
    while timeRemaining(60):
        L, C, R = getLight()
        current = (L + C + R)/3.0
        while current - amb_lev < 250:
            L, C, R = getLight()
            current = (L + C + R)/3.0
            while getObstacle('center') > 5500:
                stop()
                turnRight(1,.171)
            motors(.5,.5)
        stop()
            
    
