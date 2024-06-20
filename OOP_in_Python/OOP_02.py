# Inheritence
# ! Create a Electric Car Class that inherits from the car class and has an additional attributes battery  size.

class Car:
    def __init__ (self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}" 

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size



my_tesla = ElectricCar("Tesla","Model X", "90Kwh")
print(my_tesla.model)

print(my_tesla.full_name())
    
# my_car = Car("Porsche" , "GT3RS")   
    
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())