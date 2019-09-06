"""
Alex Singh
asin374
687195036
"""
import turtle
def draw_shape(t, n, s):			#t = turtle 
	if n == 1:						#n = level
		t.forward(s/2)				#s = size of a line
		t.left(90)
		t.forward(s/2)
		t.down()
		t.backward(s)
		t.up()
		t.forward(s/2)
		t.left(90)
		t.down()
		t.forward(s)				#base case
		t.up()
		t.right(90)
		t.forward(s/2)
		t.down()
		t.backward(s)
		t.up()
		t.forward(s/2)
		t.right(90)
		t.forward(s/2)
	else:
		t.forward(s/2)
		t.left(90)
		t.forward(s/2)
		t.down()
		t.backward(s)
		t.up()						#if level > 1
		t.forward(s/2)				#draw a level 1
		t.left(90)
		t.down()
		t.forward(s)
		t.up()
		t.right(90)
		t.forward(s/2)
		t.down()
		t.backward(s)
		t.up()
		t.forward(s/2)
		t.right(90)
#---------------------------------
		t.forward(s)
		t.left(90)
		t.forward(s/2)				#then go to one corner of the shape and face north
		t.right(90)					#call the function again with the -1 level
		draw_shape(t, n-1, s/2)
#---------------------------------
		t.right(90)
		t.forward(s)				#go to corner 2
		t.left(90)
		draw_shape(t, n-1, s/2)
#---------------------------------
		t.backward(s)				#go to corner 3
		draw_shape(t, n-1, s/2)
#---------------------------------
		t.left(90)
		t.forward(s)
		t.right(90)
		draw_shape(t, n-1, s/2)		#go to the last corner
		t.right(90)
		t.forward(s/2)
		t.left(90)					#get back to the center and face north
		t.forward(s/2)

def q1():
	my_win = turtle.Screen()
	my_turtle = turtle.Turtle()
	my_turtle.speed(0)
	my_turtle.left(90)
	my_turtle.up()
	s = 200
	n=-1
	while n < 1:
		n = int(input("Draw shape at level: "))
	draw_shape(my_turtle, n, s)
	my_win.exitonclick()
print("Name:\tAlex Singh\nUPI:\tasin374")
q1()
