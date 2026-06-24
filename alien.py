aliens = []

for aliens_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[0:10]:
    print(alien)

print("\n....")

print(f"Total number of aliens: {len(aliens)}")
