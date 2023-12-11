import module1

# original class
print(module1.Car.model) #vios
module1.Car.model = "wigo"
print(module1.Car.model)

car1 = module1.Car()
car1.brand = "Honda"
car1.model = "Brio"
print(f"{car1.brand} {car1.model}")

car2 = module1.Car()
car2.brand = "Ford"
car2.model = "Fiesta"
print(f"{car2.brand} {car2.model}")

emp1 = module1.Employee('Patrick','Starfish',45000)
print(emp1.fi)
print(emp1.la)
print(emp1.sa)



