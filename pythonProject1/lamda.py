"""
# Alternate way of making function
def myfunc(x,y):
    return x+y

print(myfunc(5, 6))


myfunc = lambda x, y: x+y
#    return x+y

print(myfunc(5, 6))
"""

def x_short (x):
    return x[1]

x = [[87,45],[88,44],[12,9]]

x.sort(key=x_short)

print(x)