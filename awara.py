# Write a function that accepts a list of items a person want son a sandwich.
# The function should have one parameter
#  that collects as many items as the function call provides,
#  and it should print a summary of the sandwich that is being ordered.
# Call the function three times, using a different number of arguments each time.


def awaraOrder(*awaras):
    for awara in awaras:
        print(f"- {awara}")


awaraOrder("awarancy")
awaraOrder("awara da miya", "awara da yaji", "awara danya")


# Start with a copy of user_profile.py from page 153.
#  Build a profile of yourself by calling build_profile(),
# using your first and last names and three other key-value pairs that describe you


def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile


profile = build_profile(
    "habu", "Aminu", location="Nigeria", field="Software Engineering", hobby="Reading"
)
print(profile)


# Write a function that stores information about a car in a dictionary.
#  The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was stored correctly.


def make_car(manufacturer, model, **car_info):
    car = {}
    car["manufacturer"] = manufacturer
    car["model"] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
