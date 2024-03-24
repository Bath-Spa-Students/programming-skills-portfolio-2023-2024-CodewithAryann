while True:
    user_age = input("Enter your age (or 'quit' to exit): ")

    # Check if the user wants to quit
    if user_age.lower() == 'quit':
        break

    # Convert age to an integer
    user_age = int(user_age)

    # Ticket price based on age
    if user_age < 3: # Age is less than 3 
        print("Your ticket is free.")
    elif user_age >= 3 and user_age <= 12:# Age is between 3 and 12 
        print("Your ticket costs $10.")
    else: # Age is more than 12
        print("Your ticket costs $15.")
