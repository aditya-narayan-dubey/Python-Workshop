#Slicing in list - to get sublist from list
a=[10,20,30,40,50,60,70,80,90,100]
print(a[: :]) #print all data
print(a[2: :]) #print 2 index to all
print(a[-5: -3:]) #print 60 70
print(a[: :-1]) #print list in reverse order
print(a[5:])#print 0 to 4
del a[0:4]
print(a)