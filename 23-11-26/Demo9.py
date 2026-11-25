# function with passing argument

class product:

    def setdata(self, a, b, c, d):
        self.code = a
        self.name = b
        self.qty = c
        self.price = d

    def display(self):
        print("Code:", self.code)
        print("Name:", self.name)

        self.total = self.qty * self.price
        print("Total Price =", self.total)


obj1 = product()
obj1.setdata(101, "printer", 2, 20000)
obj1.display()

print("-------------------")

obj2 = product()
obj2.setdata(102, "pen drive", 3, 500)
obj2.display()