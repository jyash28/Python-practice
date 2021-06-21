name=input("enter your name")
i=0
temp=""
for i in range(0,len(name)):
    if name[i] not in temp:
       temp= temp+name[i]
    print(f"{name[i]}:{name.count(name[i])}")
 
