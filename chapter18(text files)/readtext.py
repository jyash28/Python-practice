f= open("file1.txt")
print(f"cursor position{f.tell()}")
print(f.read())
#print(f.readline()) #print only one line
print(f"cursor position{f.tell()}")
f.close()