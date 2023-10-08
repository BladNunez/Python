#Number Guessing
import random
#Computer will choose a number between a range 1-10
#Once computer has number we will compare to the user input to see if guess is right/wrong
#Give hints on what the number is to user 
#keep track of score if user gets it wrong score is decremented else incremented
def display_info():
        print("Welcome to the number gussing game!")
        print("You will enter a number and see if your guess matches the computer!")
        print("The range will be between 1-100")



computer_guess = random.randint(1,100)
score = 0
user_guess = 0

print("\n")
display_info()
print("\n")

while user_guess != computer_guess:
        user_guess = int(input("Enter Guess: "))

        if user_guess > computer_guess:
                print("Guess Lower!")
                score -= 1
                print("Score: " + str(score))
        elif user_guess < computer_guess:
                print("Guess Higher!")
                score -= 1
                print("Score: " + str(score))
        else:
                print("Correct!")
                print("Score: " + str(score))

