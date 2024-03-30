def make_shirt(size, text):
    # This function prints a summary of the size and text printed on a shirt.
    print("The shirt is size: " + size + " and '" + text + "' is printed on it.")
# Call the function using positional
make_shirt("XL", "King.") 
# Call the function with keyword arguments
make_shirt(size="small",text="Queen")