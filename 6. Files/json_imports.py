import json

file = open('./6. Files/friends_json.txt', 'r')
file_contentes = json.load(file) # reads file and turns it to dictionary
file.close()

print(file_contentes['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('./6. Files/cars_json.txt', 'w')
# Guarda o contéudo do objeto cars no file, no formato JSON.
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'

# Carrega e converte a string para um objeto python
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0])