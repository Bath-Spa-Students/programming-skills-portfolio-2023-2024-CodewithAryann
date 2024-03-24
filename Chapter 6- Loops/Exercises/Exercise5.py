# List of sandwich orders
sandwich_orders = ['Club sandwich', 'Chicken sandwich', 'Pastrami', 'Texas sandwich', 'Falafel', 'Pastrami', 'Cheesesteak', 'Gyros', 'Pastrami']

# List of finished sandwiches
finished_sandwiches = []

# Print a message that the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami sandwiches.")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Loop for each sandwich in the sandwich_orders list
for sandwich in sandwich_orders:
    # Print a message for each sandwich order
    print(f"I'm making your {sandwich}.")

    # Add the sandwich to the finished_sandwiches list
    finished_sandwiches.append(sandwich)

# Print the list of sandwiches made
print("List of sandwiches prepared:")
print("____________________________")

# Loop for each sandwich in the finished_sandwiches list and print them
for sandwich in finished_sandwiches:
    print(sandwich)
