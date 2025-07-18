a = int(input("Enter a number: "))
if a % 2 == 0:
    count = a - 1
else:
    count = a
num = 1
for i in range(count):
    print(num, end=",")
    num += 2

