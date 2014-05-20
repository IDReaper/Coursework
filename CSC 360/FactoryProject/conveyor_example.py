#                               June 17, 2008, San Diego, CA
# This program simulates a factory conveyor system in which all boxes
# are the same, but they arrive with random inter-arrival times. We
# will investigate the number of boxes N(t) that have arived up to and
# including time t.
# The simulation input is the set of critical event times. 
# The simulation output is the function N(t) which is the number of
# events up to and including time t.
from visual import *
from random import random, randrange
# Draw the x,y,z axes and labels
x_axis=curve(pos=[(-200,0,0),(200,0,0)],radius=0.03, color=color.yellow)
y_axis=curve(pos=[(0,-50,0),(0,200,0)],radius=0.05, color=color.white)
z_axis=curve(pos=[(0,0,-200),(0,0,200)],radius=0.03, color=color.yellow)
x_label=label(pos=(202,0,0), text='x', box=0, opacity=0)
y_label=label(pos=(0,202,0), text='y', box=0, opacity=0)
#z_label=label(pos=(0,0,202), text='z', box=0, opacity=0)

# The ground floor is 100*100 square units
ground=box(position=(0,0,0),length=400,height=0,width=400, color=(0,10,0))
# The conveyor is 30 units long and 20 units off the ground floor, 10 units wide
conveyor=box(pos=(15,19.9,0),length=30,height=0.2,width=10,color=(0,100,200))
pole_1=box(pos=(5,9.95,0),length=2,height=19.9,width=10,color=(10,0,0))
pole_2=box(pos=(25,9.95,0),length=2,height=19.9,width=10,color=(10,0,0))
# The wharehouse where packages will come out from
# The root position of the supporting poles
F1=(-30,0,30) # southwest foot
F2=(0,0,30) # southeast foot
F3=(0,0,-30) # northeast foot
F4=(-30,0,-30) # northwest foot
# The top position of the supporting poles
T1=(-30,40,30) # southwest top position
T2=(0,40,30) # southeast top position
T3=(0,40,-30) # northeast top position
T4=(-30,40,-30) # northwest top position

# South side wall
Swall=faces(pos=[T2,F1,F2, T1,F1,T2], color=(10,5,0)) # outside of south wall
Swallb=faces(pos=[T2,F2,F1, T2,F1,T1], color=(10,5,5)) # inside of south wall

# North side wall
Nwall=faces(pos=[T3,F3,F4, T3,F4,T4], color=(10,5,0)) # outside of north wall
Nwallb=faces(pos=[T3,F4,F3, T4,F4,T3], color=(10,5,5)) # inside of north wall

# West side wall
Wwall=faces(pos=[T1,F4,F1, T4,F4,T1], color=(10,5,0)) # outside of west wall
Wwallb=faces(pos=[T1,F1,F4, T1,F4,T4], color=(10,5,5)) # inside of west wall

# East side wall where the conveyor is located
# Need 4 more points
F2R=(0,20,10) # this point is located to the right of F2
F2RR=(0,0,5) # this point is located to the right of right of F2
F2RRT=(0,20,5) # this point is located above the right of right of F2
F3L=(0,20,-10) # this point is located to the left of F3
F3LL=(0,0,-5) # this point is located to the left of left of F3
F3LLT=(0,20,-5) # this point is located ABOVE the left of left of F3
T2R=(0,30,10) # this point is located above F2r
T3L=(0,30,-10) # this point is located above F3L
Ewall=faces(pos=[F2RR,F3LL,F3LLT, F3LLT,F2RRT,F2RR, F2R,F2RR,F2RRT, F2RR,F2R,F2, F2,F2R,T2R, T2R,T2,F2, T2,T2R,T3, T2R,T3L,T3,
      T3,T3L,F3, F3,T3L,F3L, F3L,F3LL,F3, F3L,F3LLT,F3LL], color=(10,5,0)) # outside of east wall
