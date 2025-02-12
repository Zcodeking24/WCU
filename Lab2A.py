# Zachary Stickler and Kevin Glosson
# Lab 2 Part A
# This is our work for Lab 2 Part A, where we test concatenation, bracket notation, substrings, and the print function.

# Task I V (Substrings)

building = "Belk"
room = 358

print(building + " " + str(room))

location = (building + " " + str(room))

print(location)

# Person First/Middle/Last Name (PFN, PMN, PLN)

PFN = "Zachary"
PMN = "Worth"
PLN = "Stickler"

print(PFN + " " + PMN + " " + PLN)
print(PFN[0] + PMN[0] + PLN[0])

# Task II V (Substrings using slices)

fmovie = "Spectre"
print(fmovie[0:5])
print(fmovie[3:])
lenmovie = len(fmovie)
print(fmovie[3:])
print(fmovie[3:lenmovie])

# Task III V (Substring Redo)

print(PFN[0] , PMN[0] , PLN[0], sep = "")



