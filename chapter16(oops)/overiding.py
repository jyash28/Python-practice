class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = price

    def make_a_call(self,phone_number):
        print(f"calling{phone_number}........")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

class Smartphone(Phone):
    def __init__(self, brand, model_name, price,ram,internal_memory,rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is{self._price}"

class Flagshipphone(Smartphone):
    def __init__(self, brand, model_name, price,ram,internal_memory,rear_camera,front_camera):
        super().__init__(brand, model_name, price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera

    def full_name(self):
        return f"{self.brand} {self.model_name} and price is{self._price} and front camera{self.front_camera}"



smartphone =Smartphone ("oneplus","5","30000","6gb","64gb","20mp")
oneplus =Flagshipphone ("oneplus","5","30000","6gb","64gb","20mp","16mp")
print(oneplus.full_name())



