def total(a,b):
    return a+b
def all_total(*args):
    total=0
    for num in args:
        total= total +num
    return total
print(all_total(1,2,3,4))
