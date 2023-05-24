number = int(input("Please give us a number: "))
while not number % 2 or number < 0:
 number = int(input("An odd positive number please: "))

for i in range(1, number+1, 2):
 print((number-i) // 2 * ' ', i*'*', sep='')
for i in range(number-2, 0, -2):
 print((number-i) // 2 * ' ', i*'*', sep='')
