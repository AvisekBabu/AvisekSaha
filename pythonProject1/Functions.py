a = 4
b = 3
c = sum((a,b)) #Built in functions
print(c)


# User define functions
def myfunc1(a,b):
    """This function written for calculate the sum of two numbers"""
#    print("How are you")
    average = (a+b)/2
    return average
#    print(average)

#print(myfunc1(4,8))
print(myfunc1.__doc__)