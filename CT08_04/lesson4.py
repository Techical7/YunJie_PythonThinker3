# # Lesson 4 - Bookshop Ordering System (BOS)

# ## Task 1: Create the Menu
# **Display the Menu**

# Write a program that:​
# - Shows a list of school supplies and their prices.​
# - Create a dictionary with items as keys and prices as values (e.g., {"Notebook": 2.50, "Pencil": 0.50} ).​
# - Use a loop to display each item and its price.

# menu = {
#     "Notebook": 2.50,
#     "Pencil": 0.50,
#     "Eraser": 0.80,
#     "Ruler": 1.00,
#     "Backpack": 25.00,
#     "Calculator": 35.00
# }
# for item, price in menu.items():
#     print(f"{item}: ${price:.2f}")


# ## Task 2: Check if item exists
# **Take the Customer’s Order and Check if it Exists​**

# Extend the previous program that:​
# - Asks the customer for the item they want to order.​- Checks if the item exists in the menu.​
#     - If it exists: Print the item and its price.​
#     - If it does not exist: Display a message saying the item is unavailable.​
# - Keep asking again and again until customer says “no more”

# menu = {
#     "notebook": 2.50,
#     "pencil": 0.50,
#     "eraser": 0.80,
#     "ruler": 1.00,
#     "backpack": 25.00,
#     "calculator": 35.00
# }

# print("=== Menu ===")
# for item, price in menu.items():
#     print(f"{item}: ${price:.2f}")
# print()

# order = {}
# while True:
#     item = input("Enter the item you want to order (or type 'no more' to finish): ").strip().lower()
#     if item == "no more":
#         break
#     if item in menu:
#         print(f"{item} is available at ${menu[item]:.2f}.")
        
#         add_to_order = input(f"Do you want to add {item} to your order? (yes/no): ").strip().lower()
#         if add_to_order == "yes":
#             order[item] = menu[item]
#             print(f"{item} has been added to your order.")
#         else:
#             print(f"{item} was not added to your order.")
#     else:
#         print(f"Sorry, {item} is unavailable.")

# ## Task 3: Add ordered items to another dictionary
# **Add the Ordered Item to Another Dictionary​**

# Extend your program so that it:​
# - If the item exists, asks the customer if they want to add it to their order.​
#     - If the customer says "yes," ​
#         - add the item and its price to a separate dictionary that stores the customer’s order​
#     - If the customer says "no," ​
#         - display a message confirming the item was not added.

# menu = {
#     "notebook": 2.50,
#     "pencil": 0.50,
#     "eraser": 0.80,
#     "ruler": 1.00,
#     "backpack": 25.00,
#     "calculator": 35.00
# }

# print("=== Menu ===")
# for item, price in menu.items():
#     print(f"{item}: ${price:.2f}")
# print()

# order = {}
# while True:
#     item = input("Enter the item you want to order (or type 'no more' to finish): ").strip().lower()
#     if item == "no more":
#         break
#     if item in menu:
#         print(f"{item} is available at ${menu[item]:.2f}.")
        
#         add_to_order = input(f"Do you want to add {item} to your order? (yes/no): ").strip().lower()
#         if add_to_order == "yes":
#             order[item] = menu[item]
#             print(f"{item} has been added to your order.")
#         else:
#             print(f"{item} was not added to your order.")
#     else:
#         print(f"Sorry, {item} is unavailable.")

# print("\n=== Order Summary ===")
# if order:
#     for item, price in order.items():
#         print(f"{item}: ${price:.2f}")
#     total = sum(order.values())
#     print(f"Total Cost: ${total:.2f}")
# else:
#     print("Your order is empty.")

# ## Task 4: Display Order Summary and Total Cost
# **Display the Order Summary and Total Cost​**

# After the customer finishes ordering:​
# - Display all the items in their order with the prices.​
# - Calculate and display the total cost of the order.

menu = {
    "notebook": 2.50,
    "pencil": 0.50,
    "eraser": 0.80,
    "ruler": 1.00,
    "backpack": 25.00,
    "calculator": 35.00
}

print("=== Menu ===")
for item, price in menu.items():
    print(f"{item}: ${price:.2f}")
print()

order = {}
while True:
    item = input("Enter the item you want to order (or type 'no more' to finish): ").strip().lower()
    if item == "no more":
        break
    if item in menu:
        print(f"{item} is available at ${menu[item]:.2f}.")
        add_to_order = input(f"Do you want to add {item} to your order? (yes/no): ").strip().lower()
        if add_to_order == "yes":
            if item in order:
                order[item] += menu[item]
            else:
                order[item] = menu[item]
        elif add_to_order == "no":
            print(f"{item} has been added to your order.")
        else:
            print(f"please enter a valid response (yes/no).")
            # what is the possible of this code
            # if print(f"please enter a valid response (yes/no).")
            print(f"Do you want to add {item} to your order? (yes/no): ").strip().lower()
    else:
        print(f"Sorry, {item} is unavailable.")

print("\n=== Order Summary ===")
if order:
    for item, price in order.items():
        print(f"{item}: ${price:.2f}")
    total = sum(order.values())
    print(f"Total Cost: ${total:.2f}")
else:
    print("Your order is empty.")

# Do the following challenges if possible
# ## Challenge 1: Track Quantities of Items
# Allow the customer to specify how many of each item they want to buy.​
# Store both the item and quantity in a nested dictionary.​
# - purchases = ​{"Notebook": {"quantity": 2, "cost": 5.00}}​
# Calculate the total cost based on quantities.

# ## Challenge 2: Apply Discounts
# The goal of this challenge is to introduce a discount system to your program, allowing customers to receive a percentage discount if their total spending exceeds a certain threshold.​
# - Example: If the customer spends more than $20, they get a 10% discount on their bill.

