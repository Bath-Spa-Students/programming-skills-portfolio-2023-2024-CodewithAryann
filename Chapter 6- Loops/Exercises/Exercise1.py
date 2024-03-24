# Defining the question prompt
question = "\nWhat topping would you need on your pizza?"
question += "\nEnter 'quit' when you are done with the pizza toppings: "
# Starting a loop
while True:
    # Ask the user for a pizza topping
    pizza_topping = input(question)
     # Check if the user wants to quit
    if pizza_topping!= 'quit':
        # Print a message confirming the addition of the topping
        print(f"  I'll add {pizza_topping} to your pizza.")
    else:
        # If the user enters 'quit', exit the loop
        break