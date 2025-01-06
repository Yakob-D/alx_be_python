def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)
        elif choice == 2:
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
            else:
                print("Item not found.")
        elif choice == 3:
            if len(shopping_list) == 0:
                print("Shopping list is empty.")
            else:
                for item in shopping_list:
                    print(f"Item : {item}")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
