'''1'''

count = 1000
sumI = 0
for i in range(1, count):
	if i % 3 == 0:
		sumI = sumI + i

sumX = 0
for x in range(1, count):
	if x % 5 == 0:
		sumX = sumX + x

print(sumX + sumI)

'''2'''

'''check for even numbers'''

'''for i in range(1, count):
	if i % 2 == 0:
		print(i)'''

'''check for fibonacci numbers'''

a = 1
b = 0
c = 0
	
while c <= 4000000:
    if a % 2 == 0:
        c+=b
    a, b = b, a+b

print (c)