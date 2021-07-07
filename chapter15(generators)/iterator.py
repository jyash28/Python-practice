# generators are iterators
l=[1,2,3] #iterables

#i=iter(l)
#print(next(i))
#print(next(i))
#print(next(i))

for num in map(lambda a :a**2,l):#iteratos
    print(num)
