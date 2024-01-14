#Python @property decorators
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

#create a new object 
human = Celsius(37)

#set the temperature
# human.temperature = 37

#Get the teamperature attribute
print(human.temperature)

#get the fahrenheit method
print(human.to_fahrenheit())