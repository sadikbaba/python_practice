person_1_favorite_language = {
    "Ahmad": "economic",
}

poll_people = ["Ahmad", "Aliyu", "sadik", "Maryam"]

for name in poll_people:
    if name in person_1_favorite_language:
        print(f"Thank you {name} for taking the poll.")
    else:
        print(f"{name}, please take the favorite language poll.")


print("\n")

person_2_favorite_language = {"sadik": "Math"}

person_3_favorite_language = {"umar": "computer science"}

people_list = [
    person_1_favorite_language,
    person_2_favorite_language,
    person_3_favorite_language,
]

for person in people_list:
    for name, language in person.items():
        print(f"{name.title()}'s favorite language is {language.title()}.")
