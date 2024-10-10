import turtle
import time

# turtle.color('red')
# turtle.fillcolor('red')
# turtle.begin_fill()
# turtle.circle(50)
# turtle.end_fill()

def intTest(textToDisplay):
	try:
		val = int(input(textToDisplay))
		return val
	except:
		print("Please enter a valid number")
		return -1

maxLen = -1
while maxLen == -1 or maxLen < 1 or maxLen % 2 == 0:
	maxLen = intTest("Enter an odd number greater than 0: ")

for x in range(int((maxLen + 1) / 2)):
	stars = int(x * 2 + 1)
	spaces = int((maxLen - stars) / 2)
	for x in range(spaces):
		print(" ", sep = '', end='')
	for x in range(stars):
		print("*", sep = '', end='')
	for x in range(spaces):
		print(" ", sep = '', end='')
	print("")

circle = 360

def drawthis(sides):
	for x in range(sides):
		turtle.right(circle / sides)
		turtle.forward(100)
	time.sleep(2)
	turtle.clearscreen()

drawthis(3)
drawthis(4)
drawthis(6)
drawthis(8)

turtle.Screen().exitonclick()