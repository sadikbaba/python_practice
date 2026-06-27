# Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating
#  that the restaurant is open. Make an instance called restaurant from your class.
# Print the two attributes individually, and then call both methods.


class restaurant:
    def __init__(self, restaurant_name, restaurant_workers):
        self.restaurant_name = restaurant_name
        self.restaurant_workers = restaurant_workers

    def rest_name(self):
        print(f"Restaurant name is {self.restaurant_name.title()}")

    def rest_workers(self):
        print(f"Restaurant worker is {self.restaurant_workers}")


new_restaurant = restaurant("Hadiza_Balangu", 100)

new_restaurant.rest_name()
new_restaurant.rest_workers()


# Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.


class User:
    def __init__(self, firstName, lastName, gender):
        self.firstName = firstName.title()
        self.lastName = lastName.title()
        self.gender = gender.lower()

    def describe_User(self):
        if self.gender == "woman":
            print(f"{self.firstName} {self.lastName} is woman")
        elif self.gender == "man":
            print(f"{self.firstName} {self.lastName}is Man")
        else:
            print(
                f"imagine unserios {self.firstName} {self.lastName} did'nt know his gender he choose{self.gender}"
            )

    def greet_user(self):
        if self.gender == "woman":
            print(f"good morning Madam {self.firstName} {self.lastName}")
        elif self.gender == "man":
            print(f"good morning gentleman {self.firstName } {self.lastName}")
        else:
            print(
                f"Hey {self.firstName} {self.lastName} we didnt greet coward. go an know your gender.\n we rather greet animal that this bullshit gender '{self.gender}'"
            )


new_user = User("habiba", "musa", "a")

new_user.describe_User()
new_user.greet_user()
