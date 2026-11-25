#Arbitary keyword argument lists function
def product(**p):
    #print(type(p))
    print(p)

    product(code=1,name="printer",qty=1,price=20000)
    product(code=1,name="dvd",qty=5,price=300)
    product(code=1,name="monitor",qty=2,price=10000)