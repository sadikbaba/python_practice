# find a car
find_a_car = input("Enter the car you like: ")

print(f"\nlet me see if i can find {find_a_car} for you")

# space for decoration
print("\n")
print("..........................................................")
print("..........................................................")
print("\n")

# restaurant sitting places 
people_waiting = input("How many people are you in total: ")
people_waiting = int(people_waiting)

available_sit = 8
if people_waiting >= available_sit:
    print(f"\nyou have to wait we dont have sit for {people_waiting} now")
elif people_waiting == 1:
    print(f"\nGo to table 6 there sit for {people_waiting} person")
else:
    print(f"\nGo to table 5 there sit for {people_waiting} people")
