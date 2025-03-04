shopping_list =[]

while True:
    print("\nMenu: ")
    print("1. View items")
    print("2. Add items")
    print("3. Remove items")
    print("4. Exit")
    choice = input("Please choose an option (1/2/3/4): ")
    if choice == '1':
        if len(shopping_list) > 0:
            print("Here is your shopping items \n")
            for item in shopping_list:
                print(item)
        else:
            print("Your cart is empty")

    elif choice == '2':
        while True:
            new_item = input("\nEnter the item to add: ")
            if new_item == "done":
                print("Ok, all your itmes have added to your shopping list")
                break
            else:
                shopping_list.append(new_item)
                print(f"{new_item} has been added.")

    # Option 3: Remove item
    elif choice == '3':
        item_to_remove = input("\nEnter the item to remove: ")
        if item_to_remove == "done":
            print("Your items have successfully been removed from your shopping list")
            break
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            print(f"{item_to_remove} has been removed.")
        else: 
            print("The item you are trying to remove is not in shopping list")
      
        
            
    

    # Option 4: Exit

    elif choice == '4':
        print("Exiting the program. Thanks for shopping with us!")
        break  # Exit the loop and end the program
        
    # else:
    #     print("Invalid option. Please choose a valid option (1/2/3/4).")
    



        

