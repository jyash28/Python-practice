class person:
    def __init__(self,first_name,last_name,age):
        #instance variable
        print("init method called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p1 = person("harshit","vashista",24)
p2 = person("mohit" ,"jangir",21)

print(p1.first_name)
print(p2.first_name)