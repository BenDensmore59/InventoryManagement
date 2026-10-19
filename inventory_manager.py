INVENTORY_FILE = "inventory.txt"


def main():
    print(display_menu())



def display_menu():
    while True:
        print("\nInventory Manager")
        print("\n1. View inventory")
        print("2. Add an item")
        print("3. Update an item quantity")
        print("4. Remove an item")
        print("5. Search inventory")
        print("6. View inventory summary")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if not choice.isdigit() or not 1 <= int(choice) <= 7:
            print("Error: Please enter a number between 1 and 7.")
            continue
        elif choice == "1":
            print("Viewing inventory...\n")
            view_inventory(load_inventory(INVENTORY_FILE))
        elif choice == "2":
            print("Adding an item...\n")
            add_item(load_inventory(INVENTORY_FILE))
            

        elif choice == "7":
            print("Exiting the program.")
            break

    return int(choice)



def load_inventory(filename):
    inventory = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split("|")

                item = {
                    "name": parts[0],
                    "category": parts[1],
                    "quantity": int(parts[2])
                }

                inventory.append(item)

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return []

    return inventory
    


def save_inventory(inventory, filename):
    with open(filename, "w") as file:
        for item in inventory:
            file.write(
                f"{item['name']}|{item['category']}|{item['quantity']}\n"
            )



def view_inventory(inventory):
    if not inventory:
        print("No inventory items found.")
        return

    for number, item in enumerate(inventory, start=1):
        print(f"{number}. {item['name']} | {item['category']} | {item['quantity']}")



def add_item(inventory):
    # Ask for the item name
    while True:
        name = input("Enter item name: ").strip()

        if not name:
            print("Error: Item name cannot be empty.")
        elif "|" in name:
            print("Error: Item name cannot contain '|'.")
        elif any(item["name"].lower() == name.lower() for item in inventory):
            print("Error: An item with that name already exists.")
        elif name.isdigit():
            print("Error: Item name cannot be a number.")
        else:
            break

    # Ask for the category
    while True:
        category = input("Enter category: ").strip()

        if not category:
            print("Error: Category cannot be empty.")
        elif "|" in category:
            print("Error: Category cannot contain '|'.")
        elif category.isdigit():
            print("Error: Category name cannot be a number.")
        else:
            break

    # Ask for the quantity
    while True:
        quantity_input = input("Enter quantity: ").strip()

        if not quantity_input.isdigit():
            print("Error: Quantity must be a non-negative whole number.")
        else:
            quantity = int(quantity_input)
            break

    # Create the new item dictionary
    new_item = {
        "name": name,
        "category": category,
        "quantity": quantity
    }

    # Add the item to the inventory list
    inventory.append(new_item)

    # Save the updated inventory to the file
    save_inventory(inventory, INVENTORY_FILE)

    print("Item added successfully.")


#def update_quantity(inventory):


#def remove_item(inventory):


#def search_inventory(inventory):



#def display_summary(inventory):


if __name__ == "__main__":
    main()


