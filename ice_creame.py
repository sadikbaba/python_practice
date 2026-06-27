# An ice cream stand is a specific kind of restaurant.
#  Write a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

import oop_assignment as restaurant

class IceCreamStand(restaurant.Restaurant):
    def __init__(self, restaurant_name, restaurant_workers, flavors):
        super().__init__(restaurant_name, restaurant_workers)
        self.flavors = flavors

    def display_flavors(self):
        print(f"Available ice cream flavors: {', '.join(self.flavors)}")

ice_cream_stand = IceCreamStand("Sweet Treats", 5, ["Vanilla", "Chocolate", "Strawberry", "Mint"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()