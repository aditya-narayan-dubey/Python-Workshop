# list with membership operator

a = [3, 23, 56, 43, 5, 6, 7]

s = int(input("enter data to be searched: "))

res = s in a

if (res):
    print("data found")
else:
    print("not found")