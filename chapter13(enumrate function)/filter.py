def is_even(a):
    return a%2==0

numbers = [1,2,3,4,5,6,7,8,9,10]
evens = tuple(filter(is_even,numbers)) # or evens= tuple(filter(lambda a : a%2 == 0,numbers))
print(evens)