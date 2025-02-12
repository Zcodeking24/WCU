'''
num1 = 5
num2 = 8
if num1 > num2 and num1 > 3:
    print("Yeehaw!")
else:
    print("Shaazaaamm")

num1 = 5
num2 = 8
if num1 == num2 or num1 > 3:
    print("Yeehaw!")
else:
    if num2 > num1:
        num1 = num2
    else:
        num2 = num1
        print("Shaazaaamm")
print(num1)
print(num2)

num1 = 2
num2 = 7
if num1 == num2 or num1 > 3:
    print("Yeehaw!")
else:
    if num2 > num1:
        num1 = num2
    else:
        num2 = num1
        print("Shaazaaamm")
print(num1)
print(num2)

num1 = 2
num2 = 1
if num1 == num2 or num1 > 3:
    print("Yeehaw!")
else:
    if num2 > num1:
        num1 = num2
    else:
        num2 = num1
        print("Shaazaaamm")
print(num1)
print(num2)

num1 = 5
num2 = 8

if num1 == num2 or num1 < 3:
    print("Yeehaw!")
elif num1 <= 7:
    print("red")
    if num2 > num1:
        num2 = num2 % num1
    else:
        num2 = num1
        print("Shaazaaamm")
else:
    num1 = num1 - num2  

print(num1)
print(num2)

num1 = 8
num2 = 5

if num1 == num2 or num1 < 3:
    print("Yeehaw!")
elif num1 <= 7:
    print("red")
    if num2 > num1:
        num2 = num2 % num1
    else:
        num2 = num1
        print("Shaazaaamm")
else:
    num1 = num1 - num2  

print(num1)
print(num2)
'''

num1 = 5
num2 = 8

if num1 == num2 or num1 < 3:
    print("Yeehaw!")
elif num1 <= 7:
    print("red")
    if num2 > num1:
        num2 = num2 % num1
    else:
        num2 = num1
        print("Shaazaaamm")
else:
    num1 = num1 - num2  

print(num1)
print(num2)
