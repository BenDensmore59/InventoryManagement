# AI Usage Report

## Tools Used

[ChatGPT]

## How AI Was Used

[Function generation, logic, comments for readability, test cases]

## Example Prompts

[How to partition a string from a text file in python. I was struggling with splitting the string and partitioning each part to their respective name, category, quantity]
[How can I count how many items of the same category exist in inventory.txt]
[Add comments for user readability in functions that are long]

## Suggestions Accepted

[Comments for visibility]
[Stronger more concise logic behind program functionality]

## Suggestions Rejected or Modified

[A clear unnecessary suggestion for this project was incorporating external libraries. The assignment didn't require for large scale inventory item validation]

## Verification

[The code was implemented and checked for logical errors and portability issues first]
[The code was then ran and manually tested until the expected result was achieved]

## Code Understanding

[load_inventory first declares a list that will hold the item dictionaries. Then the file is read and interpreted line by line stripping blank spaces. Next a variable that will hold the partitions of the string is declared splitting the string by '|'. Lastly, a dictionary is declared and initialized by using the variable that holds the partitions. The list is then appended with the item dictionaries.]

[search_inventory first takes user input and stores it for later comparison of item names. A simple if statement checks for empty user input, then a list is declared to store the items that have matching names. A loop iterates through each item in inventory and if the user input is found within an item name, then the item item gets appended to the list. Another simple if statement provides a confirmation message when there's no matching item names. Lastly another loop iterates through each item but in the new list that stores matched item names and gets formatted and enumerated.]