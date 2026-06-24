cat = {"first_name": "Whiskers", "last_name": "McFluff", "age": 3, "color": "gray"}
dog = {"first_name": "Buddy", "last_name": "Barkley", "age": 5, "color": "brown"}
goat = {"first_name": "Billy", "last_name": "Goat", "age": 2, "color": "white"}

pets = [cat, dog, goat]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
    print("\n")
