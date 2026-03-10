class Temperature:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def toCelcius(self):
        celcius = (self.fahrenheit - 32) * 5/9
        return celcius

    def display(self):
        celcius = self.toCelcius()
        print(f"Fahrenheit: {self.fahrenheit}")
        print(f"Celcius: {celcius}")

#Object Creation
temp = Temperature(99)
temp.display()
