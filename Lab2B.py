# Zachary Stickler and Kevin Glosson
# Lab 2 Part B
# Testing errors in Python, including syntax errors, runtime errors, and logic errors, and using 
# snippets of code to demonstrate the different errors in diverse situations.

# Task 4: Errors In Python

# 1
# display on the console the initials (that is, first letter of each part) of
# the person’s name
first = "Buster"
middle = "G"
last = "Bunny"
# print(first[0] + middle[1] + last[1])
print(first[0] + middle[0] + last[1])
# Runtime error: Interpreter cannot execute due to incorrect space value. Value "G" is in space 0, not 1.
# To fix it, we will change the value to 0.

# 2
# display on the console all the parts of a person’s name with no spaces
# between the parts and with the cursor afterwards on the next line
first = "Babs"
middle = "A"
last = "Bunny"
# print(First + Middle + Last)
print(first + middle + last)
# Syntax error: Variables defined with lowercase letters, but the called values were uppercase letters.
# To fix it, change the variable names to have all lowercase letters, to match the defined variables.

# 3
# display all the parts of a person’s name on the console with one blank
# character between
# each part and with the cursor afterwards on the next line
first = "Wile"
middle = "E"
last = "Coyote"
# print(first, middle last)
print(first, middle, last)
# Syntax error: Missing comma to separate the two variables.
# To fix this, we add the missing comma to separate the variables from each other.

# 4
# display on the console the parts of a person’s name with one space in
# between the parts and with string "FOOOM" on the same line and at the end
# and with the cursor afterwards at the start of the next line
end = "FOOOM\n"
first = "Hamilton"
middle = "J"
last = "Pig"
print(first, middle, last)
print(first, middle, last, end)
# The initial function did not print the value for variable end.
# To fix this, we add a call for the variable into the code.


# 5
# display on the console the values of the variables named first and last in
# order with a space in between them and the cursor afterwards at the start
# of the second line below
first = "Fifi"
last = "La Fume"
# print(first, last, end = \n\n)
print(first, last, end = "\n\n")
# Initially forming a syntax error due to missing quotation marks defining the end value.
# To fix this, we added quotations around the desired definition for end


# 6
# display on the console the values of the variables first and last in order
# with a space in between them and the cursor afterwards at the start of
# the second line below
first = "Calamity"
last = "Coyote"
# print(first, last, "\n\n" = end)
print(first, last, end = "\n\n")
# Syntax error: Have to put the variable to be defined before the definition.
# To fix this, we swap the positions of the variable and its definition.