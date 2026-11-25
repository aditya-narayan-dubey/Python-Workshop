#Dictonary comprehension 
#its a consice single line construct for creating a new dictionary from an iterable.
#it replaces multiline
#syntax: reference={key expresion : value expression for item in iterable if condition}
sqr={x:x**2 for x in  range(1,6)}
print(sqr)
 
keys=["a","b","c"]
values=[11,12,13]
d1={k: v for k,v in zip(keys,values)}
print(d1)