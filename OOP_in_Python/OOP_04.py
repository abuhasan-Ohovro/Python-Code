# Polymorphism 
# ? Demonstrate polymorphism by defining a method fuel_type in both car and ElectricCar classes , but with different behaviours.

class Car:
    def __init__ (self, brand,model):
        self.brand = brand
        self.model = model
    
    def get_brand(self):
        return self.brand
    def full_name(self):
        return f"{self.brand} {self.model}"
    def fuel_type(self):
        return "Petrol or Diesel"     

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Elecric Charge"    
    
    
my_tesla = ElectricCar("Tesla","Model X","90Kwh")   
print(my_tesla.fuel_type())   

safari = Car("Tata","safari")

print(safari.fuel_type())
            












