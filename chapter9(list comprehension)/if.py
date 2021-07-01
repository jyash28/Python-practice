numbers = list(range(1,11))
even_nums=[i for i in numbers if i%2 == 0]
odd_nums =[i for i in numbers if i%2 != 0]
print(even_nums)
print(odd_nums)