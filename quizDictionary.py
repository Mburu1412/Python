#Mburu Martin
#BSCIT-05-0167/2024

inventory = {}

def add_or_update_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
        print(f"Updated quantity for {item_name}. New quantity: {inventory[item_name]}")
    else:
        inventory[item_name] = quantity
        print(f"Added {item_name} with quantity {quantity}")

def retrieve_item_info(item_name):
    if item_name in inventory:
        print(f"Item: {item_name}, Quantity:{inventory[item_name]}")
    else:
        print(f"{item_name} not found in inventory.")

def calculate_total_quantity():
    total = sum(inventory.values())
    print(f"Total quantity of all items in inventory: {total}")

def main():
    while True:
        print("\n Inventory System Menu:")
        print("1. Add or update item quantity")
        print("2. Retrieve item information")
        print("3. Calculate item quantity")
        print("4. Exit")

        choice = input("Enter your choice (1-4):")

        if choice == '1':
            item_name = input("Enter item name:")
            quantity = int(input("Enter quantity to add/update:"))
            add_or_update_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name: ")
            retrieve_item_info(item_name)
        elif choice =='3':
            calculate_total_quantity()
        elif choice == '4':
            print("Exiting Program.")
            break
        else:
            print("Invalid choice. Please enter a number btwn 1 and 4.")

if __name__ == "__main__":
    main()
    
