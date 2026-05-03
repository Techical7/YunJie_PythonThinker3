customer_spending = {
    "Alice": 950, 
    "Bob": 1200, 
    "Charlie": 500, 
    "Diana": 1800, 
    "Ethan": 2200, 
    "Fiona": 700, 
    "John": 685, 
    "Hor Kee": 1389, 
    "Siew Ling": 235, 
    "Matt": 452, 
    "Kristen": 985, 
    "Johnson": 785, 
    "Charles": 2352, 
    "Tommy": 741, 
    "Laura": 689
    }

print(customer_spending)
for name, spending in customer_spending.items():
    if spending > 999:
        print("Hi " + name + ", you are now a VIP! Congratulations!")
    else:
        amount_needed = 1000 - spending
        print("Hi " + name + ", spend $" + str(amount_needed) + " more to become a VIP member")