Ewallb=faces(pos=[F3LL,F2RR,F3LLT, F2RRT,F3LLT,F2RR, F2RR,F2R,F2RRT, F2R,F2RR,F2, F2R,F2,T2R, T2,T2R,F2, T2R,T2,T3, T3L,T2R,T3,
      T3L,T3,F3, T3L,F3,F3L, F3LL,F3L,F3, F3LLT,F3L,F3LL], color=(10,5,5)) # inside of east wall
wndwln=curve(pos=[T2R,F2R,F3L,T3L,T2R], radius=0.3, color=(10,0,0)) # window line
p11=curve(pos=[T1,F1], radius=1.5, color=(10,0,10))# poles in the 4 corners 
p22=curve(pos=[T2,F2], radius=1.5, color=(10,0,10))
p33=curve(pos=[T3,F3], radius=1.5, color=(10,0,10))
p44=curve(pos=[T4,F4], radius=1.5, color=(10,0,10))

# The roof
# the South side of the roof
M1=(-35,50,0) # middle point on west side
M2=(5,50,0) # middle point on east side
T1x=(-35,40,30) # T1 extra, 5 units to the west of T1
T1xx=(-35,38,40) # T1 extra extra, further south to T1 and lower
T2x=(5,40,30) # T2 extra, 5 units to the east of T2
T2xx=(5,38,40) # T2 extra extra, further south to T2 and lower
Srf=faces(pos=[M1,T1x,T2x, M1,T2x,M2],color=(10,0,10)) #South roof
Srfb=faces(pos=[T1x,M1,T2x, T2x,M1,M2],color=(10,1,10)) #South roof back side
Srfx=faces(pos=[T1xx,T2xx,T1x, T1x,T2xx,T2x],color=(10,0,10)) #South roof edge
Srfxb=faces(pos=[T2xx,T1xx,T1x, T2xx,T1x,T2x],color=(10,1,10)) #S rf edge bk side
# the North side of the roof
T4x=(-35,40,-30) # T4 extra, 5 units to the north of T4
T4xx=(-35,38,-40) # T4 extra extra, further north to T4 and lower
T3x=(5,40,-30) # T3 extra, 5 units to the north of T3
T3xx=(5,38,-40) # T3 extra extra, further north to T3 and lower
Nrf=faces(pos=[M1,M2,T4x, M2,T3x,T4x],color=(10,0,10)) #North roof
Nrfb=faces(pos=[M2,M1,T4x, T3x,M2,T4x],color=(10,1,10)) #North roof back side
Nrfx=faces(pos=[T3xx,T4xx,T3x, T3x,T4xx,T4x],color=(10,0,10)) #North roof edge
Nrfxb=faces(pos=[T4xx,T3xx,T3x, T4xx,T3x,T4x],color=(10,0,10)) #N rf edge bk s
# To build the container at end of the package trip, we need 8 points
ct1=(28,8,10) # container top point position 1
cb1=(28,0.11,10) # container bottom point position 1
ct2=(40,8,10) # container top point position 2
cb2=(40,0.11,10) # container bottom point position 2
ct3=(40,8,-10) # container top point position 3
cb3=(40,0.11,-10) # container bottom point position 3
ct4=(28,8,-10) # container top point position 4
cb4=(28,0.11,-10) # container bottom point position 4
# To build the S.E.N.W walls and base of the container
wallsNbase = faces(pos=[ct1,cb1,cb2, cb2,ct2,ct1, cb2,cb3,ct2, cb3,ct3,ct2, cb3,cb4,ct3,
                   cb4,ct4,ct3, cb4,cb1,ct1, cb4,ct1,ct4, cb1,cb4,cb2,
                   cb2,cb4,cb3], color=(1,1,30))
wallsNbasebk = faces(pos=[cb1,ct1,cb2, ct2,cb2,ct1, cb3,cb2,ct2, ct3,cb3,ct2, cb4,cb3,ct3,
                   ct4,cb4,ct3, cb1,cb4,ct1, ct1,cb4,ct4, cb4,cb1,cb2,
                   cb4,cb2,cb3], color=(30,30,0))

