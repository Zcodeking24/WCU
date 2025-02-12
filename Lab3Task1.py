# Lab 3 Task 1
# Zack Stickler and Kevin Glosson

# Experimenting with int, float, and string variable concatenations.
# Also tested type casting.

int(4.56)
# Prints 4, cuts off any and all decimal values
float("4.56") * 3
# Prints 13.68, converts string to float, which can be multiplied
float(65)
# Prints 65.0, adds the decimal because it is a Float value.
float("65") + float("45")
# Prints 110.0, converts string to float, which can be added
str(65)
# Prints 65, a string data type
# print("You are Number: " + 5)
# TypeError caused: 5 is a integer which we are trying to concatenate into a string, and Python doesn't understand it.
print("You are Number: " + str(5))
# Python understands this code concatenation, printing "You are Number: 5"
str(45) + str(29)
# Prints "4529", connecting/concatenating the two strings together.
float(str(37.8))
# Prints 37.8, converting the float to a string, and then back to a float.
str(int(57.34))
# Converts 57.34 into an int, clearing the decimal values, and then converts it into a string.

print(int(4.56))
print(float("4.56") * 3)
print(float(65))
print(float("65") + float("45"))
print(str(65))

print(str(45) + str(29))
print(float(str(37.8)))
print(str(int(57.34)))