def make_shirt(size="large", text="I love Python"):
    """Prints a summary of the size and text printed on a shirt."""
    print(f"The shirt is size: {size} and '{text}' is printed on it.")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", text="Python is awesome!")