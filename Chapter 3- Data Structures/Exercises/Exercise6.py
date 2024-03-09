# Storing names of friends in a list called names
names = ["Ali", "Noor", "Asad", "Haris"]

# Printing dinner invitation messages
print("Hey, How are you.", names[0] + "!!! Would you love to have dinner with me?")
print("Hey, How are you.", names[1] + "!!! Would you love to have dinner with me?")
print("Hey, How are you.", names[2] + "!!! Would you love to have dinner with me?")
print("Hey, How are you.", names[3] + "!!! Would you love to have dinner with me?")

# Notifying that only two guests can be invited
print("\nSorry, the dinner table won’t arrive in time, so I can only invite two people for dinner.\n")

# Removing guests one at a time until only two names remain
removed_guest = names.pop()
print("Sorry,", removed_guest + ", I'm unable to invite you to dinner.")

removed_guest = names.pop() 
print("Sorry,", removed_guest + ", I'm unable to invite you to dinner.")

# Printing the invitation messages to the remaining two guests
print("Hey, How are you.", names[0] + "!!! You're still invited to dinner.")
print("Hey, How are you.", names[1] + "!!! You're still invited to dinner.")

# Use del to remove the last two names from the list
del names[-2:]

# Printing the empty list to confirm
print("\nAfter removing all names, the list is now:", names)

