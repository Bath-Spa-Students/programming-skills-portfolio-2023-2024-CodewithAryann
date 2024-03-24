# List of sandwich orders
sandwich_orders = ['Club sandwich', 'Chicken sandwich', 'Texas sandwich', 'Falafel','Cheesesteak','Gyros']
# Empty list to hold finished sandwiches
finished_sandwiches = []
# Loop through each sandwich in the sandwich_orders list
for sandwich in sandwich_orders: 
    # Print a message for each sandwich order
    print(f"I'm making your {sandwich}.\n")
# Assign the sandwich_orders list to finished_sandwiches
finished_sandwiches = sandwich_orders
# Print a text for the list of sandwiches made
print ("List of sandwiches prepared:")
print ("__________________________________")
# Loop through each sandwich in the finished_sandwiches list and print them
for sandwhich in finished_sandwiches:
    print (sandwhich)