# This program will calculate the total stock value for each item on the menu below
menu = ["croissants", "coffee", "cakes", "juice"]

# Dictionary displaying the quantity for each menu item in the cafe
stock = {'croissants': 20,
              'coffee': 55,
              'cakes': 15,
              'juice': 30
              }
# Prints the dictionary to the user with an explanation of what the dictionary shows.
for item in stock:
    print(f"The current stock quantity for {item} is: {stock[item]}")
    # The following string variable will also print the same  output.
    # stock_cost = f'The current stock quantity is {stock[item]} x {item}'
    # print(stock_cost)

# Dictionary displaying cost for each item on the menu in the cafe.
price = {'croissants': 2.5,
              'coffee': 3,
              'cakes': 4,
              'juice': 3.5
              }
# Prints the dictionary to the user with an explanation of what the dictionary shows.
for item in price:
    print(f"The price for {item} is: £{price[item]}")

# Creates new dictionary to display the total stock worth for each item on the menu in the cafe.
total_stock = {}

# For loop through each item in the dictionary.
for key in stock:
    # Multiplies each stock item value by the price value.
    stock[key] = stock.get(key) * price.get(key)
    # Adds each new tuple to the new dictionary.
    total_stock.update(stock)

# Prints the total stock dictionary back to the user with an explanation of what the dictionary shows.
for item in total_stock:
    print(f"The total stock worth for {item} will be: {total_stock[item]}")

# Alternative method:
def total(stock, price):
    total_stock += stock[key] * price[key]
print(f"Total stock worth for each item on the menu will be: {total_stock}")