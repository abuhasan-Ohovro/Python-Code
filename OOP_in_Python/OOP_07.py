#  Multiple Inheritence
# !( Create two classes Battery and Engine , and let the Electric Car class inherit from both, demonstrating multiiople inheritence.)

class Car:
    def __init__ (self,brand,model):
        self.brand = brand
        self.model = model
        
class Battery :
    def Battery_info(self):
        return f"This is Battery!"
       
class Engine :
    def Engine_info(self):
        return f"This is Engine"
        
class ElectricVehicle(Battery,Engine,Car):
      pass      



my_new_tesla = ElectricVehicle("Tesla","Model X")
print(my_new_tesla.Engine_info())
print(my_new_tesla.Battery_info())