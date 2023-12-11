class Car:

    brand = "Toyota"
    model = "Vios"

    def greetclient():
        print("Welcome to Toyota!")
    
    def getmileage(liters,km):
        m = km/liters
        return m

class Employee:

    # constructor / initializer
    def __init__(self,firstname,lastname,salary):
        self.fi= firstname
        self.la = lastname
        self.sa = salary
        self.greetnewemp()
        
    def greetnewemp(self):
        print(f'{self.fi} {self.la} {self.sa}')

class House:

    address = "Pasig"

    def contactnum():
        return 9998877