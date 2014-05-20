from visual import *
x_axis=curve(pos=[(-200,0,0),(200,0,0)],radius=1)
y_axis=curve(pos=[(0,-200,0),(0,200,0)],radius=1)

sphere(radius=2)
mybox=box(size=(10,20,30))
print "mybox.pos = ",mybox.pos
print 'mybox.x=',mybox.x
print 'mybox.y=',mybox.y
print 'mybox.z=',mybox.z

print 'mybox.axis=',mybox.axis
print 'mybox.size=',mybox.size
print 'mybox.up=',mybox.up

print 'mybox.color=',mybox.color

up_1=(1,0,0)
rate(5)
mybox.up=up_1
print 'Later mybox.up=',mybox.up
ps_1=(50,0,0)
mybox.pos=ps_1
rate(5)
#object.rotate(angle=pi/4., axis=axis, origin=pos)
mybox_1=mybox
mybox.rotate(angle=pi/4.0, axis=(0,0,1),origin=(0,0,0))
