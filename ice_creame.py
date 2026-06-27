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


# An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

from oop import User

class Admin(User):
    def __init__(self, firstName, lastName, gender, privileges):
        super().__init__(firstName, lastName,gender)
        self.privileges = privileges

    def show_privileges(self):
        print(f"Admin privileges: {', '.join(self.privileges)}")
    


admin_user = Admin("John", "Doe", "man", ["can add post", "can delete post", "can ban user"])
admin_user.describe_User()
admin_user.show_privileges()    