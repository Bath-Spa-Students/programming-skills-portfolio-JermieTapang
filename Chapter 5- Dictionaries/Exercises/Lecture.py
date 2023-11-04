dictionary = {}
print (dictionary, type(dictionary))

example = {'name' : 'James', 'number' :'65', 'school' : 'FEPS'}
print (example)

dictionary = {'fruit' : 'Mango', 'school' : 'FEPS', 'name' : 'Cassy'}
print(dictionary.get("name"))

dictionary = {'fruit' : 'Mango', 'school' : 'FEPS'}
print(dictionary.get("name", "Jacob"))

dictionary = {'fruit' : 'Mango',  'school' : 'FEPS',  'item' : 'pillow'}
print(dictionary.items())

dictionary = {'fruit' : 'Mango',  'school' : 'FEPS',  'item' : 'pillow'}
print(dictionary.keys())

things = {'House' : 'Bungalo', 'item' : 'shovel', 'equipment' : 'power tool'}
print (things, type(dictionary))

name = {'name' : 'Vince', 'school' : 'Olfu', 'brand' : 'Nido'}
print (name["name"],type(dictionary))

fruit = { 'fruit' : 'Melon', 'round' : 'Orange', 'spiky' : 'Durian'}
print (fruit["spiky"])

place = { 'country' : 'Canada', 'city' : 'Manila', 'town' : 'Tugatog'}
print (place.get("town"))

place = { 'country' : 'Canada', 'city' : 'Manila', 'town' : 'Tugatog'}
print (place.get("name", "Dave "))

place = { 'country' : 'Canada', 'city' : 'Manila', 'town' : 'Tugatog'}
print (place.items())

place = { 'country' : 'Canada', 'city' : 'Manila', 'town' : 'Tugatog'}
print (place.keys())

