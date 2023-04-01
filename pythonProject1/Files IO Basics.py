# FILE IO BASICS
"""
"r" - Open file for reading
"w" - Open a file for writing
"x" - Creates file if not exists
"a" - Add more content to the file
"t" - text mode
"b" - binary mode
"+" - read and write
"""
## For reading concepts
"""
f = open("Avi.txt", "rt")
#content = f.read(50)

for line in f:
    print(line, end="") #if end function not insert then extra blank row will be print

#print(f.readline())

# print('1',content)
# content = f.read(4)
#
# print('2',content)


f.close()

"""

## For writing or Append concepts
"""
f = open("Avi.txt", "a")
content = f.write("Having an flight at Wednesday\n")

f.close()
"""

"""
## For read and write both
f = open("Avi.txt", "r+")

#print(f.read())
f.write("Thanks and Regards\nAvisek Saha")
f.close()
"""

"""
f = open("Avi.txt", "r")
#print(f.tell())
print(f.readline()) #Will tell file pointer position
#print(f.tell())
print(f.readline())
f.seek(0)  ##This will reset the file pointer and file pointer will go to 0 line, 0 can be change
print(f.tell())
print(f.readline())

f.close()
"""

# Alternatives of open files
with open("Avi.txt") as f:
    a = f.readline()
    print(a)
print("solution1")

f = open("Avi.txt", "rt")
a = f.readlines()
print("solution2")
f.close()
