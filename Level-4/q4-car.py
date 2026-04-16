class Student :
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def show(self):
        print("Car Name:", self.name)
        print("Car Model:", self.model)
        print("Priece:", self.price)
    def discount(self):
        amount=int(self.price)*0.1
        self.price -= amount
        print("Discount ",amount)
v=Student("Lamborghini ","Revuelto",807000)
v.show()
v.discount()
v.show()

