#Python @property decorators
class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    #getter method
    def get_temperature(self):
        return self._temperature #underscore at the beginning is used to denote private variables
    
    #setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

#create a new object 
human = Celsius(37)

#set the temperature
# human.temperature = 37

#Get the teamperature attribute
print(human.get_temperature())

#get the fahrenheit method
print(human.to_fahrenheit())

#constraint test
print(human.set_temperature(-300))

print(human.__dict__)