class Mobile:
    def __init__(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def show(self):
        print("Company:", self.company)
        print("Model:", self.model)
        print("Price:", self.price)
    def discount(self):
        a=self.price*0.2
        self.price -= a
        print("After Discount")

v = Mobile("Samsung", "S26 ULTRA", 95000)
v.show()
v.discount()
v.show()

