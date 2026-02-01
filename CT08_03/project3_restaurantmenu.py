# Lesson 3 - Restaurant Menu

## Task 1: Display the Menu
# **Display the Menu**

# Write a program that:​
# - Creates a dictionary with at least 5 menu items and their prices.​
# - Prints all the items in the menu with their prices, one item per line.

# ## Task 2: Check if item exists
# **Take the Customer’s Order and Check if it Exists**

# Asks the customer for the item they want to order.​

# Checks if the item exists in the menu.​
# - If it exists: Print the item and its price.​
# - If it does not exist: Display a message saying the item is unavailable.​

# Keep asking again and again until customer says “no more”

# ## Task 3: Add ordered item to another Dictionary
# **Add the Ordered Item to Another Dictionary**

# Extend your program so that it:​
# - If the item exists, asks the customer if they want to add it to their order.​
# If the customer says "yes," ​
# add the item and its price to a separate dictionary that stores the customer’s order.​
# If the customer says "no," ​
# display a message confirming the item was not added.

# ## Task 4: Display Order Summary and Total Cost
# **Display the Order Summary and Total Cost**

# After the customer finishes ordering:​
# - Display all the items in their order with the prices.​
# - Calculate and display the total cost of the order.

# ## Challenge 1: Wallet Feature
# Assign a wallet balance to the customer (e.g., $10).​

# Before confirming an order, check if the total cost will exceed the customer’s wallet balance.​
# - If the total exceeds the wallet balance, display a message and do not add the item.​
# - If the total is within the wallet balance, confirm the order as usual and reduce the balance.

menu = {
    "cheeseburger": 5.50,
    "fries": 3.00,
    "ice cream": 4.00,
    "nuggets": 6.00,
    "coke": 2.00,
}
print("Here's our menu:")
for item, price in menu.items():
    print(f"{item.title()}: ${price:.2f}")

order_item = input("What would you like to order? ").lower()

customer_order = {}
wallet_balance = 10.00
while order_item != "no more":
    if order_item in menu:
        item_price = menu[order_item]
        print(f"{order_item.title()} is available for ${item_price:.2f}.")
        quantity = int(input("How many would you like to order? "))
        add_to_order = input("Would you like to add it to your order? (yes/no) ").lower()
        if add_to_order == "yes":
            if item_price <= wallet_balance:
                customer_order[order_item] = item_price
                wallet_balance -= item_price * quantity
                print(f"{order_item.title()} added to your order. Remaining balance: ${wallet_balance:.2f}")
            else:
                print(f"Sorry, you do not have enough balance to add {order_item.title()}.")
        else:
            print(f"{order_item.title()} was not added to your order.")
    else:
        print(f"Sorry, {order_item.title()} is unavailable.")
    
    order_item = input("What would you like to order? (or type 'no more' to finish) ").lower()
if customer_order:
    print("\nYour order summary:")
    total_cost = 0
    for item, price in customer_order.items():
        print(f"{item.title()}: ${price:.2f}")
        total_cost += price * quantity
        print(f"Total cost: ${total_cost:.2f}")
    print(f"Remaining wallet balance: ${wallet_balance:.2f}")
else:
    print("You did not order anything.")