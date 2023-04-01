# number = 18
# no of guesses = 9
# print number of guesses left
# No of guesses he took to finish
# game over

number = 18
print('This is a number guess game')
#User_input = int(input("Enter number: "))

total_guesses = 9
guesses = 0
while(True):
    num1=int(input("Enter number: "))
    if num1==number:
        print("Booyah! You guess the correct number")
        print("Number of guesses to finish the game", guesses)
        break
    elif num1>18:
        print("Number is too high!")
    else:
        print("Number is too low!")
    guesses=guesses+1
    print("Guesses left now", total_guesses - guesses)
    if total_guesses == guesses:
        print("You lose the game")
        break
