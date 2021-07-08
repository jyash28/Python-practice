class laptop:
    discount_persent = 10
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.name = model_name
        self.price = price

    def apply_discount(self):
        off_price = (self.discount_persent/100)*self.price
        return self.price - off_price

laptop1 = laptop("hp","au11234x",50000)
laptop2 =laptop("apple", "macbookpro",80000)

laptop2.discount_persent = 50
print(laptop2.apply_discount())
