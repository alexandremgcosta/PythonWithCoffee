class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    # Imaginando que por algum motivo ainda não é possivel
    # implementar este método
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects')
        self.cars.append(car)
    

ford = Garage()
car = Car('Ford', 'Fiesta')
ford.add_car(car)
print(len(ford))