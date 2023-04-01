def getdate():
    import datetime
    return datetime.datetime.now()

#For reading
def Bob_for_exercise():
    with open("Bob.txt", "rt") as f:
        e = f.readlines()
        print(e)

def Fred_for_exercise():
    with open("Fred.txt", "rt") as f:
        e = f.readlines()
        print(e)

def Alice_for_exercise():
    with open("Alice.txt", "rt") as f:
        e = f.readlines()
        print(e)

#For writing
def Bob_for_assign():
    f = open("Bob.txt", "w")
    new_exercise = input("Write exercise and food name:",)
#    new_diet= input("Assign new Diet:")
    f.write(new_exercise)
#    f.write(new_diet)
    f.close()

def Fred_for_assign():
    f = open("Fred.txt", "w")
    new_diet = input("Write exercise and food name:")
    f.write(new_diet)
    f.close()

def Alice_for_assign():
    f = open("Alice.txt", "w")
    new_diet = input("Write exercise and food name:")
    f.write(new_diet)
    f.close()


while (True):
    print("Press 1: Continue app, 2: Close app")
    user_input = int(input("Want to continue: "))
    if user_input==1:
        while (True):
            print("Press 0: Previous Menu, 1: Bob profile, 2: Fred profile, 3: Alice profile")
            num1 = int(input("Enter number: "))
            if num1 == 0:
                break
            elif num1 > 3:
                print("Incorrect input! please try again")
            else:
                while (True):
                    print("Press 1: Read, 2: Edit")
                    num2 = int(input("Enter number: "))
                    if num2 > 2:
                        print("Incorrect input, please try again")
                        continue
                    elif num1 == 1 and num2 == 1:
                        print("[", getdate(), "]", Bob_for_exercise())
                        break
                    elif num1 == 1 and num2 == 2:
                        print("[", getdate(), "]", Bob_for_assign())
                        break
                    elif num1 == 2 and num2 == 1:
                        print("[", getdate(), "]", Fred_for_exercise())
                        break
                    elif num1 == 2 and num2 == 2:
                        print("[", getdate(), "]", Fred_for_assign())
                        continue
                    elif num1 == 3 and num2 == 1:
                        print("[", getdate(), "]", Alice_for_exercise())
                        break
                    elif num1 == 3 and num2 == 2:
                        print(Alice_for_assign())
                        break
    elif user_input == 2:
        print("Thanks for use Health Management")
    else:
        print("Wrong input")
