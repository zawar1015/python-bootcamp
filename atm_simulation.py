# ATM Simulation
# initial balance =10000

print("------------------")
current_balance =10000.00

while True:
    print("==== ATM MENU ====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("==================================")


    choice = input("Enter your choice : (1-4): ")

    if choice == "1":
        print(f"Currenct Balance is. {current_balance}")
        print("==================================")
    elif choice == "2":
        d_amount = float(input("Enter amount u want to deposit."))
        
        if d_amount >0:
            current_balance+=d_amount
            print(f"Rs.{d_amount} deposited successfully")
            print(f"Your current balance is Rs.{current_balance}")
            print("==================================")
        else:
            print("invalid input.")
            print("==================================")


    elif choice == "3":
        w_amount = float(input("Enter amount u want to withdraw."))

        if w_amount <current_balance:
            current_balance-= w_amount
            print(f"Rs.{w_amount} withdrawl successfully.")
            print(f"Your current balance is Rs.{current_balance}")
            print("==================================")
        else:
            print("invalid input.")
            print("==================================")
    elif choice == "4":
        print("Thank u for using ATM.")
        break

    else:
        print("invalid choice. please select (1-4)")


