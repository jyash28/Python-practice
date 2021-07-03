def to_power(num, *args):
    if args:
        return[i**3 for i in args]
    else:
        return "you din't pass any args"

nums = [1,2,3]
print(to_power(3,*nums))