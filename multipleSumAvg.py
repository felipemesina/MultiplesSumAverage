for i in range (1,1001, 2):
   print i

for x in range (5, 1000001, 5):
    print x


a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a: 
    sum = sum + i 
print sum

b = [1, 2, 5, 10, 255, 3]
avg = 0
for i in b:
    avg = avg + i / len(b)
print avg