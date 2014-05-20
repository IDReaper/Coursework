

def main_for():
    s = 0.0
    c = 0
    x = askQuestion("This program will print the average of the numbers.",["Start","Quit"])
    if x == 'Start':
        num_Var = input("How many numbers do you wish to average?: ")
        for i in range(num_Var):
            var = input("Enter the value: ")
            s = s + var
            c = c + 1
        print "The average of the", c, "numbers is:", s/c
        print "Program terminated."
    elif x == 'Quit':
        print "Program terminated."

def main_while():
    s = 0.0
    c = 0
    x = askQuestion("This program will print the average of the numbers.",["Start","Quit"])
    if x == 'Start':
        while True:
            var = input("Enter the value: ")
            s = s + var
            c = c + 1
            cont = askQuestion("Continue?")
            if cont == 'No':
                break  
        print "The average of the", c, "numbers is:", s/c
        print "Program terminated."
    elif x == 'Quit':
        print "Program terminated."

def sensor():
    senses()
    
def calibrate():
    cal = [0]
    c_con = -1
    c_add = 0
    calNum = -1
    inches = 0
    print "Calibration Initialized. Please make sure that the robot is 12 inches away from an obstacle."
    wait(5)
    question = askQuestion("Start Calibration?")
    if question == 'Yes':
        for i in range(10):
            c_con = s_con + 1
            cal[c_con] = getObstacle('center')
            cal += [c_add]
            wait(.5)
            print "Reading taken."
        cal.remove(0)
        avg = sum[cal]/10
        inches = 12
        
        
        

def getAverageObstacleReadingAtFixedDistance(calibrate):
    if calibrate == 'calibrate':
        cal = [0]
        c_con = -1
        c_add = 0
        calNum = -1
        inches = 12
        print "Calibration Initialized. Please make sure that the robot is 12 inches away from an obstacle."
        wait(5)
        question = askQuestion("Start Calibration?")
        if question == 'Yes':
            for i in range(10):
                c_con = c_con + 1
                cal[c_con] = getObstacle('center')
                cal += [c_add]
                wait(.5)
                print "Reading taken."
            cal.remove(0)
            sumCal = cal[0]+cal[1]+cal[2]+cal[3]+cal[4]+cal[5]+cal[6]+cal[7]+cal[8]+cal[9]
            avg = sumCal/12
            print avg

    readings = input("How many reading would you like to take?: ")
    store = [0]
    distance = [0]
    s_con = -1
    s_add = 0
    d_con = -1
    d_add = 0
    storeNum = -1
    distanceNum = -1
    inches = 0
    for i in range(readings):
        s_con = s_con + 1
        store[s_con] = getObstacle('center')
        store += [s_add]
        wait(.5)

        d_con = d_con + 1
        distance[d_con] = store[s_con]/12           
            
        distance += [d_add]
        wait(.5)
        print "Reading taken."
    store.remove(0)
    distance.remove(0)
    question = askQuestion("Print as list, table?",["List","Table"])
    if question == 'List':
        print store
        print "Reading values processed."
    elif question == 'Table':
        nums = 0
        for i in range(readings):
            #nums = nums + 1
            distanceNum = distanceNum + 1
            storeNum = storeNum + 1
            print distance[distanceNum], store[storeNum]
        print "Reading values processed."
        

    
def getAverageObstacleReadingAtFixedDistance_2():
    readings = input("How many reading would you like to take?: ")
    store = [0]
    distance = [0]
    s_con = -1
    s_add = 0
    d_con = -1
    d_add = 0
    storeNum = -1
    distanceNum = -1
    inches = 0
    for i in range(readings):
        s_con = s_con + 1
        store[s_con] = getObstacle('center')
        store += [s_add]
        wait(.5)
        aDist = input("Enter the distance from object in inches: ")
        d_con = d_con + 1
        #distance[d_con] = store[s_con]/12
        distance[d_con] = aDist            
        distance += [d_add]
        wait(.5)
        print "Reading taken."
    store.remove(0)
    distance.remove(0)
    question = askQuestion("Print as list, table?",["List","Table"])
    if question == 'List':
        print store
        print "Reading values processed."
    elif question == 'Table':
        nums = 0
        for i in range(readings):
            #nums = nums + 1
            distanceNum = distanceNum + 1
            storeNum = storeNum + 1
            print distance[distanceNum], store[storeNum]
        print "Reading values processed."
    
        
        
    
