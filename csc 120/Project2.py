

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

def getAverageObstacleReadingAtFixedDistance():
    readings = input("How many reading would you like to take?: ")
    store = [0]
    s_con = -1
    s_add = 0
    storeNum = -1
    inches = 0
    for i in range(readings):
        s_con = s_con + 1
        store[s_con] = getObstacle('center')
        store += [s_add]
        wait(.5)
        print "Reading taken."
    store.remove(0)
    question = askQuestion("Print as list, table?",["List","Table"])
    if question == 'List':
        print store
        print "Reading values processed."
    elif question == 'Table':
        nums = 0
        for i in range(readings):
            nums = nums + 1
            storeNum = storeNum + 1
            print nums, store[storeNum]
        print "Reading values processed."
        

    
    
        
        
    
