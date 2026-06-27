# Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
#  you like that could represent how many customers were served in, say, a day of business.


class Restaurant:
    def __init__(self, restaurant_name, restaurant_workers):
        self.restaurant_name = restaurant_name
        self.restaurant_workers = restaurant_workers
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name.title()}")

    def number_of_workers(self):
        print(f"Restaurant worker is {self.restaurant_workers}")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

    def get_number_served(self):
        return self.number_served


new_restaurant = Restaurant("Hadiza_Balangu", 100)

print(
    f"we have {new_restaurant.get_number_served()} customers served in our restaurant"
)  # 0

new_restaurant.describe_restaurant()
new_restaurant.number_of_workers()
new_restaurant.set_number_served(50)
new_restaurant.increment_number_served(20)
print(
    f"we have {new_restaurant.get_number_served()} customers served in our restaurant"
)
