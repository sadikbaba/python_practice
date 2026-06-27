magician_list = ["alice", "david", "carolina"]


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


show_magicians(magician_list)

print("\n")


def greet_magicians(magicians):
    for magician in magicians:
        print(f"Hello, {magician.title()} you are great magician!")


greet_magicians(magician_list)


# Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original names
# and one list with the Great added to each magician’s name.


def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magicians.append(f"Great {magician.title()}")
    return great_magicians


make_great_magicians = make_great(magician_list)
show_magicians(magician_list)
print("\n")
show_magicians(make_great_magicians)
