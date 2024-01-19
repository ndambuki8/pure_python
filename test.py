#Python @property decorators
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    #getter method
    def get_temperature(self):
        print("Getting value.....")
        return self._temperature #underscore at the beginning is used to denote private variables
    
    #setter method
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    #create a property object
    temperature = property(get_temperature, set_temperature)