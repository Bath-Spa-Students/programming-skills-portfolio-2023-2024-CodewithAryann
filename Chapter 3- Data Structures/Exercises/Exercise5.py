# Storing names of friends in a list called names
names=["Ali","Noor","Asad","Haris"]
# Printing a personalized dinner invitation message to the first friend in the list (index 0)
print("Hey, How are you.",names[0]+"!!! Would you love to have dinner with me?")
# Printing a personalized dinner invitation message to the first friend in the list (index 0)
print("Hey, How are you.",names[1]+"!!! Would you love to have dinner with me?")
# Printing a personalized dinner invitation message to the first friend in the list (index 0)
print("Hey, How are you.",names[2]+"!!! Would you love to have dinner with me?")
# Printing a personalized dinner invitation message to the first friend in the list (index 0)
print("Hey, How are you.",names[3]+"!!! Would you love to have dinner with me?")

# Printing the name of the guest who can't make it
guest_cant_make_it = names[2]  # Asad can't make it
print(guest_cant_make_it + " can't make it to the dinner.")

# Replacing the name of the guest who can't make it to dinner
replacement_guest = "Zainab"  # New person to invite
names[2] = replacement_guest

# Printing updated invitation messages
print("\nUpdated invitation messages:")
print("---------------------------------------------------------------")
print("Hey, How are you.",names[0]+"!!! Would you love to have dinner with me?")
print("Hey, How are you.",names[1]+"!!! Would you love to have dinner with me?")
print("Hey, How are you.",names[2]+"!!! Would you love to have dinner with me?")
print("Hey, How are you.",names[3]+"!!! Would you love to have dinner with me?")

