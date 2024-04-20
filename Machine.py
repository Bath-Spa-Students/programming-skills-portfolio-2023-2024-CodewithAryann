import time
import sys
import random

# Function to display the menu
def display_menu():
    print("\n\n\n=========/\= Menu =/\=========")
    for category, items in menu.items():
        print(f"{category}:")
        for code, details in items.items():
            print(f"  {code}: {details['item']} - AED{details['price']:.2f} (Stock: {details.get('stock', 'Unlimited')})")

# Function to process a purchase
def process_purchase(selected_item, money_inserted):
    if selected_item in item_codes:
        item_details = item_codes[selected_item]
        if item_details.get('stock', 0) > 0 or item_details.get('stock') is None:
            if money_inserted >= item_details['price']:
                change = money_inserted - item_details['price']
                print(f"Dispensing {item_details['item']}")
                animate_dispense()
                print(f"Change: AED{change:.2f}")
                update_stock(selected_item)
                return True
            else:
                print("\nThe inserted credit is insufficient. Please insert more money.")
                animate_insufficient_funds()
        else:
            print("\nSorry, this item is currently out of stock.")
            animate_out_of_stock()
    else:
        print("\nThe item code inserted is invalid, please enter a valid code.")
        animate_invalid_code()
    return False

# Function to animate dispensing
def animate_dispense():
    for _ in range(3):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print(" Dispensed!")

# Function to animate insufficient funds
def animate_insufficient_funds():
    for _ in range(3):
        print("!", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print(" Please insert more money.")

# Function to animate out of stock
def animate_out_of_stock():
    for _ in range(3):
        print("X", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print(" Out of stock.")

# Function to animate invalid code
def animate_invalid_code():
    for _ in range(3):
        print("?", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print(" Invalid code.")

# Function to update stock after a purchase
def update_stock(selected_item):
    category, code = get_category_and_code(selected_item)
    if 'stock' in menu[category][code]:
        menu[category][code]['stock'] -= 1
    else:
        print(f"Warning: No stock information available for {menu[category][code]['item']}")

# Function to get category and code of an item
def get_category_and_code(selected_item):
    for category, items in menu.items():
        for code in items.keys():
            if code == selected_item:
                return category, code
    return None, None

# Function to display stock status
def display_stock():
    print("\n\n=========\/= Stock Status =\/=========")
    for category, items in menu.items():
        print(f"{category}:")
        for code, details in items.items():
            print(f"  {details['item']} - Stock: {details.get('stock', 'Unlimited')}")

# Function to refill stock
def refill_stock():
    for category, items in menu.items():
        for code, details in items.items():
            if 'stock' in details:
                details['stock'] = 10
    print("Stock has been refilled.")

# Function for the welcome animation
def welcome_animation():
    print("Welcome to the Vending Machine!")
    for _ in range(3):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\nLoading menu...")
    for _ in range(3):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print("\nReady!")

# Function for the thank you animation
def thank_you_animation():
    print("\nThank you for using the Vending Machine!")
    for _ in range(random.randint(3, 5)):
        print("*", end="")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\nHave a great day!")

# Menu of the vending machine
menu = {
    'Drinks': {
        '001': {'item': 'Coca Cola', 'price': 2.50, 'stock': 5},
        '002': {'item': 'Fanta', 'price': 3.00, 'stock': 3},
        '003': {'item': 'Appy Fizz', 'price': 5.50, 'stock': 8},
        '004': {'item': 'Mirinda', 'price': 2.75, 'stock': 7},
        '005': {'item': 'Water', 'price': 1.50, 'stock': 10},
    },
    'Coffe': {
        '006': {'item': 'Espresso', 'price': 7.50, 'stock': 4},
        '007': {'item': 'Mocha', 'price': 4.99, 'stock': 6},
        '008': {'item': 'Cappuccino', 'price': 6.99, 'stock': 9},
        '009': {'item': 'Arabica', 'price': 9.99, 'stock': 2},
        '010': {'item': 'Turkish Coffee', 'price': 8.75, 'stock': 3},
    },
    'Snacks': {
        '011': {'item': 'Cookies', 'price': 4.99, 'stock': 2},
        '012': {'item': 'Popcorn', 'price': 1.50, 'stock': 4},
        '013': {'item': 'Potato Chips', 'price': 3.99, 'stock': 6},
        '014': {'item': 'Crosissant', 'price': 5.99, 'stock': 5},
        '015': {'item': 'Cake', 'price': 13.99, 'stock': 7},
    },
}

# Dictionary to map item codes to their details
item_codes = {}
for category, items in menu.items():
    for code, details in items.items():
        item_codes[code] = details

# Start of the program
welcome_animation()
display_menu()

while True:
    money_inserted = float(input("\nEnter money: AED"))

    selected_item = input("\nEnter the code of the item that you would want to purchase: ")

    transaction_completed = process_purchase(selected_item, money_inserted)

    if transaction_completed:
        print("\nThank you, Please collect your items below and change from the receipt box.")
        time.sleep(2)
    else:
        print("\nTransaction failed. Please try again.")
        time.sleep(2)

    another_purchase = input("\nWould you like to make another purchase? (yes/no): ").lower()
    if another_purchase != 'yes':
        break

    display_stock()

    refill_stock_choice = input("\nWould you like to refill the stock? (yes/no): ").lower()
    if refill_stock_choice == 'yes':
        refill_stock()
        time.sleep(2)

# End of the program
thank_you_animation()