"""
def avisek (str1):
    avisek (str1)
    print("this is me", str1)

avisek("ovi")
"""

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac
"""
5*4*3*2*1 = 120
"""
num = int(input("Enter nuber: "))
print(factorial_iterative(num))


def factorial_recursive(n):
    if n==0:
        return f"factorial not possible"
    elif n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
"""
5 * factorial_recursive(4)
5 * 4 * factorial_recursive(3)
5 * 4 * 3 * factorial_recursive(2)
5 * 4 * 3 * 2 * 1 = 120
"""
num = int(input("Enter nuber: "))
print(factorial_recursive(num))


