import random

def select_num():
        num = [1,2,3,4,5,6]

        random_num = random.choice(num)

        return random_num


while True:
        dice_roll = random.randint(1,6)

        keep_rolling = raw_input("Would you like to keep rolling? Y/N: ")

        if keep_rolling == "yes" or keep_rolling == "Yes":
                print("Dice Roll: " + str(dice_roll))
                print("Function Call of Dice Roll: " + str(select_num()))

        else:
                break
