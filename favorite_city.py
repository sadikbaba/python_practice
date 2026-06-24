person_1 = {"umar": "Makkah"}
person_2 = {"Ahmad": "medina"}
person_3 = {"Sadik": "kano"}

people = [person_1, person_2, person_3]


for person in people:
    for name, favCIty in person.items():
        print(f"\nName: {name.title()}. \nFavorite city: {favCIty.title()}")
