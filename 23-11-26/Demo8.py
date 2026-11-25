class product:
    def setdata(self):
        self.code=101
        self.name="printer"
        self.qyt=5
        self.price=20000
        def display(self):

            print("code",self.code)
            print("name",self.name)
            self.total=self.qty*self.price
            print("total price=", self.total)

            obj=product()
            obj=setdata()
            obj=display()