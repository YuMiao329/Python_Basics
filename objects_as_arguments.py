# Pass objects as an argument into a function

# car creating factory
class Car:
    color = None


class Motorcycle:
    color = None


# car color changing function
def change_color(car, color):  # here passing the car object as the first argument
    #                            car here is just a place holder for the object
    car.color = color


# create brand new (colorless cars from car factory)
car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

# paint new cars by color changing method
change_color(car_1, "red")
change_color(car_2, "white")
change_color(car_3, "blue")

# bike can also be used into the change color function even thought the argument
# is specified as a "car" which in that context is just a place holder
change_color(bike_1, "green")

print(car_1.color)  # red
print(car_2.color)  # white
print(car_3.color)  # blue
print(bike_1.color)  # green
