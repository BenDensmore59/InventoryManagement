# Inventory Manager Testing


| 1 | Missing inventory file | Rename or temporarily move inventory.txt, then start the program. | Program handles the missing file without crashing and loads an empty inventory. | Program starts without crashing or showing error message. | Pass |

| 2	| View empty inventory | Start with an empty inventory.txt and select option 1. | Displays No inventory items found. | Displayed no inventory items found. | Pass |

| 3 | Add valid item | Enter name Laptop Charger, category Electronics, quantity 8. | Displays Item added successfully. | Displayed item added successfully. | Pass |

| 4 | Reject empty item name | Select Add Item and enter only spaces for the item name. | Displays an error and prompts for the item name again. No item is added. | Displayed an error message. | Pass |

| 5 | Reject duplicate item name | Enter an item name that already exists, but with different capitalization. | Duplicate item is rejected and the user is prompted to enter a different name. | Displayed an error message. | Pass |

| 6 | Reject nonnumeric quantity | Enter 'abc' as the quantity when adding an item. | Error message is displayed, and the user is prompted to enter a valid quantity. | Displayed an error message. | Pass |

| 7 | Reject negative quantity | Enter -5 as the quantity when adding an item. | Negative quantity is rejected, and the user is prompted to enter a valid quantity. | Displayed an error message. | Pass |

| 8 | Update valid item | Select an existing item and enter a new quantity of 15. | Item quantity is updated, a confirmation message displays the item name and new quantity, and changes are saved. | item quanitity was updated and a confirmation message was displayed | Pass |

| 9 | Reject invalid item number | Enter 0 or a number greater than the number of available items when updating or removing an item. | Error message is displayed, and the user is prompted to enter a valid item number. | Error message displayed with confirmation message of outside available range  | Pass |

| 10 | Remove item | Select an existing item to remove. | Item is removed, a confirmation message displays the removed item's name, and changes are saved. | Confirmation item removed: item name message | Pass |

| 11 | Case-insensitive partial search | Search 'cab' in search input when two different cables exist in inventory. | Both matching items are displayed, regardless of capitalization. | Both USB and HDMI cable items displayed as enumerated | Pass |

| 12 | Search with no matches | Search for keyboard when no inventory item contains that name. | Displays no inventory items matched your search. | output matchs expected result | Pass |

| 13 | Verify inventory summary | Use an inventory containing 8 items, a total quantity of 86, 2 low-stock items, and specified category counts. | Displays 8 items, total quantity of 86, 2 low-stock items, and the correct number of items in each category. | output matches expected result | Pass |

| 14 | Verify persistence after restart | Add an item, close the program, restart it, and view the inventory. | Previously saved items and quantities remain in the inventory after restarting. | New item remains in inventory.txt and is displayed by view inventory after restart | Pass |