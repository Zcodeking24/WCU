'''
start = 3
stop = 8

cnt = start
while cnt <= stop:
    print( cnt)
    cnt = cnt + 2

print()

start = 3
stop = 8

cnt = start
while cnt < stop:
    cnt = cnt + 2
    print( cnt )

print()

max = 3

cnt = 0
mystery = 2
while cnt < max:
    cnt = cnt + 1
    print(str(cnt) + " " + str(mystery ) )
    mystery = mystery + 2

print()

start = 3
stop = 3

cnt = start
while cnt > stop:
    print("cnt is " + str( cnt) )

'''
# Rewrite each of the code fragments above using a for statement instead of a while statement.


start = 3
stop = 8

cnt = start

for i in range(3,9,2):
    print(i)

print()

start = 3
stop = 8

cnt = start
for i in range(5,10,2):
    print(i)

print()

max = 3

cnt = 0
mystery = 2
for i in range(1,9):
    
    print(str(cnt) + " " + str(mystery ) )
    

print()

start = 3
stop = 3

cnt = start
for num in range(stop,cnt):
    print("cnt is " + str( cnt) )