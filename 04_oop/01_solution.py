class Car:
    total_car = 0


    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def chai_brand(self):
        return self.__brand + " !"    

    def full_name(self):
        return f"{self.__brand} {self.__model}" 
    
    def fuel_type(self):
        return "petrol or diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transpot" 
    
    @property
  
    def model (self):
        return self.__model  

class ElectricCar(Car):
    def __init__(self, brand, model, bettery_size):
        super().__init__(brand, model)
        self.bettery_size = bettery_size

    def fuel_type(self):
        return " electric charge"


#my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

#print(isinstance(my_tesla, Car))
#print(isinstance(my_tesla, ElectricCar))
#print(my_tesla.model)
#print(my_tesla.brand)
#print(my_tesla.bettery_size)
#print(my_tesla.full_name())        
#print(my_tesla.fuel_type())


#my_car = Car("Tata", "Safari")
#my_car.model = "city"

#safariThree = Car("Tata", "Nexon") 
#print(safari.fuel_type())

#print(Car.total_car)
#print(my_car.model)


#my_car = car("Toyota", "Corolla") 
#print(my_car.brand)
#print(my_car.model) 
#print(my_car.full_name())
#new_my_car = car("Toyota", "Safari")
#print(new_my_car.model)


class Battery:
    def battery_info(self):
        return "this is battery"
    
class Engine:
    def engine_info(info):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())