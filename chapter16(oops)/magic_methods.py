# magic methods __init__,__dict__ and so on
class Phone():
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def phone_number(self):
        return f"{self.brand} {self.model}"
      ### magic methods __str__,__repr__
    def __repr__(self):
        return f"{self.brand} {self.price}"

    def __str__(self):
        return f"{self.brand} {self.price}  {self.model}"

my_phone = Phone("nokia","1100",1000)
print(str(my_phone))
print(repr(my_phone))