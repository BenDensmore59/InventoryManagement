# InventoryManager

Program that allows for inventory management, updating, and viewing

## Current Features

-[Inventory adding]
-[Inventory item removal]
-[Inventory viewing]
-[Inventory summary]
-[Updating inventory quantity]
-[Inventory summary]
-[Persistent inventory storage]

## Requirements

-[Python 3]
-[Inventory.txt file]

## Project Files

-`inventory_manager.py` — Main file that holds all the features
-`inventory.txt` — Where the inventory items are stored
-`.gitignore` — Files that are to be ignored by git

## Running the Program

[A terminal can be opened from the upper left "Terminal" tab]

```text
[python inventory_manager.py]
```

## Task Persistence

-[Items are loaded from and saved to inventory.txt]

## Inventory Format

-[Name | Category | Quantity]

## Menu options

-[Inventory Manager]

-[1. View inventory]
-[2. Add an item]
-[3. Update an item quantity]
-[4. Remove an item]
-[5. Search inventory]
-[6. View inventory summary]
-[7. Exit]

## Sample Interaction

-[Enter your choice (1-7): 2]
-[Adding an item...]
-[Enter item name: Toothbrush]
-[Enter category: Personal Care]
-[Enter quantity: 7]
-[Item added successfully.]

## Current Limitations

-[Strict formatting rules tied to the dictionary structure]
-[Limited item identification. Nothing is identified by an id, thus adding two of the same type of item will be rejected for sharing the same general name.]
-[Data storage is dependent on the inventory.txt file]

## Testing Summary

-[All tests ran are located in TESTING.md]
-[No logical errors found when testing functions and their boundaries]

## Future Improvements

-[Adding unique ID's for each item]
-[Improved file validation, less reliance on inventory.txt]

## Version Control

[The project uses git and github to upload to a cloud repository from a local repository. Changes can be committed, and then pushed to the cloud repository on github. To update the project locally pull the latest updated version from github]
