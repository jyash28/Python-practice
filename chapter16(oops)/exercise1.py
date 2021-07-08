class laptop:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.name = model_name
        self.price = price

    def apply_discount(self,num):
        off_price = (num/100)*self.price
        return self.price - off_price

laptop1 = laptop("hp","au11234x",50000)
print(laptop1.apply_discount(10))