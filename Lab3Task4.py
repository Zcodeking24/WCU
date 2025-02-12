# Zack Stickler and Kevin Glosson
# Lab 3 Task 4

# Experimenting with eval functions with different data types.

test_var = eval("Hello my name is Paws")
print(test_var)

# THIS CAUSED AN ERROR ^

test_var = eval(" 'Hello my name is Paws' ")
print(test_var)

# This is just evaluating the literal string and then printing it.

# test_var = eval(16 * 4 + 6)
# print(test_var)

# Not a string, so the eval function is confused.

test_var = eval("16 * 4 + 6")
print(test_var)

# 16 * 4 = 64 + 6 = 70, and it prints 70.

test_var = eval(" '16 * 4' + '6' ")
print(test_var)

# Prints "16 * 46", concatenating the strings "16 * 4" and "6" into "16 * 4'6'"" (without single quotes)