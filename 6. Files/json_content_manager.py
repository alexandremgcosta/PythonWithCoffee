import json

with open('./6. Files/friends_json.txt', 'r') as file:
    file_contentes = json.load(file) # reads file and turns it to dictionary

print(file_contentes['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('./6. Files/cars_json.txt', 'w') as file:
# Guarda o contéudo do objeto cars no file, no formato JSON.
    json.dump(cars, file)

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

# Carrega e converte a string para um objeto python
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0])