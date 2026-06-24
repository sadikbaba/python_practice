cities = {
    "Kano": {"location": "Nigeria", "fact": "business"},
    "medina": {"location": "saudi Arabia", "fact": "Mosque of Nabiyy"},
    "Makkah": {"location": "saudi Arabia", "fact": "Hajj & ummarah"},
}
for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"location: {info['location']}")
    print(f"Fact: {info['fact']}")
