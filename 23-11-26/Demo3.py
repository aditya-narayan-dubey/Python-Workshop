x=10 #global variable
print("outside function x=",x)
def demo():
    global y
    y=20 #local variable
    print("inside function x=",x)
    print("inside function y=",y)

    demo()