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
        elif choice == "3":
            print("Updating item quantity...\n")
            update_quantity(load_inventory(INVENTORY_FILE))
        elif choice == "4":
            print("Removing an item...\n")
            remove_item(load_inventory(INVENTORY_FILE))
        elif choice == "5":
            print("Searching inventory...\n")
            search_inventory(load_inventory(INVENTORY_FILE))

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


def update_quantity(inventory):
    # Check whether the inventory is empty
    if not inventory:
        print("No inventory items found.")
        return

    # Display the numbered inventory
    view_inventory(inventory)

    # Ask which item to update
    while True:
        item_input = input("Enter the item number to update: ").strip()

        if not item_input.isdigit():
            print("Error: Please enter a valid item number.")
            continue

        item_number = int(item_input)

        if item_number < 1 or item_number > len(inventory):
            print("Error: Item number is outside the available range.")
            continue

        break

    # Ask for the new quantity
    while True:
        quantity_input = input("Enter the new quantity: ").strip()

        if not quantity_input.isdigit():
            print("Error: Quantity must be a non-negative whole number.")
            continue

        new_quantity = int(quantity_input)
        break

    # Update the correct dictionary
    item = inventory[item_number - 1]
    item["quantity"] = new_quantity

    # Save the updated inventory
    save_inventory(inventory, INVENTORY_FILE)

    # Display confirmation
    print(f"{item['name']} quantity updated to {new_quantity}.")


def remove_item(inventory):
    # Check whether the inventory is empty
    if not inventory:
        print("No inventory items found.")
        return

    # Display the numbered inventory
    view_inventory(inventory)

    # Ask which item to remove
    while True:
        item_input = input("Enter the item number to remove: ").strip()

        if not item_input.isdigit():
            print("Error: Please enter a valid item number.")
            continue

        item_number = int(item_input)

        if item_number < 1 or item_number > len(inventory):
            print("Error: Item number is outside the available range.")
            continue

        break

    # Remove the selected item
    removed_item = inventory.pop(item_number - 1)

    # Save the updated inventory
    save_inventory(inventory, INVENTORY_FILE)

    # Display confirmation
    print(f"Item removed: {removed_item['name']}")


def search_inventory(inventory):
    search_term = input("Enter an item name to search for: ").strip()

    # Reject empty searches
    if not search_term:
        print("Error: Search term cannot be empty.")
        return

    # Find every item whose name contains the search term
    matches = []

    for item in inventory:
        if search_term.lower() in item["name"].lower():
            matches.append(item)

    # Display the results
    if not matches:
        print("No inventory items matched your search.")
        return

    for number, item in enumerate(matches, start=1):
        print(f"{number}. {item['name']} | {item['category']} | {item['quantity']}")



#def display_summary(inventory):


if __name__ == "__main__":
    main()


