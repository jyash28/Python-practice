class circle:
    pi= 3.14 # class variable
    def __init__(self,radius):
        self.radius = radius
    def cal_circumfrence(self):
        return 2*circle.pi*self.radius

c= circle(4)
print(c.cal_circumfrence())
