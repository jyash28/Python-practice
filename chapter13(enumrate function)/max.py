def func(item):
    return len(item)
names = ["yash", "harshit", "vinay","abc"]
print(max(names,key= func)) 
#or
#names = ["yash", "harshit", "vinay","abc"]
#print(max(names,key= lambda item : len(item))) 