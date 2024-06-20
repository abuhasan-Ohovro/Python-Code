# Static Method 
# ! Add a static method to the Car class that returns a general description of a Car. 



class Car:
    total_car = 0 
    def __init__ (self,brand,model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1
    def ger_brand(self):
        return self.brand 
        
    def full_name(self):
        return f"{self.brand} {self.__model}" 
    
    def fuel_type(self):
        return " Diesel or Patrol" 
    @staticmethod
    def general_description(): #! (When static method is declared there is no need to give the self reference.)
        return "Cars are means of Transport"
    @property
    def model(self):
        return self.__model
      
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"
    
    
    
    
my_tesla = ElectricCar("Tesla","Model S","90 Kwh")    
print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))


    
# my_car = Car("Toyota","Supra") 
# my_car.model = "Corolla"   
# print(my_car.general_description())
# print(Car.general_description())

# print(my_car.model)
    