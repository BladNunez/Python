class Bank:
        balance = 0

        def withdraw(self,num):
                if num <= 0 or self.balance <= 0:
                        raise Exception("Can not withdraw a negative amount and zero amount!")
                
                return self.balance - num

        def deposit(self,num):
                if num <= 0:
                        raise Exception("Can not deposit negative amount and zero amount!")
                
                return self.balance + num

        def check_balance(self):
                return self.balance
        
        def transfer_money(self,num):
                if num <= 0:
                        raise Exception("Can not transfer negative funds nor zero amount!")
                txt = " has been transferred to "

                return "$" + str(num) + txt
        
        def print_menu(self):
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transfer Money")
                print("5. End Transaction")

        def make_calculations(self,option):
                if option == 1:
                 depo = int(input("How much would you like to deposit?: "))
                 print("Balance after deposit: $" + str(self.deposit(depo)))
       
                elif option == 2:
                   withd = int(input("How much would you like to withdraw?: "))
                   print("Balance after withdraw: $" + str(self.withdraw(withd)))
                elif option == 3:
                  print("Current balance is: $" + str(self.check_balance()))
                elif option == 4:
                  transfer_money = int(input("How much would you like to transfer?: "))
                  reciepent = raw_input("Who is the reciepent of this transfer? : ")

                  print(str(self.transfer(transfer_money)) + reciepent)
                else:
                  print("Thank you for banking with us! Good Day")
                  quit()

banking = Bank()
print("Hello, Welcome to our personal banking system \n")
banking.print_menu()
print("\n")
option = input("What would you like to do today? Input number from menu: ")
banking.make_calculations(option)

another_transaction = raw_input("Would you like to make another transaction? Y/N: ")

if another_transaction == "yes" or another_transaction == "Yes":
        print("\n")
        banking.print_menu()
        print("\n")
        question = input("What would you like to do today? Input number from menu: ")
        banking.make_calculations(question)
else:
        print("Thank you for banking with us! Good Day")
        quit()

