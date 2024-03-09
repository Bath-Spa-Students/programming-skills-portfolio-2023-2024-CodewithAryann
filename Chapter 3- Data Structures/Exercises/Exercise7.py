# List of places
places = ['Maldives', 'Zurich', 'Rome', 'Istanbul', 'Niagara Falls']

# Printing the original order of the list
print("Original Order:")
print(places)

# Sorting the list alphabetically using sorted() and printing the result
print("\nAlphabetical:")
print(sorted(places))

# Printing the original order of the list
print("\nOriginal Order:")
print(places)

# Sorting the list in reverse alphabetical order using sorted()
print("\nReverse Alphabetical:")
print(sorted(places, reverse=True))

# Printing the original order of the list
print("\nOriginal Order:")
print(places)

# Reversing the order of the list using reverse()
print("\nReversed:")
places.reverse()
print(places)

# Reversing the order of the list again to revert to the original order
print("\nOriginal Order:")
places.reverse()
print(places)

# Sorting the list alphabetically in place using sort()
print("\nAlphabetical:")
places.sort()
print(places)

# Sorting the list in reverse alphabetical order in place using sort()
print("\nReverse Alphabetical:")
places.sort(reverse=True)
print(places)