from car import Car
#We define a term Car to make car models
#This object is been defined to make car models with details

#Together with file car.py
#In python, we dont need to parse self argument, it has been done automatically
car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make) #Chevy
print(car_1.model) #Corvette
print(car_1.year) #2021
print(car_1.color) #blue

car_1.drive() #This Corvette is driving
car_1.stop() #This Corvette is stopping

print(car_2.make) #Ford
print(car_2.model) #Mustang
print(car_2.year) #2022
print(car_2.color) #red

car_2.drive() #This Mustang is driving
car_2.stop() #This Mustang is stopping