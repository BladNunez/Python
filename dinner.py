# Create menu of food options with pricing 
def list_menu():
        print("Welcome to Gains Restraunt!\n")
        print("Entrees:")
        print("1.- 8 oz Steak with Mashed Potatoes/Broccoli: $25.00")
        print("2.- Rice and Chicken: $12.00")
        print("3.- Oatmeal with Protein Powder mixed in, side of Berries/Bananna: $8.00")
        print("4.- Spaghetti and meatballs: $18.00")
        print("5.- Mega Protein Shake w/oatmeal,fruits,2 scoops protein, peanut butter, ice: $10.00")
        print("------------------------------------------------------------------------------------")
        print("Gainy Desserts:")
        print("6- Choclate Protein Cake w/Vanilla Ice Cream: $6.00")
        print("7-Bannana Float w/Choclate Syrup: $6.00")

#Have user choose what option they want from menu
list_menu()
print("\n")
print("Choose the number options above!")
order = input("Hello, What would you like today?: ")
#depending on what they choose add the price and description to a structure
order_receipt = {
        1 : ["8 oz Steak with Mashed Potatoes/Broccoli",25.00],
        2 : ["Rice and Chicken" , 12.00],
        3 : ["Oatmeal with Protein Powder mixed in, side of Berries/Bananna", 8.00],
        4 : ["Spaghetti and meatballs", 18.00],
        5 : ["Mega Protein Shake w/oatmeal,fruits,2 scoops protein, peanut butter, ice", 10.00],
        6 : ["Choclate Protein Cake w/Vanilla Ice Cream", 6.00],
        7 : ["Bannana Float w/Choclate Syrup", 6.00]
}

food = ""
price = 0
sales_tax = 1.25

if order == 1:
        food = order_receipt[1][0]
        price = order_receipt[1][1] 
elif order == 2:
        food = order_receipt[2][0]
        price = order_receipt[2][1] 
elif order == 3:
        food = order_receipt[3][0]
        price = order_receipt[3][1] 
elif order == 4:
        food = order_receipt[4][0]
        price = order_receipt[4][1] 
elif order == 5:
        food = order_receipt[5][0]
        price = order_receipt[5][1] 
elif order == 6:
        food = order_receipt[6][0]
        price = order_receipt[6][1] 
elif order == 7:
        food = order_receipt[7][0]
        price = order_receipt[7][1] 
else:
        print("Sorry we do not have anything for the option you chose!")
        quit()

food_two = ""
price_two = 0

another_order = raw_input("Would you like something else for your order? Y/N: ")

if another_order == "yes" or another_order == "Yes":
        list_menu()
        print("\n")
        second_order = input("What would you like?: ")

        if second_order == 1:
          food_two = order_receipt[1][0]
          price_two = order_receipt[1][1]
        elif second_order == 2:
          food_two = order_receipt[2][0]
          price_two = order_receipt[2][1]
        elif second_order == 3:
          food_two = order_receipt[3][0]
          price_two = order_receipt[3][1]
        elif second_order == 4:
          food_two = order_receipt[4][0]
          price_two = order_receipt[4][1]
        elif second_order == 5:
          food_two = order_receipt[5][0]
          price_two = order_receipt[5][1]
        elif second_order == 6:
          food_two = order_receipt[6][0]
          price_two = order_receipt[6][1]
        elif second_order == 7:
          food_two = order_receipt[7][0]
          price_two = order_receipt[7][1]
        else:
          print("Sorry we do not have anything for the option you chose!")
          quit()

        txt = "Receipt"
        print(txt.upper())
        full_price = (price + price_two) * sales_tax
        full = format(full_price,'.2f')
        print("Items: " + food + ", " + food_two)
        print("Total Price: $" + str(full)  + " Including Tax \n")
        print("Thank you for coming!")
else:
        two_decimal_places = price * sales_tax
        full = format(two_decimal_places,'.2f')
        print("Here is your original receipt below:")
        print("Item: " + food)
        print("Total Price: $" + str(full) + " Including Tax \n")

        print("Thank you for coming!")

