animals = [
    {"name": "dog", "type": "animal", "nol": 4},
    {"name": "cat", "type": "animal", "nol": 4},
    {"name": "pigeon", "type": "animal", "nol": 2},
    {"name": "mosqueto", "type": "animal", "nol": 6},
    {"name": "snake", "type": "animal", "nol": None},
]

for animal in animals:
    print(animal['name'], animal['type'], animal['nol'])
