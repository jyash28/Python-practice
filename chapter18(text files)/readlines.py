f= open("file1.txt")
lines = f.readlines()
for line in lines:
    print(line,end="")
f.close()