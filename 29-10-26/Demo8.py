#print sum from 1 to n
n=int(input("enter the limit: "))
s=0
a=1
while(a<=n): #3<=3, 4<=3 stop
    s=s+a #s=0+1+1, s=1+2, s=3, s=3+3, s=6
    a+=1 #a=2, a=3
print("sum=",s) 