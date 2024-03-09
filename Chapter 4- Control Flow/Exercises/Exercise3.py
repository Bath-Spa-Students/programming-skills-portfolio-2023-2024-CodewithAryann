# Defining the alien's color
alien_color = 'yellow'
# Checking if the alien's color is green
if alien_color == 'green':
    # If the alien's color is green, print this
    print("You got 5 points!")
    # If the alien's color is not green, check if it's yellow
elif alien_color == 'yellow':
     # If the alien's color is yellow, print this
    print("You got 10 points!")
    # If the alien's color is not green or yellow, execute else block
else:
    # Print this statement if the alien's color is different
    print("You got 15 points!")