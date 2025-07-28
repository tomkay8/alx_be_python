shopping_list = []

def display_menu():
while True:
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list.append(item)

    elif choice == '2':
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} is not in the shopping list.")

    elif choice == '3':
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping_list:
                print(f"- {item}")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

