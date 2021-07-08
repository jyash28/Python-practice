class person:
    count_instance = 0 #class variable/ class attribute
    def __init__(self,first_name,last_name,age):
        person.count_instance = person.count_instance + 1
        self.first_name = first_name
        self.last_name= last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
       first,last,age= string.split(",")
       return cls(first,last,age)


    @classmethod
    def count_instances(cls):
        return f"you have created{cls.count_instance} of person class "

    @staticmethod
    def hello():
        print("hello, static method called")

    def full_name(self):
        return f"{self.first_name}  {self.last_name}"

    def is_above_18(self):
        return self.age>18

p1 = person("harshit" ," vashista",24)
p2 = person("harsh" ,"jangid",21)
p3 = person.from_string("yash, jangir,34")
print(p3.full_name())
person.hello()
