# Defining the person's age
person_age = 20
# Check if the person is a baby
if person_age < 2:
    print("You are a baby!")
 # If not a baby, check if the person is a toddler 
elif person_age < 4:
    print("You are a toddler!")
# If not a toddler, check if the person is a kid    
elif person_age < 13:
    print("You are a kid!")
# If not a kid, check if the person is a teenager     
elif person_age < 20:
    print("You are a teenager!")
# If not a teenager, check if the person is an adult    
elif person_age < 65:
    print("You are an adult!")
# If not an adult, the person must be an elder    
else:
    print("You are an elder!")