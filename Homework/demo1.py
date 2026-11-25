#prg. for 1/1+1/2+........ +1/n
n=int(input("enter the limit"))
sum=0
a=1
while(a<=n):
    div=1/a
    print("div=",div)
    sum=sum+div
    print("sum=",sum)
    a+=1
    print("sum=",sum)