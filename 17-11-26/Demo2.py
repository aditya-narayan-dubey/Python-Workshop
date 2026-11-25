#dynamic dictionary
product={}
print(type(product))
n=int(input("enter the limit: "))
for i in range(1,n+1):
    key=input("enter key: ")
    value=input("enter value: ")
    product.update({key:value})
    print(product)