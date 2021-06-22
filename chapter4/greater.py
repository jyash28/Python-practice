def greater(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("enter first no."))
num2=int(input("enter second no."))
bigger= greater(num1,num2)
print(f"{bigger}is greater")
