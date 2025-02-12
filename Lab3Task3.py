# Zack Stickler and Kevin Glosson
# Lab 3 Task 3 

# Calculating and printing the slope and y intercept of lines connecting 2 user-inputted points.

name = input("Please enter your name: ")
point1x = float(input("Enter the x-coordinate of your first location: "))
point1y = float(input("Enter the y-coordinate of your first location: "))
point2x = float(input("Enter the x-coordinate of your second location: "))
point2y = float(input("Enter the y-coordinate of your second location: "))

slope = (float(point2y) - float(point1y))/(float(point2x)-float(point1x))
print("The slope is: " + str(slope))

yintercept = float(point1y) - (float(point1x)*slope)
print("The y-intercept is: " + str(yintercept))
print()
print("Goodbye for now, " + name)