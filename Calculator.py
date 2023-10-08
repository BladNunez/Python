        #Addition Function 
def addition(numberOne, numberTwo):
        return numberOne +  numberTwo

        #Subtraction Function
def subtraction(numberOne,numberTwo):
       return numberOne - numberTwo
        #Division Function 
def divide(numberOne , numberTwo):
       if numberOne == 0 or numberTwo == 0:
              raise Exception("CAN NOT DIVIDE BY ZERO!")

       return numberOne / numberTwo

        #Multiplication Function 
def multiply(numberOne , numberTwo):
        return numberOne * numberTwo

def display_list():
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")
                print("5. End Program")

while True:
 display_list()
 choice = input("Enter Choice for Calculation: ")

 if choice == 1:
        print("Addition was Chosen")
        num_one = int(input("Enter First Number: "))
        num_two = int(input("Enter Second Number: "))
        print(addition(num_one,num_two))
 elif choice == 2:
        print("Subtraction was Chosen")
        num_one = int(input("Enter First Number: "))
        num_two = int(input("Enter Second Number: "))
        print(subtraction(num_one,num_two))
 elif choice == 3:
        print("Multiplication was Chosen")
        num_one = int(input("Enter First Number: "))
        num_two = int(input("Enter Second Number: "))
        print(multiply(num_one,num_two))
 elif choice == 4:
        print("Division was Chosen")
        num_one = int(input("Enter First Number: "))
        num_two = int(input("Enter Second Number: "))
        print(str(num_one) + " / " + str(num_two) + " = " + str(divide(num_one,num_two)))
 else:
        txt = "Program Terminated!"
        print(txt.upper())
        quit()