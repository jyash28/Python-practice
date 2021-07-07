# print 1 to 10
def nums(n):
    for i in range(1,n+1):
        yield(i)
for number in nums(10):
    print(number)