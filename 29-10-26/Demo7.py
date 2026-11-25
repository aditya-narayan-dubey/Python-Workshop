#prg. for check armstrong no.

n = int(input("Enter any number: "))
r = n
res = 0
temp = n

while n != 0:
    a = n % 10
    res = (a ** 3) + res
    n = n // 10

if res == temp:
    print(r, "is an Armstrong number")
else:
    print(r, "is not an Armstrong number")
