def main():
    WIDTH = 532
    HEIGHT = 640
    win = GraphWin("Myro Control Panel",WIDTH,HEIGHT)
    
    #Background Color
    back = Rectangle(Point(0,0),Point(542,650))
    back.draw(win)
    back.setFill('White')
    
    #Window 1
    r1 = Rectangle(Point(10,10),Point(256,192))
    lbl1 = Text(r1.getCenter(), "No Connection")
    r1.draw(win)
    lbl1.draw(win)
    win1_width = 256
    win1_height = 192
    gap = 10
    center_p = Point(gap+win1_width/2, gap+win1_height/2)
    feed1 = Image(r1.getCenter(),makePixmap(loadPicture('scribbler.jpg')))
    feed1.draw(win)
    
    #Window 2
    r2 = Rectangle(Point(276,10),Point(531,192))
    lbl2 = Text(r2.getCenter(), "No Connection")
    r2.draw(win)
    lbl2.draw(win)
    win1_width = 256
    win1_height = 192
    gap = 10
    center_p = Point(276+win1_width/2, gap+win1_height/2)
    feed2 = Image(r2.getCenter(),makePixmap(loadPicture('scribbler.jpg')))
    feed2.draw(win)

    #Window 3
    r3 = Rectangle(Point(10,212),Point(256,403))
    lbl3 = Text(r3.getCenter(), "No Connection")
    r3.draw(win)
    lbl3.draw(win)
    win1_width = 256
    win1_height = 192
    gap = 10
    center_p = Point(276+win1_width/2, gap+win1_height/2)
    feed3 = Image(r3.getCenter(),makePixmap(loadPicture('scribbler.jpg')))
    feed3.draw(win)

    #Window 4
    r4 = Rectangle(Point(276,212),Point(531,403))
    lbl4 = Text(r4.getCenter(), "No Connection")
    r4.draw(win)
    lbl4.draw(win)
    win1_width = 256
    win1_height = 192
    gap = 10
    center_p = Point(276+win1_width/2, gap+win1_height/2)
    feed4 = Image(r4.getCenter(),makePixmap(loadPicture('scribbler.jpg')))
    feed4.draw(win)

    #COM Port entry field
    comEntry = Entry(Point(154,444),6)
    comEntry.setText('COM')
    comEntry.draw(win)

    #Refresh_Cam entry field
    refEntry = Entry(Point(254,512),2)
    refEntry.setText('0')
    refEntry.draw(win)

    #Draw Add_Robot Button
    addRobot = Rectangle(Point(10,432),Point(102,482))
    aRlbl = Text(addRobot.getCenter(), "Add Robot")
    addRobot.draw(win)
    addRobot.setFill('Cyan')
    aRlbl.draw(win)

    #Refresh Button
    refresh = Rectangle(Point(210,432),Point(302,482))
    reflbl = Text(refresh.getCenter(), "Refresh")
    refresh.draw(win)
    refresh.setFill('Cyan')
    reflbl.draw(win)

    #Quit Button
    endP = Rectangle(Point(10,532),Point(102,582))
    endlbl = Text(endP.getCenter(), "End")
    endP.draw(win)
    endP.setFill('Cyan')
    endlbl.draw(win)
    
    #Draw Joystick controls
    joyStick = Circle(Point(420,512),80)
    joyStick.setFill('cyan')
    joyStick.draw(win)

    
    while True:
        count = 0
        while True:
            click = win.getMouse()
            print "(%d, %d)"%(click.getX(),click.getY())
            if 10<click.getX()<102 and 432<click.getY()<482:
                count = count + 1
                Rob = comEntry.getText()
                print "Add Robot Clicked"
                if count == 1:
                    static_feed = Image(r1.getCenter(), makePixmap(loadPicture('scribbler2.jpg')))
                    static_feed.draw(win)
                    print count
                    #init(comEntry.getText())
                    robot1 = Scribbler(Rob)
                    print comEntry.getText(), "initialized."
                    #Add com specified in box
                elif count == 2:
                    static_feed = Image(r2.getCenter(), makePixmap(loadPicture('scribbler3.jpg')))
                    static_feed.draw(win)
                    print count
                    #init(comEntry.getText())
                    robot2 = Scribbler(Rob)
                    print comEntry.getText(), "initialized."
                    #Add com specified in box
                elif count == 3:
                    static_feed = Image(r3.getCenter(), makePixmap(loadPicture('scribbler4.jpg')))
                    static_feed.draw(win)
                    print count
                    #init(comEntry.getText())
                    robot3 = Scribbler(Rob)
                    print comEntry.getText(), "initialized."
                    #Add com specified in box
                elif count == 4:
                    static_feed = Image(r4.getCenter(), makePixmap(loadPicture('scribbler5.jpg')))
                    static_feed.draw(win)
                    print count
                    #init(comEntry.getText())
                    robot4 = Scribbler(Rob)
                    print comEntry.getText(), "initialized."
                    #Add com specified in box
                else:
                    print "Unable to add additional robots."
                    count = 4

            #Quit
            if 10<click.getX()<102 and 532<click.getY()<582:
                win.close()
                #quitSure = askQuestion("Do you really want to quit?")
                #if quitSure == 'Yes':
                    #win.close()
                #else:
                    #print "Continuing..."

            #Refresh
            if 210<click.getX()<302 and 432<click.getY()<482:
                refNum = refEntry.getText()
                if refNum == '1' and count >= 1:
                    p = robot1.takePicture()
                    rob1Pic = Image(r1.getCenter(),makePixmap(p))
                    rob1Pic.draw(win)
                    print "Robot_Cam_1 updated."
                elif refNum == '2' and count >=2:
                    p = robot2.takePicture()
                    rob1Pic = Image(r2.getCenter(),makePixmap(p))
                    rob1Pic.draw(win)
                    print "Robot_Cam_2 updated."
                elif refNum == '3' and count >=3:
                    p = robot3.takePicture()
                    rob1Pic = Image(r3.getCenter(),makePixmap(p))
                    rob1Pic.draw(win)
                    print "Robot_Cam_3 updated."
                elif refNum == '4' and count >=4:
                    p = robot4.takePicture()
                    rob1Pic = Image(r4.getCenter(),makePixmap(p))
                    rob1Pic.draw(win)
                    print "Robot_Cam_4 updated."
                else:
                    print "Unable to aquire feed."

            #Joystick
            if 0>click.getX()>532 and 0>click.gety()>640:
                line1 = Line(Point(r4.getCenter()),Point(click.getX(),click.getY()))
                line1.draw(win)
                
            
            
                
            
            

            #Click Window
            #askQuestion
            #Multiple options
            #   remove feed
            #   realtime feed
            #   save screen to out folder
            #   enable joystick control
            #   swap window
            #   
            
                
                


            
                
                
                
    #########################################################################
                
        










