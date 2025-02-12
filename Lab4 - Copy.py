# Lab 4 Task 1
# Zack Stickler and Kevin Glosson
# Practiced with While and For loops, and saw how they could be interchanged.


# Problem A:

i = 2
while i<9:
    
    print(i)
    i=i+2
    
print("\nWho do we appreciate?")


# Problem B:

i = 2
while i<9:
    if i % 2 == 0:
        print(i)
    i=i+1
    if i > 8:
        print("\nWho do we appreciate?")



# Problem C

i = int(input("Initialize Countdown: "))
print()
while i>0:
    print((i) , "...", end = "", sep = "")
    i=i-1
    if i == 0:
        print("\n\nBLASTOFF!!" )



# Problem D

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))
sum = base

while exponent > 1:
    
    sum = sum * base
    exponent = exponent - 1
    
print(sum)



# Problem A:

for i in range(2,9,2):
    print(i)
print("\nWho do we appreciate? ")

# Problem B:

for i in range(1,9):
    if i % 2 == 0:
        print(i)
   
    
print("\nWho do we appreciate?")


# Problem C

ii = int(input("Initialize Countdown: "))
for i in range(ii,0,-1):
    print((i) , "...", end = "", sep = "")
    i=i-1
    if i == 0:
        print("\n\nBLASTOFF!!" )




# Problem D

base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))
sum = base

while exponent > 1:
    
    sum = sum * base
    exponent = exponent - 1
    
print(sum)


base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))
sum = base

for i in range(1,exponent):
    
    sum = sum * base
    exponent = exponent - 1
    
print(sum)


# For v While: How they are controlled. 
# We know how many loops a for loop will iterate before-hand. 
# A while loop can loop indefinitely and be controlled within the loop.

# definite loop: For loop

# indefinite loop: While loop