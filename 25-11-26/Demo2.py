#function overloading
from multipledispatch import dispatch

@dispatch(int)
def add(x):
    print(x+x)

@dispatch(int,float)
def add(x,y):
    print(x+y)

@dispatch(float,int,float)
def add(x,y,z):
    print(x+y+z)    

    add(10)
    add(10,20.32)
    add(3.4,5,6,5)
    
