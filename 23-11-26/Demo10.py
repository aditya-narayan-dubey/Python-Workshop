#constructor is a special member function.in python
#python #consturctor define by
#magic method __init__()
class product:
    def __init__(self):
        self.qty=5
        self.price=1000
        print("total=",(self.qty*self.price))
p=product()
