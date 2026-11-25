
#prg. for check given no. is prime no. or not

n = int(input("enter any number: "))
found = 0  # prime no.

for i in range(2, n):
    if n % i == 0:
        found = 1  # not prime no.
        break

if found == 1:
    print("not a prime no.")
else:
    print("prime no.")