pets = []

pet = {
    'Dog type': ' Shih Tzu',
    'name': 'Yuki',
    'owner': 'Betty',
    'weight': 20,
    'eats': 'Dog food',
}
pets.append(pet)

pet = {
    'Cat Type': 'Persian Cat',
    'name': 'Bean',
    'owner': 'Ayi',
    'weight': 15,
    'eats': 'Cat Food',
}
pets.append(pet)

pet = {
    'Fish Type': 'Gold Fish',
    'name': 'Bubbles',
    'owner': 'Bella',
    'weight': 2,
    'eats': 'Fish Treats',
}
pets.append(pet)

for pet in pets:
    print("\n This is what I understand, " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))