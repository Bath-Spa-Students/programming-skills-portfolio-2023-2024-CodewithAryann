def describe_city(city, country="Unknown"):
    """Prints a simple sentence describing the city and its country."""
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Lahore", "Pakistan")
describe_city("Ottawa", "Canada")
describe_city("Berlin","Germany")