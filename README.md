# GetAllTheItemsinator Python Practice
A test tool that allows for an easy look at where and how to manage every item in the game.

## Understanding the code:
This program should be opened in a Command Prompt/Shell (bash) and is designed to look like a basic bash shell with non-root privileges ("jk$ ")
There are three major files in this project, these files include,
1. GetAllTheItemsinator.py - Where all the main code and logic are stored.
2. items_list.csv - A large table including all the major in-game items (minus potions, trims, etc.)
3. chest_index.csv - A table including the ID of double chests, giving starting and finishing slot numbers. This allows the code to decide which chest an item should be placed in based on its name and ID so it can be sorted alphabetically.

## To-do:
- Update the code where CSV columns are referenced by a friendly name, not by their index.
- Add official item names (e.g., DIAMOND_AXE) to the item_list.csv file.
- Add a checklist feature that allows users to keep track of what they have found and include simple stats.
- Add a sub-CSV for non-stackables, such as potions. Additionally, add armor trims to a sub-CSV.
