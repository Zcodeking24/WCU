# Zack Stickler and Kevin Glosson
# Lab 3 Task 2

# Ask for user inputs, and then displayed and added collected information.

fullname = input("Please enter your name: \n")

hometown = input("\nPlease enter your hometown: " + "\n")
age = input("\nPlease enter your age: " + "\n")
luckynum = input("\nEnter your lucky number: " + "\n")

print("Name: " + fullname)
print()
print("Hometown: " + hometown)
print()
print("Age: " + age)
print()
print("Lucky number: " + luckynum)

newnum = int(age) + int(luckynum)
print()
print("Age + lucky number: " + str(newnum))