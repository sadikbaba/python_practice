class restaurant():
    def __init__(self, restaurant_name, restaurant_workers ):
        self.restaurant_name = restaurant_name
        self.restaurant_workers = restaurant_workers
    def rest_name(self):
        print(f"Restaurant name is {self.restaurant_name.title()}")
    def rest_workers(self):
        print(f"Restaurant worker is {self.restaurant_workers}")



new_restaurant = restaurant("Hadiza_Balangu", 100)

new_restaurant.rest_name()
new_restaurant.rest_workers()