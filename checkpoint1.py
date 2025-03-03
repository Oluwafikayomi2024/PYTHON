def pizza_order():
    print("Welcome to Python Pizza Deliveries")

    size = input("What size of pizza do you want? (small/medium/large): ").lower()
    pepperoni = input("Would you like pepperoni on your pizza? (yes/no): ").lower()
    extra_cheese = input("Would you like some extra cheese? (yes/no): ").lower()

    # Initialize base price for each size
    if size == "small":
        price = 15
    elif size == "medium":
        price = 20
    elif size == "large":
        price = 25
    else:
        print("You can only select from the above listed sizes")
        return  # Stop the function if the size is invalid

    # Add extra charges for toppings
    if pepperoni == "yes":
        price += 2
    if extra_cheese == "yes":
        price += 1

    # Display the total price
    print(f"Your total bill is: ${price}")

pizza_order()

