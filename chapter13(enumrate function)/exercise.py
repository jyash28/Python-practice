def average_finder(*args):
    average = []
    for i in zip(*args):
        average.append(sum(i)/len(i))
    return average
print(average_finder([1,2,3] ,[4,5,6],[7,8,9]))

# or
#average_finder = lambda *args:[sum(i)/len(i) for i in zip(*args)]
# print(average_finder([1,2,3] ,[4,5,6],[7,8,9]))