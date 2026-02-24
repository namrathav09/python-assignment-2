# ATM Simulation Program

def atm_machine():

    # Initial balance
    balance = 10000   

    # Minimum balance     
    minimum_balance = 500  

    print("Welcome to the ATM!!!!")

    while True:

        print("\n-----ATM CHOICE-----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice from 1-4: ")

    
        if choice == "1":
            print("Your current balance is: ₹", balance)

        
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))
            except:
                print("Invalid input. Please enter a number.")
                continue

            if amount <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                balance = balance + amount
                print("Money deposited successfully.")
                print("Updated balance is: ₹", balance)

        
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
            except:
                print("Invalid input. Please enter a number.")
                continue

            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")

            elif amount > balance:
                print("Insufficient balance.")

            elif balance - amount < minimum_balance:
                print("Minimum balance of ₹500 must be maintained.")
                print("Transaction cancelled.")

            else:
                balance = balance - amount
                print("Please collect your cash.")
                print("Updated balance is: ₹", balance)

        elif choice == "4":
            print("Thank you for using the ATM!!!Always at yor service!!.")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")

atm_machine()