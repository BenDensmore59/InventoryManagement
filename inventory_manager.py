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
            inventory = load_inventory(INVENTORY_FILE)
            for item in inventory:
                print(f"{item},")

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
    


#def save_inventory(inventory, filename):



#def view_inventory(inventory):



#def add_item(inventory):


#def update_quantity(inventory):


#def remove_item(inventory):


#def search_inventory(inventory):



#def display_summary(inventory):


if __name__ == "__main__":
    main()


