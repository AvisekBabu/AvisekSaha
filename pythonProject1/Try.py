num1 = input("Enter number: ")
num2 = input("Enter number: ")
#num1 =int(input("Enter number: "))
#num2 =int(input("Enter number: "))

try:
    print("Sum of the two number is",
          int(num1)+int(num2))
except Exception as x:
    print(x)

#except Exception as e:
#    print(e)

print("Fail")