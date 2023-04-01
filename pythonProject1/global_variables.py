"""
i = 10


def myfunc1(n):
#    global i
#    i = 5
    j = 7
    global i
    i = i+7
    print(i,j)
    print(n, "Avisek is learning")

myfunc1("This is me")
"""

"""
x = 50

def avisek():
    x = 25
    def animesh():
        global x
        x = 13

#    print("Before calling avisek", x)
    animesh()
    print("After calling avisek", x)
avisek()
print(x)

"""

"""
i = 99

def myfunc(n):
    j = 33
    i = i+1
    print(i,j)
    print(n, "My name is Avisek")

myfunc("This is me")
print(i)
"""

i = 100
def Amiya():
    i = 50
    def Avisek():
        global i
        i = 25
    print("before calling Avisek",i)
    Avisek()
    print("after calling Avisek",i)

Amiya()
print(i)