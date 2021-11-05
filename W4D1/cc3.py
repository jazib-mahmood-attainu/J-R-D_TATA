class Temperature:
    def convertFahrenheit(self,temp):
        self.temp = temp*(9/5) + 32
        print(f"Temperature in Fahrenheit is {self.temp}")
        
    def convertCelsius(self,temp):
        self.temp = temp*-32 * (5/9)
        print(f"Temperature in Fahrenheit is {self.temp}")

obj1 = Temperature()
obj1.convertFahrenheit(15)
