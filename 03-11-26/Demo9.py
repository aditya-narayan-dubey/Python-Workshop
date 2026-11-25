a=(10,20,30,40,50)
print(a)
#a.append (60)#AttributeError
#convert tuple to list 
b=list(a)
b.append(60)
print(b)
#convert list to tuple 
a=tuple(b)
print(a)