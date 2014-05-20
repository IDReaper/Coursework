# face.py

from myro import *


#from visual import *


class Face:
    
    def __init__(self, window, center, size):
        self.window = window
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize/2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)
        
    def move(self,x,y):
        self.head.move(x,y)
        self.leftEye.move(x,y)
        self.rightEye.move(x,y)
        self.mouth.move(x,y)
        
    def flinch(self):
        self.leftEye.undraw()
        self.rightEye.undraw()
        pL = self.leftEye.getCenter()
        pR = self.rightEye.getCenter()
        p1 = pL.clone()
        p2 = pL.clone()
        p3 = pR.clone()
        p4 = pR.clone()
        rL = self.leftEye.getRadius()
        rR = self.rightEye.getRadius()
        p1.move(-rL,0)
        p2.move(rL,0)
        p3.move(-rR,0)
        p4.move(rR,0)
        deadleftEye = Line(p1,p2)
        deadrightEye = Line(p3,p4)
        deadleftEye.draw(self.window)
        deadrightEye.draw(self.window)
        self.leftEye = deadleftEye
        self.rightEye = deadrightEye

    def unflinch(self):
        #self.deadleftEye.undraw()
        #self.deadrightEye.undraw()
        self.leftEye.undraw()
        self.rightEye.undraw()
        pL = self.leftEye.getCenter()
        pR = self.rightEye.getCenter()
        headSize = int(self.head.getRadius())
        eyeSize = 0.15 * headSize
        newEye_Left = Circle(pL,eyeSize)
        newEye_Right = Circle(pR,eyeSize)
        newEye_Left.draw(self.window)
        newEye_Right.draw(self.window)
        self.leftEye = newEye_Left
        self.rightEye = newEye_Right

    def blink(self,interval,numberBlinks,alwaysTrue):
        if alwaysTrue == 1:
            while True:
                self.flinch()
                wait(interval)
                self.unflinch()
                wait(interval)
        elif numberBlinks > 0:
            for i in range(numberBlinks):
                self.flinch()
                wait(interval)
                self.unflinch()
                wait(interval)
        else:
            self.flinch()
            wait(interval)
            self.unflinch()
            wait(interval)
                
        

win = GraphWin('Faces', 500, 500)
f1 = Face(win,Point(250,250),100)

def threeFaces():
    win = GraphWin('Faces', 500, 500)
    f1 = Face(win,Point(150,150),100)
    f2 = Face(win,Point(350,150),100)
    f3 = Face(win,Point(250,323.3),100)
    


    
    

