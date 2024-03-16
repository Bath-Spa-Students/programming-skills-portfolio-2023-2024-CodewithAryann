# Define a dictionary of rivers and the countries that flows across
rivers = { 
    "Yangtze": "China",
    "Indus River":"Pakistan",
    "Irtysh River":"Kazakhstan",
    "Citarum River":"Indonesia",
    "Nile":"Egypt", }
# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} flows across {country.title()}.")
# Print the name of each river
print("\n Rivers Name:")
for river in rivers.keys():
    print(f". {river.title()}")
# Print the name of each country
print("\n Countries Name :")
for country in rivers.values():
    print(f". {country.title()}")
    