# Class Variable
# ! Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0 
    def __init__ (self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1
    def ger_brand(self):
        return self.brand 
        
    def full_name(self):
        return f"{self.brand} {self.model}" 
    
    def fuel_type(self):
        return " Diesel or Patrol" 
      
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    
Car("Tata","Nixon")
Car("Tata","Nixon")
Car("Tata","Nixon")
Car("Tata","Nixon")
Car("Tata","Nixon")
print(Car.total_car)   
                  