l1=[1,3,5,7]
l2 =[2,4,6,8]
new_list = []

for i in zip(l1,l2):
    new_list.append(max(i))

print(new_list)