cln_1 = curve(pos=[ct1,cb1],radius=0.3,color=(10,0,0)) # corner line no. 1
cln_2 = curve(pos=[ct2,cb2],radius=0.3,color=(10,0,0)) # corner line no. 2
cln_3 = curve(pos=[ct3,cb3],radius=0.3,color=(10,0,0)) # corner line no. 3
cln_4 = curve(pos=[ct4,cb4],radius=0.3,color=(10,0,0)) # corner line no. 4
tln = curve(pos=[ct1,ct2,ct3,ct4,ct1],radius=0.2,color=(10,0,0)) # top line
bln = curve(pos=[cb1,cb2,cb3,cb4,cb1],radius=0.2,color=(10,0,0)) # base line

# ....... End Building the Factory Conveyor System with End-Container  .......



# Prompt user for total number of events to take place
TotEvntNbr=input("Enter total number of boxex to arrive:\n") # TotEvntNbr=Total Event Nbr
intrArTmList=[]  #inter-arrival time(also named inter-event time) list
for i in range(TotEvntNbr):
    intrArTmList.append(randrange(1,100))
print "intrArTmList = ",intrArTmList
arvTmLst=[intrArTmList[0]] # arrival time list, also named event time list, initialized
                           # with the arrival time of the very first event.
                           # From the second one on, each event arrival time is equal to
                           # the sum of its precessor's arrival time plus the inter-arrival
                           # time as shown in the next two statements.
for x in intrArTmList[1:]:
    arvTmLst += [arvTmLst[-1]+x]
    
print "Arrival Time List or Event Time List = arvTmLst = ",arvTmLst # should be an ascending list
#print "Now, Enter a list of critical event times, in ascending order:\n"
crtEvnTmLst=input("Now, Enter a list of critical event times, in ascending order:\n")
nbrEvnUpInclLst = [] # list of numbers N(t)'s of events up to and including t. t is called critical
                     # event time.  length of crtEvnTmLst = length of nbrEvnUpTnclLst.
                     # that is if crtEvnTmLst = [t1, t2, t3, t4, t5], then
                     #        nbrEvnUpInclLst = [N(t1), N(t2), N(t3), N(t4), N(t5)]
pair=zip(arvTmLst[:-1],arvTmLst[1:])
#print "Debug $$$$$$$ pair = ",pair
for m in crtEvnTmLst:
    if m<arvTmLst[0]:
        nbrEvnUpInclLst.append(0)
    elif arvTmLst[-1] <= m:
        nbrEvnUpInclLst.append(len(arvTmLst))
    else:
        for k in range(len(pair)):
            if pair[k][0] <= m <pair[k][1]:
                nbrEvnUpInclLst.append(k+1)                
print "List of nbr of events up to and including critical time = nbrEvnUpInclLst = ",nbrEvnUpInclLst    
#Next we will show the arrival of one box for each entry a in inList
# The longer the inter-event time implies the slower the execution.
# So we use rate(10.0/a) as the inter-event time.
for k in intrArTmList:
    rate(10.0/k) # waiting for k seconds. Greater k value implies smaller rate
                 # which then implies longer waiting time for next box to arrive
    # All packages are the same, so we use a box object to display a package
    pkg=box(position=(0,22.5,0),length=5,height=5,width=2, color=(100,0,0))
    # pkg is being transported On the conveyor
    t=0.0
    dt=0.1
    while t<=32.5:
        x=  t
        y=22.5
        z=0
        pkg.pos=(x,y,z)
        t +=dt
        rate(150)
    # pkg is descending
    t=22.5
    dt=0.2
    while t>=2.5:
        rate(50)
        x=32.5
        y=t
        z=0
        pkg.pos=(x,y,z)
        t=t-dt
    #pkg.visible = 0  # pkg disappearing
