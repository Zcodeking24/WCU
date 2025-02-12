sum = 1
num = 3


if sum == 0: 
    if num > 3: 
        print("alpha") 
else: 
    if num < 2: 
        print("beta")

print()

if sum == 0 and num > 3:
    print("alpha")

elif num < 2:
    print("beta")

print()

for num in range(2,6):
    print(num)

print()

for num in range(3,10,3):
    print(num)

print()

for num in range(9,2,-3):
    print(num)

print()

colors = ["red", "blue", "green"] 
for num in range(0,3):
    print(colors[num])

print()

for num in range(0):
    print("I will not be printed =( ")