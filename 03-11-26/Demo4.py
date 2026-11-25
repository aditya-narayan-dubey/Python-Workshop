#bubble sorting

a = [5, 4, 3, 2, 1]

print("before sorting")
print(a)

n = len(a)

for i in range(0, n):  # no. of rounds
    for j in range(0, n-1-i):  # data comparison
        if (a[j] > a[j+1]):
            #swap
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t

print("after sorting")
print(a)
