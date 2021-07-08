class laptop:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.name = model_name
        self.price = price

laptop1 = laptop("hp","au11234x",50000)
print(laptop1.name)