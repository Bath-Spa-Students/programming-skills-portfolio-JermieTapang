glossary = {
    'string': 'A collection of words.',
    'comment': 'It includes short description.',
    'list': 'function can convert certain types of object to lists.',
    'Sequence': 'an object that contains multiple items of data..',
    'len function': "returns the length of a sequence such as a list.",
    }

for title, definition in glossary.items():
    print("\n" + title.title() + ": " + definition)