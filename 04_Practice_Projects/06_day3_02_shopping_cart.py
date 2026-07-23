# shoping  cart:
# using list to store/add items.
cart = []

while True:    
    print("\n===== Shopping Cart =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show Cart")
    print("4. Total Items")
    print("5. Exit")


    choice = input("Enter ur choice(1-5): ")

    if choice == "1": 
        item = input("Enter item to add : ")
        cart.append(item)
        print(f"{item} added to cart .")

    elif choice  == "2":
        item = input("Enter item to remove .")
        if item in cart:
            cart.remove(item)
            print(f"{item} removed successfully .")
        else:
            print("item not found in cart .")


    elif choice =="3":
        if len(cart) == 0:
            print("ur cart is empty .")
        else:
            print("\n---items in cart---")
            for i, item in enumerate(cart,start=1):
                print(f"{i}. {item}")

    elif choice  ==  "4":
        print(f"Total items in cart are :{len(cart)}")


    elif choice == "5":
        print("Thank u for shoping ! ")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
