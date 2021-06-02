# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional} for filter
# dictionary = {key: (if/else) for (key, value) in iterable} for new value return
# dictionary = {key: function(value) for (key, value) in iterable}

cities_in_F = {"New York": 32,
               "Boston": 75,
               "Los Angeles": 100,
               "Chicago": 50}

# To convert the list into a new list from F to C
# specify the formula in the expression part
# Use: dictionary = {key: expression for (key, value) in iterable}
cities_in_C = {key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)  # {'New York': 0, 'Boston': 24, 'Los Angeles': 38, 'Chicago': 10}

# ----------------------------------------------------------------------------------------------------

# Use: dictionary = {key: expression for (key, value) in iterable if conditional} for filter
weather = {"New York": "snowing",
           "Boston": "sunny",
           "Los Angeles": "sunny",
           "Chicago": "cloudy"}
cities_sunny = {key: value for (key, value) in weather.items() if value == "sunny"}
print(cities_sunny)  # {'Boston': 'sunny', 'Los Angeles': 'sunny'}

# ----------------------------------------------------------------------------------------------------

# Use: dictionary = {key: (if/else) for (key, value) in iterable} for new value return
desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities_in_F.items()}
print(desc_cities)  # {'New York': 'COLD', 'Boston': 'WARM', 'Los Angeles': 'WARM', 'Chicago': 'WARM'}


# ----------------------------------------------------------------------------------------------------

def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"


# Use: dictionary = {key: function(value) for (key, value) in iterable}
desc_cities2 = {key: check_temp(value) for (key, value) in cities_in_F.items()}
print(desc_cities2)  # {'New York': 'COLD', 'Boston': 'HOT', 'Los Angeles': 'HOT', 'Chicago': 'WARM'}
