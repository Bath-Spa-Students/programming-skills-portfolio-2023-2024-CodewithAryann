# Define dictionaries of different pets
pet1 = {"type": "Dog", "owner-name": "Ali"}
pet2 = {"type": "Cat", "owner-name": "Haris"}
pet3 = {"type": "Parrot", "owner-name": "Saad"}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3]

# Loop of the list and print information of each pet
for pet in pets:
    print(f"type: {pet["type"]}")
    print(f"Owner: {pet["owner-name"]}")
    print()  # Print a blank line after every pet's information