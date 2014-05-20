# This program shows how to use the object.rotate(...) function.
# We first create a box. We rotate it two different ways by using
# all the same parameters except the origin:
# (1) same box to be rotated; (2) same "axis" parameter;
# (3) same "angle" parameter; (4)But different "origin" parameter.
# You will see the different outcomes, and therefore learn the effect
# of using "origin"

from visual import *

# Create the coordinate system for reference of object positions
x_axis = curve(pos=[(-500,0,0), (500,0,0)], radius=2, color=(10,10,0))
x_label = label(pos=(505,0,0), text='X', box=0, opacity=0)
y_axis = curve(pos=[(0,-500,0), (0,500,0)], radius=2, color=(10,10,0))
y_label = label(pos=(0,505,0), text='Y', box=0, opacity=0)
z_axis = curve(pos=[(0,0,-500), (0,0,500)], radius=2, color=(10,10,0))
z_label = label(pos=(0,0,505), text='Z', box=0, opacity=0)

# Create the object to be rotated
myBox = box(pos=(-100,0,0), axis=(1,0,0), size=(50,100,150), color=(250,0,0))

# First we rotat myBox using
# Rotating an Object
#The cylinder, arrow, cone, pyramid, sphere, ring, box, and ellipsoid objects
#(but not curve or convex) can be rotated about a specified origin:
#
#object.rotate(angle=pi/4.0, axis=axis, origin=pos)
#The rotate function applies a transformation to the specified object
#(sphere, box, etc.). The transformation is a rotation of angle radians,
# counterclockwise around the line defined by origin and origin+axis.
# By default, rotations are around the object's own pos and axis.


print "Before rotation: myBox.pos = ",myBox.pos
print "Before rotation: myBox.axis = ",myBox.axis
print "Before rotation: myBox.size = ",myBox.size
print "Before rotation: myBox.color = ",myBox.color

myBox.rotate(angle=pi/4.0, origin=(-100,0,0), axis=(1,0,0))# now myBox has been rotated
print "After rotation: myBox.pos = ",myBox.pos
print "After rotation: myBox.axis = ",myBox.axis
print "After rotation: myBox.size = ",myBox.size
print "After rotation: myBox.color = ",myBox.color

#Now we are to create another box, myBox2, the same as myBox except color being blue 
myBox2 = box(pos=(-100,0,0), axis=(1,0,0), size=(50,100,150), color=(250,0,250))

myBox2.rotate(angle=pi/2.0, origin=(100,0,0), axis=(0,0,1))

myBox3 = box(pos=(-100,0,0), axis=(1,0,0), size=(50,100,150), color=(250,250,250))

myBox3.rotate(angle=5*pi/4.0, origin=(100,0,0), axis=(0,0,1))
for i in range(30):
    alpha=pi/6.0 + i*0.005
    myBox3.rotate(angle=alpha, origin=(100,0,0), axis=(0,0,1))
    rate(10)
axis_of_rotation_of_Box3 = arrow(pos=(0,300,0), axis=(250,250,250))    
for alpha in arange(0.0, pi, 0.05):
    myBox3.rotate(angle=alpha, origin=(0,300,0), axis=(1,1,1))
    rate(100)

myBall = sphere(pos=(-100,-50,-200), radius=50, color=(10,10,10))
for alpha in arange(0.0, pi, 0.05):
    myBall.rotate(angle=alpha, origin=(0,300,0), axis=(1,1,1))
    rate(10)
