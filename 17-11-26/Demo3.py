#remove duplicate elements from list
a=[11,12,12,12,13,14,13,11]
print(a)
x=list(dict.fromkeys(a))
print(type(x))
print(x)