# This program shows how to construct a container. But it does only
# half of the container. Since angle alpha only ranges from -pi/2.0
# to pi/2.0

from visual import *
x_axis=curve(pos=[(-200,0,0),(200,0,0)],radius=1)
y_axis=curve(pos=[(0,-200,0),(0,200,0)],radius=1)
ground=box(size=(600,0,600),color=(0,10,0))

sphere(radius=2)

mybox=box(pos=(0,15,50),size=(20,30,2),axis=(1,0,0))

print "mybox.pos = ",mybox.pos
print 'mybox.x=',mybox.x
print 'mybox.y=',mybox.y
print 'mybox.z=',mybox.z


for alpha in arange(-pi/2.0,pi/2.0,pi/50.0):
    ps=(50*cos(alpha),15,-50*sin(alpha))
    ax=(cos(alpha+pi/2.0),0,sin(alpha+pi/2.0))
    box(pos=ps,axis=ax,size=(20,30,2))
    
print 'mybox.axis=',mybox.axis
print 'mybox.size=',mybox.size
print 'mybox.up=',mybox.up

print 'mybox.color=',mybox.color

