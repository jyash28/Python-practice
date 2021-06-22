x=5 #global variable
def func():
    x = 7 # local variable
    return x

print(func())
print(x)