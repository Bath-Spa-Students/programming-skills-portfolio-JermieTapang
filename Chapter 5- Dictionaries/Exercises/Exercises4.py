rivers = {
    'Amazon River': 'South Africa',
    'Yangtze River': 'EurAsia',
    'Yenisei River': 'Mongolia',
    'Congo River' : 'Africa',
    'Yellow River': 'China',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- " + country.title())