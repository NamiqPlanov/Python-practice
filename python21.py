from abc import ABC

class Calculator:
    def logarithm(self,base,exponent):
        return 1

calculator = Calculator()
print(calculator.logarithm(2,8))


class Vehicle(ABC):
    def start_enigne(self):
        pass

class Car(Vehicle):
    def start_enigne(self):
        print('start {} engine'.format(self.model))
class Motorcycle(Vehicle):
    def start_enigne(self):
        print('start {} engine'.format(self.model))

car = Car()
car.model = 'Mercedes'
print(car.start_enigne())

motorcycle  = Motorcycle()
motorcycle.model = 'k1'
print(motorcycle.start_enigne())


    
    