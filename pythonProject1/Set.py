"""Set retain the unique value"""
s = set()

#s.add(1)
#s.add(1)
#s.add(9)

#print(s)

l = [1,2,2,3,4]

s_from_list = set(l)

#print(type(s_from_list))
#print(s_from_list) #will print set output {1,2,3,4}
#print(s) #will print list output [1,2,2,3,4]
print(min(s_from_list))